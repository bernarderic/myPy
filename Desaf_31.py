"""Desenvolva um programa que pergunte a distância de uma viagem em km
Calcule o preço da passagem cobrando r$ 0,50 por km para viagens de até 
200km e R$ 0.45 para as viagens mais longas"""
km=int(input('Qual a distância em km da viagem?'))
if km <= 200:
    val1= km*0.5
else:
    val1=km*0.45
    
print('O valor da viagem é de R${:.2f}'.format(val1))
