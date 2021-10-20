#quando for importada a bilblioteca, quando colocar o ponto aparece todas as funcionalidades 
#da biblioteca, ex: import math.. e na hora de usar math.(aparecera as funções disponiveis para uso)
#importanto tudo
import math
num=int(input('Digite um numero :'))
raiz= math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num,raiz))

#importando só o que vai usar
#from math import sqrt, floor  etc...
#print('A raiz de {} é igual a {:.2f}'.format(num, floor(raiz))) ja faz o arredondamento pra baixo



