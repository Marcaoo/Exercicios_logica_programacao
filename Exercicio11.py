# Crie uma função recursiva chamada fatorial que calcule o fatorial de um número

def fatorial(n): #Define a função
    if n == 0:
        return 1 
    else:
        return n * fatorial(n-1)

a = int(input('Digite um número: ')) #Entrada de Variável
resultado = fatorial(a)

print(f'O fatorial de {a} é: {resultado}') #Resultado da operação