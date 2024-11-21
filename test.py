# import the models
from models import gpt, claude
# to chose a model
import random

a = 1
b = 2

def suma (a,b):
	return a+b


# -p ahora escribe una función para restar dos numeros 
def resta(a, b):
	return a - b

# -p ahora mediante random haz que se ejecute aleatoriamente suma o resta sobre a y b 

# elegir aleatoriamente una función
resultado = random.choice([suma, resta])(a, b)
print(f'El resultado es: {resultado}')


# -p independientemente, dame una función para guardar un string en un nuevo archivo txt 
def guardar_en_archivo(nombre_archivo, contenido):
	with open(nombre_archivo, 'w') as archivo:
		archivo.write(contenido)


# -p ahora haz que ese contenido del print se guarde en un archivo llamado resultado.txt 
resultado = random.choice([suma, resta])(a, b)
print(f'El resultado es: {resultado}')
guardar_en_archivo('resultado.txt', f'El resultado es: {resultado}')
