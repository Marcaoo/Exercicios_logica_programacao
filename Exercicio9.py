matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

soma_total = sum(sum(linha) for linha in matriz)

print(f'A soma de todos os elementos da matriz é: {soma_total}')