![# Watson AI](presentation/card.png)

![Static Badge](https://img.shields.io/badge/OpenAI-LLM_API-%231D896B?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/Anthropic-LLM_API-%23D97757?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/Python-Build_with-%23FEDD55?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/bash-Build_with-%232D0B22?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/made_with-Love_and_AI-red?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/made_for-MacOS_%26_Linux-black?style=for-the-badge)



1. `Download` code, `install` dependencies and `run` the executable.
2. Start `watson` on your project main directory.
3. c**ode wherever you want with AI 🚀**

# 💡 How it works?

1. Run the `watson` executable in the terminal, in the directory your project is.
2. After that, just `write the prompts` in **any file inside the directory you're working on.**
3. Finally save the file and `watson` will answer the prompt inside the file you're on.

# 🪄 How to prompt?

## Write a `fast code` `-f`

`Fast` prompts **just consider the written prompt** to generate the code. It is for fast and initial uses.

```python
# -f create a code with pandas to read a .csv located in ../input/path/data.csv and also print its shape and display the head. finally drop all the rows with null values. 
import pandas as pd

# Read the CSV file
data = pd.read_csv('../input/path/data.csv')

# Print the shape of the DataFrame
print(data.shape)

# Display the head of the DataFrame
print(data.head())

# Drop all rows with null values
data_cleaned = data.dropna()
```

## Complete `lines needed` `-p`

`Partial` prompts **consider the written prompt and the content of the file** (excluding the prompt). It is for files that work alone or have functions.

```python
path = '../input/path/data.csv'

# Read the dataset
ds = pd.read_csv(path)
# print the shape
print(ds.shape)
# print the head
ds.head()

# -p drop all the rows with null values ```
```

## Code with `more files` `-F`

`Full` prompts consider **the written prompt, the content of the file and also the files saved on state,** Making it the more complete way to code. Mostly used to main files that include all the others.

### Having this file

```python
# functions.py
# -f create two functions with numpy, one to create a random matrix and the other to get the dot product of two given matrices 
import numpy as np

def create_random_matrix(rows, cols):
    return np.random.rand(rows, cols)

def dot_product(matrix_a, matrix_b):
    return np.dot(matrix_a, matrix_b)

# -p write a function to calculate the determinant of a given matrix 
def calculate_determinant(matrix):
    return np.linalg.det(matrix)
```

### Prompt on main file

```python
# main.py
# -a add functions.py 
# Added: functions.py 

# -F import all the functions from functions.py 
from functions import create_random_matrix, dot_product, calculate_determinant

# -F create two matrices, print their dot product and finally print the product of their determinants 
matrix_a = create_random_matrix(3, 3)  
matrix_b = create_random_matrix(3, 3)
dot_product_result = dot_product(matrix_a, matrix_b)  

print("Dot product of the two matrices:\n", dot_product_result)  

determinant_a = calculate_determinant(matrix_a)  
determinant_b = calculate_determinant(matrix_b)  

product_of_determinants = determinant_a * determinant_b  

print("Product of the determinants:\n", product_of_determinants)
```

## Manage files in `state` `-a`

These `actions` are used to manage the state.

- `ls` list the current considering files to prompts
- `add` add new files to consider in prompts
- `rm` removes files to consider in prompts
- `clear` removes all the considered files

# 💾 How to install?

## Installing the code

1. Download the code and open it.

```bash
git clone https://github.com/OmarSaldanna/watson-ai.git && cd watson-ai
```

1. Create a `virtual environment` to install the libraries (**inside the project dir**).

```bash
python3 -m venv venv && source venv/bin/activate
```

1. Install dependencies.

```bash
pip install -r requirements.txt
```

1. Set the file to be executable.

```bash
chmod 700 watson
```

1. Make the file visible on a `$PATH` dir. Make a soft link to a folder that appears on `$PATH` to make `watson` executable everywhere. In my case I have that folder added to `$PATH`

```bash
ln watson ~/bin/watson
```

## Setting your `api keys` and `main` path

1. Copy the path where the code is located and go to `global.conf` and paste that path in the variable named `MAIN`
2. Get an `API KEY` from `OpenAI` and `Anthropic` and paste them on `sample.keys`. Finally rename the file to `.keys`. You can get that keys here:
    1. [**Get OpenAI API key**](https://platform.openai.com/docs/quickstart)
    2. [**Get Anthropic API key**](https://docs.anthropic.com/en/api/getting-started)

### Note about models

**If you decide to only use one api**: `OpenAI` or `Anthropic` models, you can modify the `presets/models.json` file to just use the models and the api you want.

# ⚙️ About `presets/` and config files

- **`comments.json`** contains the syntax needed to comment the prompts on the files, since it depends on the type of file.
- **`models.json`** contains the params for the LLMs used: **system message, max tokens**. Also here you can decide what models from what API use:
    
    ```json
    "models": {
    		"gpt-4o-mini": "gpt",
    		"claude-3-5-haiku-latest": "claude",
    		"claude-3-5-sonnet-latest": "claude"
    	},
    
    	"probs": ".70 .20 .10"
    ```
    
    Watson will randomly choose a model to answer. based on the probs given there. Those above are the default presets. You can choose any model from both APIs now.
    
- **`prompts.json`** this file contains the relation between the prompt call and the function used. If you desire to add functions you will have to make changes on this file.
- **`state.json`** here is the code saved on state to make `full` prompts.

---

- **`.keys`** contains the keys needed to use the APIs from `OpenAI` and `Anthropic`.
- **`global.conf`** contains other special parameters to run the code.

# 💼 Features

## Executed in background

Just write `watson` on the terminal located on the project you're working on. **And That’s It**

## Use it everywhere

`Prompt Hamilton writing comments` and pressing `command + option`

**Note: delimiters and buttons can be changed in `global.conf`**

## **Use the LLMs you want**

The `LLMs used can be changed` and randomly chosen to test what models are better. 

## Chance of growing

The AI can be grown by the user, creating `more functions` and adding `more LLM’s` APIs.

# 📎 Links

- [**Get OpenAI API key**](https://platform.openai.com/docs/quickstart)
- [**Get Anthropic API key**](https://docs.anthropic.com/en/api/getting-started)

---

- [**OpenAI Models**](https://platform.openai.com/docs/models#current-model-aliases)
- [**Anthropic Models**](https://docs.anthropic.com/en/docs/about-claude/models)

# 🪸 Comments

Running on the `Lambda brain` it will be a mini Lambda `specialized in code tasks and other quick functions` it will have the models from `Anthropic and OpenAI`. The basics of Lambda are running in `ai.[py](http://AI.py)`. Thanks for reading my code.

