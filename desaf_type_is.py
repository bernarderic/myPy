from typing import TypeAlias


""" faça um programa que leia algo pelo teclado e mostre na Tela 
o seu tipo primitivo e todas as informações possiveis sobre ele.
 """
n = input('digite algo : ')
print('tipo :', type(n))
print('é um alfa numerico? :', n.isalnum())
print('é alpha? ', n.isalpha())
print('é códidigo ascii? ', n.isascii())
print('é decimal? ', n.isdecimal())
print('é um digito? ', n.isdigit())
print('é um identificador? ',n.isidentifier())
print('é em letra minuscula? ',n.islower())
print('é em letra maiuscula? ',n.isupper())
print('é imprimivel? ', n.isprintable())
print('é um espaço? ', n.isspace())
print('é um numero? ',n.isnumeric())
print('é um titulo? ', n.istitle())