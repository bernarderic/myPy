# fazer um programa que leia um nimero inteiro e mostre o seu sucessor e antecessor
# dica format (n, (n-1),(n+1)) usando apenas uma variavel economiza memória
n = int(input('Digite um numero inteiro :'))
a = n + 1
b = n - 1
print('O numero digitado foi {}, o seu sucessor é {}, e seu antecessor é {}'.format(n, a, b))
