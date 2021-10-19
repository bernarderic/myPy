#crie um programa que leia qto dinheiro tem na carteira
#e mostre o valor dolar
n=int(input('Quanto tem na carteira? '))
d= n / 3.27
print('Com seus R$ {:.2f} vc pode comprar apenas USD {:.2f} dólares'.format(n,d))