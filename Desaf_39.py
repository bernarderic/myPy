'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com 
a sua idade:
- se ele ainda vai se alistar ao serviço militar
-se é a hora de se alistar
-se ja passou o tempo de se alistar
o programa também deverá mostrar o tempo que falta ou que ja passou o prazo '''
from datetime import date
atual=date.today().year
nasc=int(input('Digite o seu ano de nascimento: '))
idade= atual-nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc,idade,atual))


if idade == 18:
    print('voce tem que alistar imediatamente!')
elif idade <18:
    saldo=18-idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    ano=atual+saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade >18:
    saldo =idade-18
    print('voce ja deveria ter se alistado a {} anos'.format(saldo))
    ano=atual-saldo
    print('Seu alistamento foi em {}'.format(ano))