#Calcular média baseado na quantidade de alunos e verificar os que estão 10% acima e abaixo dela
qal = int(input('Digite a quantidade de alunos: ')) #A quantidade de alunos
notas = [] #Lista que vai receber as notas

for c in range(qal): #Loop para poder receber a quantidade de notas equivalente a de alunos
    nota = float(input('Digite a nota do aluno {}: '.format(c + 1))) #Pedindo a nota correspondente ao aluno
    notas.append(nota) #Adicionando o valor à lista

media = sum(notas) / qal #Calculando a média ao somar as notas dentro da lista e dividir pela qtd de alunos
limite_superior = media * 1.1 #Definindo o limite acima de 10%
limite_inferior = media * 0.9 #Definindo os limite abaixo de 10%

#socorro ;-;

acima_10_media = [nota for nota in notas if nota > limite_superior] #Verificando notas acima de 10%
abaixo_10_media = [nota for nota in notas if nota < limite_inferior] #Verificando notas abaixo de 10%

print(f'Média das notas: {media:.2f}') #Imprimindo a média formatada em 2 casas decimais
print(f'Notas 10% acima da média: {acima_10_media}') #Imprimindo as notas acima de 10%
print(f'Notas 10% abaixo da média: {abaixo_10_media}') #Imprimindo as notas abaixo de 10%
