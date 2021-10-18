#função sem parametro, pode servir para desviar o código e executar algo
#a função leva em consideração o denteamento ou seja usa o tab, no final precisa pelo menos uma linha em branco
def traco():
    print("-------------")

#função com 2 parametros, retorna um resultado de acordo com os parametros enviados
def soma(n1,n2):
    s= n1+n2
    print(s)

traco()
print("ola Eric")
traco()
soma(10,20)
traco()
print("Fim")
traco()