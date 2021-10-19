#escreva um programa que leia em metros e mostre em centimetros e milimetros
n=int(input('Digite quantos metros é a medida :'))
a= n*100
b=n*1000
print('O valor de {} metroes corresponte a {} centimetros e a {} milimetros'.format(n,a,b))