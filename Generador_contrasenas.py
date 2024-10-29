import random

letras = 'abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUYXZ'
numeros = '0123456789'
simbolos = '@#$%&*.'

unir = f'{letras}{numeros}{simbolos}'
longitud = int(input('Elige la cantidad de caracteres de la contrasena: '))
contrasena = random.sample(unir, longitud)
password_final = "".join(contrasena)
print(password_final)

