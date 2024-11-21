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
	# use the model
	response = llm.chat(prompt, model, info['system'], info['max-tokens-coef'])
	# and return
	return response['code']