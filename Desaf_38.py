'''Escrever um programa que leia dois numeros inteiros e compare-os mostrando na tela
uma mensagem:
o primeiro valor e´maior]
o segundo valor é  maior
não exite valor maior os dois são iguais'''

n1=int(input('Digite o primeiro numero inteiro :'))
n2=int(input('Digite o segundo numero inteiro :'))

if n1> n2:
    print('O primeiro número {} é maior que o segundo numero {}'. format(n1,n2))
elif n2>n1:
    print('O segundo número {} é maior que o primeiro número {}'. format(n2,n1))
elif n1==n2:
    print('Não existe numero maior os dois são iguais!')