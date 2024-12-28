import json
from openai import OpenAI

# instance this
client = OpenAI()

def chat (prompt, model, system, tokens): 
  # and use the LLM
  try:
    response = client.chat.completions.create(
      model=model,
      messages=[
        {
          "role": "developer",
          "content": system
        },
        {
          "role": "user",
          "content": prompt
        }
      ],
      max_tokens=int(tokens),
      response_format={
        "type": "json_object"
      }
    )
    # return the response
    try:
      return json.loads(response.choices[0].message.content)
    except:
      return { "code": response.choices[0].message.content}

  except Exception as e:
    return { "error": str(e) }


# # testing code 
# prompt = "estamos en el archivo numbers.py\n\ngenera una matriz de ceros de 5x5 y llenala de numeros aleatorios, finalmente multiplicala por si misma"
# model = "gpt-4o-mini"
# token_coef = 2
# system = "You are a code generation assistant. Always respond with valid JSON in the format: {\"code\": \"generated_code_here\"} Make sure the code is properly escaped for JSON."
# print(chat(prompt, model, system, token_coef))