""" Crie um programa que leia o nome completo de uma pessoa e mostre:
1- o nome com todas as letras maiusculas
2- o nome com todas as letras minusculas
3-quantas letras ao todo sem considear espaços
4-quantas letras tem o primeiro nome 
 """
n=str(input('Qual o seu nome Completo ?'))
m=n.upper() # maiusculo
a=n.lower() # minusculo
b=n.replace(" ", "") # remove espaços da frase
l=len(b) # tamanho da frase sem espaço
p1=n.split() #separa cada nome em lista
p2=p1[0] #captura o primeirpo bloco da lista
print('Nome maiusculo : {}'.format(m))
print('Nome minusculo : {}'.format(a))
#print(b)
print('O nome sem espaços tem o tamanho de {}'.format(l))
print('O primeiro nome é {} e tem {} letras'.format(p2,len(p2)))
