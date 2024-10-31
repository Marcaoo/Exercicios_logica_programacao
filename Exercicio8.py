#Exercicio 8

#Inicio
print('Programa para cálculo de IMC\n')

#Entrada de dados
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso/altura * altura

#Condicional

if imc < 18.5:
    print('Abaixo do peso')
elif imc <=18.5 or imc < 24.9:
    print('Peso Normal')
elif imc <= 25  or imc <29.9:
    print('Sobrepeso')
elif imc > 29.9:
    print('Obesidade')