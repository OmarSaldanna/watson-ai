# import the models
from models import gpt, claude
# to chose a model
import random


# fast does not consider nothing for the prompt
def main (params):
	# get the prams
	prompt, _, info, current_file = params
	# this is arbitrary, I have more credits on OpenAI
	available_models = [
		(gpt, info['gpt']), (gpt, info['gpt']), (claude, info['claude'])
	]
	# randomly chose the model
	llm, model = random.choice(available_models)
	print("used:", model)
	# include the file content in the prompt
	new_prompt = f"[{current_file.file_path}]\n{current_file.content}\n[end of file]\n" + prompt
	# the system message
	system = info['system'] + " Considering the file, answer ONLY with an independant new code to complete the given code with the request."
	# use the model
	print(new_prompt)
	print(system)
	response = llm.chat(new_prompt, model, system, info['max-tokens-coef'])
	print(response)
	# and return
	return response['code']