from modules.files import FILE, JFILE
import importlib
import os

class AI:

	def  __init__ (self):
		# instance the state file
		self.state = JFILE(os.environ["MAIN"] + "/presets/state.json")
		# the prompt delimiters
		self.delimiters = JFILE(os.environ["MAIN"] + "/presets/prompts.json")
		# and the models info
		self.models = JFILE(os.environ["MAIN"] + "/presets/models.json")

	def __call__ (self, current_file):
		# instance the current file
		self.current_file = FILE(current_file, self.delimiters.dic.keys())
		# get the prompt
		delimiter, prompt = self.current_file.get_prompt()
		# check if there's prompt:
		if prompt == '':
			# print(">> No prompt to process, skipping")
			return
		# try:
		# based on delimiter use the function
		function = self.delimiters[delimiter]
		# form the params to pass them to the function
		params = (prompt, self.state, self.models, self.current_file)
		# get the function
		function = importlib.import_module(f"functions.{function}")
		# get an answer
		answer = function.main(params)
		# if there was an answer then write it
		if answer:
			self.current_file.post_answer(answer)
		# else 
		else:
			print("promt executed, no answer receipt")
		# except:
		# 	os.system('osascript -e \'display notification "Error in watson prompt" with title "Watson"\'')
