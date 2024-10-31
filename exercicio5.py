#Exercicio 5  Oprograma deve verificar se a idade de uma pessoa é suficiente para dirigir (18 anos ou mais).

#Inicio
print('Programa para verificar se você possui idade para dirigir\n')

#Entrada de dados

idade = int(input('Digite sua idade: '))

#Condicional
if idade >= 18:
    print ('Você ja pode dirigir e participar do elenco de Veloses e Furiosos!')
else:
    print ('Você não possui idade para dirigir, volte para escola <3')