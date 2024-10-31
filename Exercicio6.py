#Exercicio 6  Desenvolva um programa que verifica o valor da compra e aplica um desconto de 10% se o valor for maior que 100.

#Entrada de dados
valor_compra = float(input('Digite o valor da compra: '))

#Condicional
if valor_compra > 100:
    valor_final = valor_compra * 0.9
    print(f'Desconto aplicado" O valor final é {valor_final}.')
else:
    print(f'Sem desconto. O valor a pagar é {valor_compra}.')