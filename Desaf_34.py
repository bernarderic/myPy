"""Escreva um progrma que pergunte o salário de um funcionário e calcule
o valor do seu aumento.
Para salários superiores a R$1.250 aumneto de 10%
Para salários inferiores ou iguais aumento de 15%"""
sal=float(input('Digite o salário atual: '))
f1=1250
if sal > f1:
    print('Seu novo salário com 10% de aumento será {:.2f}'.format(sal*1.1))
else:
    print('Seu novo salário com 15% de aumento será de: {:.2f}'.format(sal*1.15))