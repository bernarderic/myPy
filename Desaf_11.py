#faça um progrma que leia a largura de uma parede em metros calcule a sua area e
#a quantidade de tinta nescessária para pintar sabendo que cada litro de tinta 
# pinta uma área de 2 m2
l=float(input('Qual é a largura da pareda em metros? '))
h=float(input('Qual é a altura da parede em metros?'))
a= l*h
qtd= a /2
print('A quantidade de tinta necessária será de {:.2f} litros, para pintar essa parede'.format(qtd))