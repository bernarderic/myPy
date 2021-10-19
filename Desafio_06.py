#crie um algoritmo que leia um numero e mostre o seu dobro
#triplo e a raiz quadrada--- {:.3f}= float com 3 casas decimais
n=int(input(' Digite um numero :'))
a=n*2
b=n*3
c=n**(1/2)
print('O numero digitado foi {}, o doblo é {} o triplo é {} a raiz é {:.3f}'.format(n,a,b,c))