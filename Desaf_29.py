"""Escreva um programa que leia a velocidade de um carro
Se ele ultrapassar  os 80km/h mostre uma mensagem 
dizendo que ele foi multado .
A multa vai custar R7,00 por cada km acima do limite """
velo=float(input('Digite a velocidade do carro: '))
if velo > 80:
    print('Foi multado!')
    m1= velo-80
    m2= m1*7
    print('Pague a multa de : R$ {:.2f}'. format(m2))


