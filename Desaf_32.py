"""faça um programa que leia um ano qualquer e infor se ele é Bisexto"""
#if ano % 4 == 0 é bissexto
#from datetime import date --> data atual
ano=int(input('Digite o ano: '))
resto =ano / 4

if resto.is_integer() == True:
    print('Bisexto')
else:
    print('não é Bisexto')
