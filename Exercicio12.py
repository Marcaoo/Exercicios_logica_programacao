#Crie uma função chamada eh_primo que verifique se um número é primo.

def eh_primo(numero):   #Define a função
    if numero <=1:
        return False
    for i in range(2,int(numero**0.5)+1):
        if numero %i == 0:
            return False
        return True

n = int(input('Digite um número'))
print(eh_primo(n))
