from modules.files import JFILE
import os

# current path where watson was ran
current_path = os.environ["CURRENT"] + "/"
# get the comments file
comments = JFILE(os.environ["MAIN"] + "/presets/comments.json")

# actions to handle the app and files
def main (params):
	# get the prams
	prompt, state, _, current_file = params
	# stablish the correct answer
	answer = ""
	# remove spaces from prompt
	prompt = prompt.strip()

	##################### change current file ######################

	if prompt.startswith("mv"):
		# get the current file from the prompt
		new_file = current_path + prompt.split(" ")[1]
		# check if exists
		try:
			read_file(new_file)
		except:
			return f"file {new_file} not found"
		# if exists, change the file
		current_file.file_path = new_file
		# also save the new comments
		try:
			current_file.comment = comments['.' + new_file.split('.')[-1]]
		except:
			current_file.comment = comments["default"]
		# also return the answer
		answer = "Waiting orders"

	##################### add files ######################

	elif prompt.startswith("add"):
		answer = "Read: "
		# catch the files
		files = prompt.split(" ")[1:]
		# for every file given
		for f in files:
			# add the current path to the file
			file = current_path + f
			# try to read the file
			try:
				# save it on state
				state[file] = read_file(file)
				# save the file as well read
				answer += f + " "
			except:
				pass
		# finally write state
		state.write()

	##################### list files ######################

	elif prompt.startswith("ls"):
		# show every file in state
		answer = "In state:\n\t" + '\n\t'.join(state.dic.keys())

	##################### End ######################

	return answer



# function to read files
def read_file(path):
    with open(path, 'r') as file:
    	# read the file
        return file.read()