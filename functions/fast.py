# import the model selector
from modules.selector import select_model


# fast does not consider nothing for the prompt
def main (params):
	# get the prams
	prompt, _, info, _ = params
	# randomly chose the model
	llm, model = select_model(info)
	# use the model
	response = llm.chat(prompt, model, info['system'], info['max-tokens'])
	# and return
	return response['code']