"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma
casa . O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal sabendo que ela não poderá exceder 30% do salário ou
o empréstimo será negado."""
casa=float(input('Qual o valor da casa? '))
sal=float(input('Digite o seu salário ?'))
anos=float(input('Emq uantos anos vc pretende financiar? '))
meses= anos*12
prest= casa/meses
sal30= sal*0.3
if prest>sal30:
    print('Empréstimo negado, a prestação {:.2f} é maior que 30% do seu salário {:.2f}'.format(prest,sal30))
else:
    print('Empréstimo aprovado, bem vindo ao rat race!')
print('Fim')