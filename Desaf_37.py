"""escreva um programa que leia um numero inteiro qualquer e peça para o usuário 
escolher qual será a base de conversão:
1- para binário
2- para octal
3- para hexadecimal"""
num=int(input('Digite um numero inteiro: '))
print(''' Escolha uma das bases para conversão:
[1] converter para Binário
[2] converter para OCTAL
[3] converter para Hexadecimal ''')
opção=int(input('Sua opção: '))

if opção == 1 :
    print('{} convertido para Binário é igual a {}'.format(num, bin(num)[2:]))
elif opção ==2:
    print('{} convertido para OCTAL é igual  a {}'.format(num, oct(num)[2:]))
elif opção ==3:
    print('{} convertido para Hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida!')
