# FHIRLLMs
This repository holds the code and files of the master's thesis "FHIR mapping via LLMs" by Christoph Stengel.
It holds the data used for the experiments as well as the results that are presented in the thesis.
The code "experiments.py" contains all experiments for the different models and if executed will run all experiments and start evaluating them. During the evaluation the code might crash! For the correct evaluation simply run "experiments_evaluation.py". This will create the evaluation of the results in the results folder.
To run the consistency experiment, simply run "experiments_GPT.py" and the experiment will be startet and evaluated.

Since some of the models are restricted, you have to put your HuggingFace access token and OpenAI token into a file called config.json. The config.json should look like this:<br>
{"HF_TOKEN":"HF_TOKEN",<br>
 "GPT_TOKEN":"GPT_TOKEN"}<br>

# CODE
To run the experiments, one needs the following Python libraries:<br>
torch<br>
transformers<br>
bitsandbytes<br>
accelerate<br>
openai<br>
fhir.resources<br>
elementpath<br>
