#Verificar ocorrência de caracter na palavra

palavra = input("Digite uma palavra: ") #Recebe a palavra
char = input("Digite um caractere: ") #Recebe o caracter

print(palavra.find(char)) #Encontra o caracter na palavra. Se ele n for encontrado, automaticamente já reporta -1