#Verificar números primos
import math #Importando blibioteca math

num = int(input("Digite um número: ")) #Recebendo o número

def primo(n): #Criando função para realizar o cálculo
    if n < 2: #Verificando se é menor que 2, pois 1 e 2 são primos
        return False

    #Cálculo para saber se é número primo
    limite = int(math.sqrt(n)) + 1
    for i in range(2, limite):
        if n % i == 0:
            return False
    return True

if primo(num):
    print("Número primo")
else:
    print("Número não é primo")
