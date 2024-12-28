import os
import json
from anthropic import Anthropic

# Initialize the Anthropic client
client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))


def chat (prompt, model, system, tokens):
    try:
        # Make the API call
        message = client.messages.create(
            model=model,
            max_tokens=int(tokens),
            temperature=0,
            system=system,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        # Parse the response as JSON
        try:
            response_json = json.loads(message.content[0].text)
            return response_json
        except:
            # If response isn't valid JSON, wrap it in our format
            return {
                "code": message.content[0].text
            }
            
    except Exception as e:

        return { "error": str(e) }


# testing code
# prompt = "estamos en el archivo numbers.py\n\ngenera una matriz de ceros de 5x5 y llenala de numeros aleatorios, finalmente multiplicala por si misma"
# model = "claude-3-5-haiku-20241022"
# token_coef = 2
# system = "You are a code generation assistant. Always respond with valid JSON in the format: {\"code\": \"generated_code_here\"} Make sure the code is properly escaped for JSON."
# print(chat(prompt, model, system, token_coef))