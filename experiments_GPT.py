import os

# Added to check if it prevents cuda out of memory
#os.environ['CUDA_VISIBLE_DEVICES'] = '0'

import json
import torch
from transformers import (AutoTokenizer,
                          AutoModelForCausalLM,
                          BitsAndBytesConfig,
                          pipeline)
import datetime
import time
import subprocess
from openai import OpenAI
import xml.etree.ElementTree as ET

from fhir.resources.bundle import Bundle
from fhir.resources.patient import Patient
import pathlib


models = ["gpt-4"]
models_name = ["gpt-4"]
experiments = ["dm1"]

NUM_EXPERIMENTS = 100

HF_TOKEN = ""
GPT_TOKEN = ""
FHIR_PROFILE = "Person"
FHIR_PROFILE_DESCRIPTION = ""

# input_example2 is the json that is used for testing the correctness
input_usecase_str = ""
input_example_str = "{example json}"
output_example_str = ""
output_example = {}
output_usecase_str = ""
output_usecase = {}

def save_results( path, file_name, results="none"):

    if not os.path.exists(path):
        os.makedirs(path)

    file = open(path+file_name, "w+")
    file.writelines(results)
    file.close()

def save_intermediate_results( path, file_name, results="none"):

    if not os.path.exists(path):
        os.makedirs(path)

    file = open(path+file_name, "w+")
    file.writelines(results)
    file.close()

def read_xml_file(file_path):
    try:
        # Parse the XML file
        tree = ET.parse(file_path)        
        # Get the root element
        root = tree.getroot()
        # Convert the XML tree to a string
        xml_string = ET.tostring(root, encoding='unicode')
        return xml_string
    except ET.ParseError as e:
        return f"Error parsing XML: {e}"

def startup():

    global HF_TOKEN
    global GPT_TOKEN
    global FHIR_PROFILE_DESCRIPTION

    global input_example
    global input_example_str
    global input_usecase
    global input_usecase_str
    global output_example
    global output_example_str
    global output_usecase
    global output_usecase_str

    config_data = json.load(open("config.json"))
    HF_TOKEN = config_data["HF_TOKEN"]
    GPT_TOKEN = config_data["GPT_TOKEN"]   

    FHIR_PROFILE_DESCRIPTION = read_xml_file('Data/Patient_Description_alternative.xml')     
    
    input_example_str = read_xml_file('Data/Pat_Tumor1_Behandlungsende_ST_01.xml') 

    with open('Data/Patient_fhir_01.json') as f:
        output_example = json.load(f)
        output_example_str = json.dumps(output_example)
        f.close()

    
    input_usecase_str = read_xml_file('Data/Pat_Tumor1_Behandlungsende_ST_04.xml')
        

    with open('Data/Patient_fhir_04.json') as f:
        output_usecase = json.load(f)
        output_usecase_str = json.dumps(output_usecase)
        f.close()

def ready_model(model_name):
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_use_double_quant=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16
    )

    tokenizer = AutoTokenizer.from_pretrained(model_name,
                                          token=HF_TOKEN)

    tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map="cuda",
        quantization_config = bnb_config,
        token=HF_TOKEN
    )

    text_generator = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        do_sample=True,
        temperature=0.7,
        # default would be 50
        top_k=10,
        min_new_tokens = 200,
        max_new_tokens=10000
    )

    return text_generator

def get_response(text_generator, prompt):
    sequences = text_generator(prompt)
    gen_text = sequences[0]["generated_text"]
    return gen_text

