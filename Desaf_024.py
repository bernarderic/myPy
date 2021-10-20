""" crie um progrma que leia o nome de uma cidade e diga se ela 
começa ou não com o nome "santo" """
cid=str(input('Digite o nome da cidade: '))
nom=cid.upper()
teste= nom.split()
teste2='SANTO' in teste[0]
#'up=nom.upper()
print('A cidade começa com a palavra Santo? {}'.format(teste2))