"""crie um programa que leia um numero inteiro e  mostre se ele é par ou impar"""
num=int(input ('Digite um numero inteiro: '))
resto= num % 2
if resto == 0:
    print('É par!')
else:
    print('É impar!')

print("=="* 10)