def get_prompt(experiment):
    match experiment: # cg -> code generation, dm -> direct FHIR mapping
        case "cg1":
            prompt = "You are a Python Software Engineer and are asked to create a Python programm that turns the content of a xml file into a specific json. The xml file contains data from a database while the json is supposed to be a FHIR resource json. The input looks like this: \n" +\
                  input_example_str + " while the output should look like this: \n" +\
                      output_example_str + ". Create runnable python code for this task that only prints the resulting FHIR json to the console. Only return the python code!" 
        case "cg2":
            prompt = "You are a Python Software Engineer and are asked to create a Python programm that turns the content of a xml file into a specific json. The xml file contains data from a database while the json is supposed to be a FHIR resource json. The input looks like this: \n" +\
                  input_example_str + " while the output should look like this: \n" +\
                      output_example_str + ". The resulting FHIR profile is called " + FHIR_PROFILE +\
                        ". Create runnable python code for this task that only prints the resulting FHIR json to the console.  Only return the python code!"
        case "cg3":
            prompt = "You are a Python Software Engineer and are asked to create a Python programm that turns the content of a xml file into a specific json. The xml file contains data from a database while the json is supposed to be a FHIR resource json. The input looks like this: \n" +\
                  input_example_str + " while the output should look like this: \n" +\
                      output_example_str + ". The resulting FHIR profile is calles " + FHIR_PROFILE +\
                        ". The description of the  FHIR profile is the following: \n" + FHIR_PROFILE_DESCRIPTION + \
                                "Create runnable python code for this task that only prints the resulting FHIR json to the console.  Only return the python code!"    
 
        case "cg4":
            prompt = "You are a Python Software Engineer and are asked to create a Python programm that turns the content of a xml file into a specific json. The xml file contains data from a database while the json is supposed to be a FHIR resource json. The input looks like this: \n" +\
                  input_example_str + ". Create runnable python code for this task that only prints the resulting FHIR json to the console. Only return the python code!" 

        case "cg5":
            prompt = "You are a Python Software Engineer and are asked to create a Python programm that turns the content of a xml file into a FHIR json. The input looks like this: \n" +\
                  input_example_str + ". The runnable python code for this task that only prints the resulting FHIR json to the console looks like this:" 
                        
        case "dm1":
            prompt = "You are tasked with turning this input xml file \n" + input_usecase_str +\
                  " into a valid FHIR json.\n" + \
                    "Additionally you are given two other files as example. The first one is a xml similar to the input file, while the second one is the corresponing FHIR json." +\
                          "The example input xml is this: \n" + input_example_str + " And the corresponding output FHIR json is this: \n" + output_example_str + "\n" + \
                          "Provide the corresponing output FHIR json to the first input xml. Only return the json!"
        case "dm2":
            prompt = "You are tasked with turning this input xml file \n" + input_usecase_str +\
                  " into a valid FHIR json.\n" + \
                    "Additionally you are given two other files as example. The first one is a xml similar to the input file, while the second one is the corresponing FHIR json." +\
                          "The example input xml is this: \n" + input_example_str + " And the corresponding output FHIR json is this: \n" + output_example_str + "\n" + \
                          "The resulting FHIR profile is called " + FHIR_PROFILE +\
                              "Provide the corresponing output FHIR json to the first input json. Only return the json!"
        case "dm3":
            prompt = "You are tasked with turning this input xml file \n" + input_usecase_str +\
                  " into a valid FHIR json.\n" + \
                    "Additionally you are given two other files as example. The first one is a xml similar to the input file, while the second one is the corresponing FHIR json." +\
                        "The example input xml is this: \n" + input_example_str + " And the corresponding output FHIR json is this: \n" + output_example_str + "\n" + \
                        "The resulting FHIR profile is called " + FHIR_PROFILE +\
                        ". The description of the  FHIR profile is the following: \n" + FHIR_PROFILE_DESCRIPTION + \
                        "Provide the corresponing output FHIR json to the first input json. Only return the json!"

        case "dm4":
            prompt = "You are tasked with turning this input json file \n" + input_usecase_str +\
                  " into a valid FHIR json. Please provide the according FHIR json to this input. Only return the json!"
            
        case "dm5":
            prompt = "You are tasked with turning this input json file \n" + input_usecase_str +\
                  " into a valid FHIR json. The according FHIR json to this input looks like this:"
            
        case "dm6":
            prompt = "Create a Person FHIR profil json."
    return prompt            

def levenshteinFullMatrix(str1, str2):
    m = len(str1)
    n = len(str2)
 
    # Initialize a matrix to store the edit distances
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
 
    # Initialize the first row and column with values from 0 to m and 0 to n respectively
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
 
    # Fill the matrix using dynamic programming to compute edit distances
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                # Characters match, no operation needed
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # Characters don't match, choose minimum cost among insertion, deletion, or substitution
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
 
    # Return the edit distance between the strings
    return dp[m][n]


