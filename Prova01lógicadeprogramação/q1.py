#Faça um programa que leia 3 números inteiros e os imprima em ordem crescente

num = ['','',''] #Lista para receber os 3 números

#Recebendo os números
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite mais um número: "))

#Colocando esses números em variáveis
num[0] = n1
num[1] = n2
num[2] = n3

#Colocando em ordem crescente e imprimindo
list.sort(num)
print(num)