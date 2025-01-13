# -f crea una fucnión de numpy para crear dos matrices simples 
import numpy as np

def crear_matrices():
    matriz_a = np.array([[1, 2], [3, 4]])
    matriz_b = np.array([[5, 6], [7, 8]])
    return matriz_a, matriz_b

# -p ahora crea una función para obtener los determinantes de las matrices y usa las funciones para crear dos matrices e imprimir sus determinantes 
def obtener_determinantes():
    matriz_a, matriz_b = crear_matrices()
    det_a = np.linalg.det(matriz_a)
    det_b = np.linalg.det(matriz_b)
    print(f"Determinante de matriz A: {det_a}")
    print(f"Determinante de matriz B: {det_b}")

obtener_determinantes()