if __name__ == "__main__":
    print("------------------------------------")
    print("Setting up experiments")
    print("------------------------------------")

    startup()
    result_matrix = []
    chatgpt = False
    client = OpenAI(
        api_key=GPT_TOKEN
    )
    
    print("------------------------------------")
    print("Setup done. Starting experiments.")
    print("------------------------------------")

    save_intermediate_results_str = ""

    for idx, model in enumerate(models):
        print("------------------------------------")
        print("starting on model:" + model)
        print("------------------------------------")
        

        for idx2, experiment in enumerate(experiments):
            print("starting on experiment " + experiment)
            for idx3 in range(NUM_EXPERIMENTS):
                print("------------------------------------")
                print("starting on execution:" + str(idx3))
                print("------------------------------------")
                executed = True
                counter = 0
                while True:
                    
                    try:
                        if "gpt" in model:
                            chatgpt = True
                        else:
                            chatgpt = False
                            text_generator = ready_model(model)
                    except:
                        print("Readying model did not work. Trying again in 5 min! Attempt: {counter}")
                        time.sleep(300)
                        counter += 1
                        if counter > 9:
                            executed = False
                            break
                        continue
                    break

                if not executed:
                    continue  
                
                result_matrix.append([])
                result_matrix[idx3].append(model)
                result_matrix[idx3].append(experiment)
                result_matrix[idx3].append(idx3)
                
                start_time = datetime.datetime.now().replace(microsecond=0)

                prompt = get_prompt(experiment)
                
                if chatgpt:
                    gpt_counter = 0
                    while True:
                        try:
                            completion = client.chat.completions.create(
                            model=model,
                            messages=[
                                # TODO: possible experiment is to tell ChatGPT what it is
                                #{"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
                                {"role": "user", "content": prompt},
                            ],
                            temperature=0.7 
                            )
                            
                            response = completion.choices[0].message.content
                        except Exception as e:
                            print(f"Executing GPT did not work. Trying again in 5 min! Attempt: {gpt_counter}")
                            print("Reason: \n" + str(e))
                            gpt_counter += 1
                            if gpt_counter > 9:
                                response = f"Executing {model} did not work. \n" + str(e)
                                break
                            time.sleep(300)
                            
                            continue
                        break
                else:
                    try:
                        response = get_response(text_generator, prompt)
                        #response = prompt
                    except Exception as e:
                        response = "model crashed. \n" + str(e)
                        


                if "dm" in experiment:
                    save_results("results_gpt/dm/", models_name[idx] + "_experiment_" + experiment + "_execution_" + str(idx3) + ".txt", response)
                    end_time = datetime.datetime.now().replace(microsecond=0)
                    result_matrix[idx3].append(str(end_time-start_time))
                    save_intermediate_results_str += str(result_matrix[idx3]) + "/n"
                    save_intermediate_results("results_gpt/", "intermediate_evaluation_matrix.txt", save_intermediate_results_str)

                print("done")
                print("------------------------------------")
            print("done with the model!")
            print("------------------------------------")

    print("------------------------------------")
    print("All experiments have been run. Starting evaluation.")
    print("------------------------------------")
    

    for idx, model in enumerate(models):
        print("Starting evaluation of " + model)
        print("------------------------------------")
        for idx2, experiment in enumerate(experiments):
            for idx3 in range(NUM_EXPERIMENTS):
                # Evaluation of direct mapping experiments
                if "dm" in experiment:
                    with open("results_gpt/dm/" + models_name[idx] + "_experiment_" + experiment + "_execution_" + str(idx3) + ".txt", "r") as f:
                    #with open("Data/fhir_bundle_datablock_valid_meona.json", "r") as f:
                        
                        try:
                            result_json = json.load(f)
                            result_json_str = json.dumps(result_json)
                            functioning_json = True
                            print("Found functioning json!")
                        except:
                            f.close()
                            print("No functioning json found, using output as string!")
                            functioning_json = False
                            #with open("Data/fhir_bundle_datablock_valid_meona.json", "r") as g:
                            with open("results_gpt/dm/" + models_name[idx] + "_experiment_" + experiment + "_execution_" + str(idx3) + ".txt", "r") as g:
                                try:
                                    result_json = {}
                                    result_json_str = g.read()
                                except:
                                    print("------------------------------------")
                                    print("------------------------------------")
                                    print("------------------------------------")
                                    print("everything went wrong!")
                                    print("------------------------------------")
                                    print("------------------------------------")
                                    print("------------------------------------")

                            g.close()
                            

                    #print(result_json_str)
                    levenshtein_distance = levenshteinFullMatrix(result_json_str, output_usecase_str)
                    try:
                        entry_length = len(result_json["entry"])
                    except:
                        entry_length = -1

                    # Check whether the whole file is a correct fhir bundle
                    try:
                        bundle = Bundle.parse_obj(result_json)
                        is_bundle = bundle.resource_type == "Bundle"
                    except:
                        is_bundle = False

                    # Check whether the whole resource in entry[0] is a correct fhir patient
                    try:
                        pat = Patient.parse_obj(result_json["entry"][0]["resource"])
                        is_patient = pat.resource_type == "Patient"
                    except:
                        is_patient = False

                    # To make more comparable, we could devide the levenshtein distance through the length of the longer string to get a "normalized" number
                    result_matrix[idx3].append(entry_length) 
                    result_matrix[idx3].append(levenshtein_distance)
                    result_matrix[idx3].append(is_bundle)
                    result_matrix[idx3].append(is_patient)
                    result_matrix[idx3].append(functioning_json)

                # Evaluation of code generation experiments   
                else:
                    print("------------------------------------") 
                    print("Something went wrong!!!")
                    print("------------------------------------") 
                    
                

        print("Done evaluating " + model)
        print("------------------------------------") 



    file_str = ""

    for id in range(NUM_EXPERIMENTS):
        result = result_matrix[id]
        print(result)
        file_str += str(result) + "\n"

    save_results("results_gpt/", "evaluation_matrix.txt", file_str)
    print("Evaluation done.")





