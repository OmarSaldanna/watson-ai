import importlib
import numpy as np


# function to select the model on every call
def select_model (info):
	# get the available models
	models = list(info["models"].keys())
	# the probabilities
	probs = info["probs"].split()
	probs = [float(p) for p in probs]
	# check the parameters
	if sum(probs) != 1:
		raise ValueError("Probs must sum 1 in models.json")
	if len(models) != len(probs):
		raise ValueError("len of probs and models must be the same")
	# select the model's name
	model = np.random.choice(models, p=probs)
	# get the module name
	module_name = info["models"][model]
	# then import the model
	module = importlib.import_module(f"models.{module_name}")
	# an advice
	print("using", model)
	# finally return the model
	return module, model