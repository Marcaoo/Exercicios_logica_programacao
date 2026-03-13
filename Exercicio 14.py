# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 09:22:12 2026

@author: Marcão
"""

print("***INDICADOR DE NÚMEROS IGUAIS***")
n = int(input("Digite um valor a ser testado: "))   #solicita o número ao usuário

y = False

while n !=0:    #laço de repetição para verificar se os números são adjacentes
    a = n % 10
    n = n // 10
    b = n % 10
    if a == b:
        print(f"O número {a} , possui dois digitos adjacentes iguais. ")
        y = True
        
if y != True:
    print("Não a números adjacentes iguais no valor digitado")