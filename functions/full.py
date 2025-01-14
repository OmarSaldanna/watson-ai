# import the model selector
from modules.selector import select_model


# full considers the content of the file, and the added files
def main (params):
    # get the prams
    prompt, state, info, current_file = params
    # select the model
    llm, model = select_model(info)
    # include the file content in the prompt
    new_prompt = f"Current file: [{current_file.file_path}]\n{current_file.content}\n[end of file]\n\n"
    new_prompt += "Context files: "
    # add the files
    for key in state.dic.keys():
        new_prompt += f"[{key}]\n" + state[key] + "\n[end of file]"
    # and the prompt    
    new_prompt += "\nPrompt: " + prompt
    # the system message
    system = info['system'] + " Considering current file and the context files, answer the prompt ONLY with an independant new code to complete the current file code."
    # use the model
    response = llm.chat(new_prompt, model, system, info['max-tokens'])
    # and return
    return response['code']