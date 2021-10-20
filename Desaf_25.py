##crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome
nom=str(input('Digite o seu nome inteiro :'))#.strip #remove os espaços do inicio e o fim

t1= nom.upper()
t2= "SILVA" in t1
print('O nome possui a palavra Silva?  {}'.format(t2))

#nome=str(input('Qual o seu nome completo?')).strip()
#print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))