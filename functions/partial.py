# import the model selector
from modules.selector import select_model


# partial considers the content of the file
def main (params):
	# get the prams
	prompt, _, info, current_file = params
	# select the model
	llm, model = select_model(info)
	# include the file content in the prompt
	new_prompt = f"[{current_file.file_path}]\n{current_file.content}\n[end of file]\n" + prompt
	# the system message
	system = info['system'] + " Considering the file, answer ONLY with an independant new code to complete the given code with the request."
	# use the model
	response = llm.chat(new_prompt, model, system, info['max-tokens'])
	# and return
	return response['code']