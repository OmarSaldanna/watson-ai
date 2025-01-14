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
	# based on current file, get the current dir
	last_slash_idx = len(current_file.file_path) - current_file.file_path[::-1].index('/')
	current_dir = current_file.file_path[:last_slash_idx]

	##################### add files ######################

	if prompt.startswith("add"):
		answer = "Added: "
		# catch the files
		files = prompt.split(" ")[1:]
		# for every file given
		for f in files:
			# add the current path to the file
			file = current_dir + f
			# try to read the file
			try:
				# save it on state
				state[file] = read_file(file)
				# save the file as well read
				answer += f + " "
			except:
				continue
		# finally write state
		state.write()

	##################### remove files ######################

	elif prompt.startswith("rm"):
		answer = "Removed: "
		# catch the files
		files = prompt.split(" ")[1:]
		# for every file given
		for f in files:
			file = current_dir + f
			# try to remove the file
			try:
				# save it on state
				del(state.dic[file])
				# save the file as well read
				answer += f + " "
			except:
				continue
		# finally write state
		state.write()

	##################### clear files ######################

	elif prompt.startswith("clear"):
		answer = "State clear"
		# clear the state
		state.dic = {}
		# finally save changes
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