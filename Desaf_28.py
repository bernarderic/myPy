"""Escrever um programa que faça o computador pensar em um numero interior de 0-5 
e peça para o usuário tentar adivinhar qual foi o numero escolhido
pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu"""
#from time import sleep
#sleep(3)#3 segundos pra fazer o computador pensar
from random import randint
n=randint(0,5)
user=int(input('Tente adivinhar o numerro de 0 a 5: '))
if user == n:
    print('Voce acertou!')
else: 
    print('perdeu!')
   
print('Fim')

