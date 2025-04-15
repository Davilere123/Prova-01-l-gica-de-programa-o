n = int(input("Informe a quantidade de números: ")) #Recebe a quantidade de números que serão digitados
numeros = [] #Lista para receber os números

print("Digite os números:")
for c in range(n): #Loop da quantidade de números
    numero = int(input(f"Número {c + 1}: ")) #Recebe o número correspondente
    numeros.append(numero) #Adiciona o número à lista

print("Números na ordem inversa:")
for c in reversed(numeros): #Loop que imprime os números na ordem reversa
    print(c)

numeros_decrescente = reversed(sorted(numeros)) #Variável que recebe a lista de números crescente ao contrário, virando decrescente
print("Números em ordem decrescente:")
for c in numeros_decrescente: #Imprimindo esses números
    print(c)
