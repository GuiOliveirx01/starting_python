#Cenário: Inscrição para modalidade de corrida.
print("Olá! Seja bem-vindo(a) a página de inscrição.\nInforme seus dados para realizar a inscrição.")
nome = input("Informe seu nome completo:\n") #Guilherme Oliveira de Araújo
idade = input(f"Qual sua idade {nome}?\n") #19 anos
cpf = input("Qual seu CPF?\n") #168.593.226-67 
sexo = input("Qual seu sexo?\n") #Masculino
endereço = input("Qual seu endereço?\n") #Rua Shirley Martins Guimarães nº9, Jardim dos Comerciários. 
telefone = input("Qual seu telefone?\n") # 31 99935-5860
email = input("Qual seu e-mail?\n") # guilhermeoliveiradearaujo015@gmail.com
modalidade = input("Qual modalidade você vai escolher: 2km, 5km, 10km, meia-maratona, maratona?\n")
if modalidade == "2km":
    print(f"{nome}, segue o horário da largada:\n - 10:00")
elif modalidade == "5km":
    print(f"{nome}, segue o horário da largada:\n - 9:00")
elif modalidade == "10km":
    print(f"{nome}, segue o horário da largada:\n - 8:00")
elif modalidade == "meia-maratona":
    temp = input("Escolha uma das opções:\n 1-<1 hora\n 2->1 hora\n 3->2 horas\n")                


#print(f"\nConfirme seus dados:\n Nome: {nome}\n\n Idade: {idade}    CPF: {cpf}    Sexo: {sexo}\n\n Endereço: {endereço}\n\n Tel: {telefone}\n\n e-mail: {email}\n")
#input("Seus dados estão corretos?\n")


