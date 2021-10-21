"""Desenvolva um programa que leia o comprimento de tres retas
e diga ao usuário se elas podem ou não formar um triângulo"""
l1=float(input('digite o primeiro lado:'))
l2=float(input('digite o segundo lado:'))
l3=float(input('digite o terceiro  lado:'))
if l1<l2+l3 and l2<l1+l3 and l3<l1+l2:
    print('ok pode formar triângulo!')
else:
    print('não é possivel formar o triangulo')