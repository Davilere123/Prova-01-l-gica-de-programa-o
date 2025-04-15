#Mostrar nome do fulano de tal

print("Digite seu nome (pode conter até 120 caracteres):") #Texto para iniciar
nome = input() #Recebendo o nome

while True: #Loop para repetir o código caso passe de 120 caracteres
    if len(nome) < 119: #Verificando se passou de 120
        print('Seja muito bem-vindo {}!'.format(nome)) #A mensagem
        break #Quebrando o loop e encerrando
    else:
        print('Opa! Seu nome é longo demais. Por favor tente novamente.')
        print('Digite um nome com menos de 120 caracteres:')
        nome = input() #Pedindo que o usuário escreva novamente
        continue #Voltando do começo