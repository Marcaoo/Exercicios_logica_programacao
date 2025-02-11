#Crie uma função chamada maior_numero que receba dois números como parâmetros e retorne o maior deles.

def maior_numero(): #Define a função
    n1 = int(input('Digite o número 1: ')) #Entrada de variável
    n2 = int(input('Digite o número 2: ')) #Entrada de variável
    
    if n1 > n2:     #Condicional
        return n1
    elif n1 < n2:
        return n2
    else:
        print('Iguais')

print(maior_numero())   #Mostra o resultado