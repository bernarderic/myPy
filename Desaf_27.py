""" Faça um progrma que leia o nome completo de uma pessoa, mostrando em seguida 
o primeiro e op ultimo nome separadamente. """
nom=(str(input('Digite o seu nome completo :'))).strip()
t1=nom.split()
print('O primeiro nome é {}  e o último nome é {}'. format(t1[0],t1[len(t1)-1]))