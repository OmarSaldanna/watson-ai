# part of Lambda's memory
import os
import json

# class to handle code files
class FILE:
  
  def __init__ (self, file_path: str, delimiters: list):
    # save the file path
    self.file_path = file_path
    # load the comments
    self.comments = JFILE(os.environ["MAIN"] + "/presets/comments.json")
    # save the delimiters
    self.prompt_delimiters = delimiters
    # file extension
    extension = '.' + file_path.split('.')[-1]
    # get the comment syntax
    try:
      self.comment = self.comments[extension]
    except:
      self.comment = self.comments["default"]

  # function to comment a line
  def comment_line (self, line: str):
    commented_line = ""
    # see where the text begins
    begins = line.index(line.strip()[0])
    # add the previous tabs or spaces
    commented_line += line[:begins]
    # finally the rest
    commented_line += self.comment[0] + ' ' + line.strip() + ' ' + self.comment[1]
    # and return
    return commented_line

  # function to get the query
  def get_prompt (self):
    prompt = ""
    delimiter = ""
    self.file_content = ""
    # open the current file
    with open(self.file_path, 'r') as file:
      # iterate the lines
      for i, line in enumerate(file):
        # if the line starts with one of the delimiters
        if line.strip()[:2] in self.prompt_delimiters:
          # set the delimiter as the first one
          if not delimiter:
            delimiter = line.strip()[:2]
          # save the prompt
          prompt += line.strip()[2:] + " "
        # is the rest of the file
        else:
          self.file_content += line
    # return the query
    return delimiter, prompt.strip()

  # function to append the code after the query
  def post_answer (self, answer: str):
    already_comented_prompt = False
    already_posted_answer = False # when the prompts are in last lines
    # open the current file
    with open(self.file_path, 'r') as current_file:
      # create a temporary file
      with open(self.file_path + os.environ['TMP_EXT'], 'w') as temp_file:
        # iterate the lines of the current file
        for i, line in enumerate(current_file):
          # define the content to write
          line_to_write = line
          # if the line starts with one of the delimiters
          if line.strip()[:2] in self.prompt_delimiters:
            # comment the prompt line
            commented_line = self.comment_line(line)
            # active the flag
            already_comented_prompt = True
            # set as write line
            line_to_write = commented_line
          # if the line doesn't starts with a delimiter and the flag
          # is enabled, then here comes the answer
          elif already_comented_prompt and not already_posted_answer:
            # alter the flag
            already_comented_prompt = False
            # start writing the anser
            temp_file.write("\n")
            for answer_line in answer.split("\n"):
              # each line
              temp_file.write(answer_line)
              # and the enter. These was implemented to not write
              # everything in a line sometimes
              temp_file.write("\n")
            # the last line
            temp_file.write("\n")
            # and continue with the rest of the file
            continue
            # and the other flag
            already_posted_answer = True
          # write the line
          temp_file.write(line_to_write)
        # in case of last line prompts
        if not already_posted_answer:
          temp_file.write("\n" + answer + "\n")
        # finally convert the current file into the temp file
        print(f">>> Writing file {self.file_path}\n")
        os.system(f"mv \"{self.file_path + os.environ['TMP_EXT']}\" \"{self.file_path}\"")

# class to handle json files
class JFILE:
  # open the json
  def __init__ (self, file_path: str):
    # open the dic
    try:
      # save the file path
      self.file_path = file_path
      # open the json file
      with open(self.file_path, "r") as f:
        # save the info
        self.dic = json.load(f)
    except:
      raise ValueError(f"Error: bad json file {file_path}")

  # save changes
  def write (self):
    with open(self.file_path, "w") as write_file:
      json.dump(self.dic, write_file, indent=int(os.environ["INDENT"]), ensure_ascii=False)

  # update file
  def update (self, data: dict):
    # iterate the new dic with the changes
    for key, value in data.items():
      # make the changes
      self.dic[key] = value
    # and save them
    with open(self.file_path, "w") as write_file:
      json.dump(self.dic, write_file, indent=int(os.environ["INDENT"]), ensure_ascii=False)

  # select items
  def __getitem__ (self, key: str):
    try:
      return self.dic[key]
    except:
      raise KeyError(key)

  # set items
  def __setitem__ (self, key: str, value):
    try:
      self.dic[key] = value
    except:
      raise KeyError(key)

  # in case of print the memory
  def __str__ (self):
    return self.dic