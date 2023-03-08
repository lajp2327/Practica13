import random
import string

def generar_contraseña(long=8, mayusculas=False, especiales=False):
    caracteres = string.ascii_lowercase
    if mayusculas:
        caracteres += string.ascii_uppercase
    if especiales:
        caracteres += string.punctuation
    return ''.join(random.choice(caracteres) for i in range(long))
