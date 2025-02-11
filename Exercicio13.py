#Crie um programa que calcule a áreas de figuras geométricas(Cículo,triângulo,retângulo)

import os
import math
import time

def clear(): #função para limpar as linhas.
    time.sleep(3)
    os.system('cls')

def calcula_area_circulo(): #função para calcular a área do círculo.
    raio = float(input('Digite o valor do raio: '))
    a = math.pi * raio**2
    
    return a

def calcula_area_triangulo(): #função para calcular a área do triângulo
    b = float(input('Digite o valor da base: '))
    h = float(input('Digite o valor da altura: '))
    
    a = (b * h)/2
    
    return a

def calcula_area_retangulo(): #função para calcular a área do retângulo
    b = float(input('Digite o valor da base: '))
    h = float(input('Digite o valor da altura: '))
    
    a = b * h
    
    return a

def main(): #função principal do programa
    while True:
        
        print(38* '*')
        print('Cálculo de área de figuras geométricas')
        print(38* '*')
        print('\n1-Área círculo')
        print('2-Área triângulo')
        print('3-Área retângulo')
        print('4-Sair')
    
        escolha = input('Digite a opção que deseja: ')
    
        if escolha == '1':
            print(f'A área do círculo é: {calcula_area_circulo():.2f}')
            clear()
        elif escolha == '2':
            print(f'A área do triângulo é: {calcula_area_triangulo():.2f}')
            clear()
        elif escolha == '3':
            print(f'A área do retângulo é: {calcula_area_retangulo():.2f}')
            clear()
        elif escolha == '4':
            print('Encerrando o programa...')
            clear()
            break
        else:
            print('Opção inválida!')
            clear()
        
if __name__ == '__main__':
    main()    