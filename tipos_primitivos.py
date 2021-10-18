#type mostra o tipo primitivo, numero não declarado com int é string
n1=input('Digite um valor: ')
print(type(n1))
# agora vai encontrar como intiro
n1=int(input('Digite um valor: '))
print(type(n1))
#somando
n1=int(input("Digite um valor: "))
n2=int(input('Digite outro: '))
s= n1+n2
print('A soma é:' , s)
#concatenando, tirou o int
n1=input("Digite um valor: ")
n2=input('Digite outro: ')
s= n1+n2
print('A soma é:' , s)
# soma entre 6 e 2
n1=int(input("Digite um valor: "))
n2=int(input('Digite outro: '))
s= n1+n2
#print('A soma entre :' , n1, 'e ',n2, 'vale : ', s)
print('A soma entre : {} e {} vale {}'.format(n1,n2,s))
