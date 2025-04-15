#Imprimir valores entre x e y que tem resto de divisão por 5 igual a 2 ou 3

x = int(input('Número 1: ')) #Recbe x
y = int(input('Número 2: ')) #Recebe y

for c in range(x, y): #Loop entre o intervalo de x e y
    if c % 5 == 2 or c % 5 == 3: #Verifica os números de resto 2 e 3 na divisão por 5
        print(c) #Imprime esses números