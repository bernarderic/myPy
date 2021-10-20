""" crie um programa que leia a frase digitada  pelo teclado e mostre :
1- qtas vezes aparece a letra  'a'
2-em que posição ela aparece a primeira vez
3-em que posição ela aparece a ultima vez
 """
fra=str(input('Digite uma frase :')).upper().strip()   
print('A letra  A  aparece {} vezes na frase'.format(fra.count('A')))
print('A primeira letra A apareceu na posição {}'.format(fra.find('A')+1))
print('A última letra A apareceu na posição {}'.format(fra.rfind('A')+1))
