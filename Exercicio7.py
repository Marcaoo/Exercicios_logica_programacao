#Exercicio 7 Desenvolva um programa que solicita um ano para o usuário e verifique se ele é bissexto ou não.

#inicio
print('Programa para verificar se o ano é bissexto')

#Entrada de dados
ano = int(input('Digite um ano: '))

#Condicional

if (ano % 4) == 0 or (ano % 400) == 0:
    print('Ano bissexto')
else:
    print('Não é ano bissexto')