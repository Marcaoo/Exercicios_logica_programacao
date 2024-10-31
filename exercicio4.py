#Exercicio 4 O programa deve solicitar um número e verificar se ele está dentro do intervalo de 1 a 100

#Entrada de dados
numero = int(input("Digite um número: "))

#Condicional
if (numero >=1) and (numero <= 100):
    print('o número digitado está no intervalo de 1 a 100')
elif numero < 1:
    print('o número digitado é menor que 1')
else:
    print('o número digitado é maior que 100')

     