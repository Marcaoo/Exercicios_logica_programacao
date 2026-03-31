# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 09:15:10 2026

@author: Marcão
"""

import math

def delta(a,b,c):       #função que calcula o delta
    return b**2 - 4 * a * c

def main():         #função principal do programa
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    imprime_raizes(a, b, c)
    
def imprime_raizes(a,b,c):      #define as raizes
    d = delta(a,b,c)
    if d == 0:
        raiz1 = (-b + math.sqrt(d) / (2*a))
        print(f"A unica raiz é: {raiz1}")
    else:
        if d < 0:
            print("Esta equação não possui raízes reais")
        else:
            raiz1 = (-b + math.sqrt(d) / (2*a))
            raiz2 = (-b - math.sqrt(d) / (2*a))
            print(f"A primeira raiz é: {raiz1}")
            print(f"A segunda raiz é: {raiz2}")

main()