# Cenário: Inscrição para modalidade de corrida

print("Olá! Seja bem-vindo(a) a página de inscrição.\nInforme seus dados para realizar a inscrição.")
nome = input("Informe seu nome completo:\n") # Guilherme Oliveira de Araújo
idade = input(f"Qual sua idade {nome}?\n") # 19 anos
cpf = input("Qual seu CPF?\n") # 168.593.226-67 
sexo = input("Qual seu sexo?\nMasculino\nFeminino\n") # Masculino
endereço = input("Qual seu endereço?\n") # Rua Shirley Martins Guimarães nº9, Jardim dos Comerciários
telefone = input("Qual seu telefone?\n") # 31 99935-5860
email = input("Qual seu e-mail?\n") # guilhermeoliveiradearaujo015@gmail.com

modalidade = int (input("Escolha a opção da modalidade:\n 1- 2km\n 2- 5km\n 3- 10km\n 4- meia-maratona\n 5- maratona\n"))
if modalidade == 1:
    print(f"{nome}, segue o horário da largada:\n - 10:00")
elif modalidade == 2:
    print(f"{nome}, segue o horário da largada:\n - 9:00")
elif modalidade == 3:
    print(f"{nome}, segue o horário da largada:\n - 8:00")
elif modalidade == 4:
   temp = int (input("Escolha uma das opções:\n1 - <1 hora\n 2 - >1 hora\n 3 - >2 horas\n"))
   if temp == 1 and sexo == "Feminino":
         print("Seu pelotão de elite larga às 6:10")
   elif temp == 1 and sexo == "Masculino":
         print("Seu pelotão de elite larga às 6:00")
   elif temp == 2 and sexo =="Feminino":
         print("Seu pelotão A larga às 6:40")
   elif temp == 2 and sexo =="Masculino":
         print("Seu pelotão A larga às 6:30")
   else: 
     print("Seu pelotão geral larga às 6:50")
elif modalidade == 5:
   temp = int(input("Escolha uma das opções:\n 1 - <1h\n 2 - >1h\n 3 - >2h\n"))
   if temp == 1 and sexo == "Feminino":
       print("Seu pelotão de elite larga às 5:10")
   elif temp == 1 and sexo == "Masculino":
       print("Seu pelotão de elite larga às 5:00")
   elif temp == 2 and sexo == "Feminino":
       print("Seu pelotão A larga às 5:40")
   elif temp == 2 and sexo == "Masculino":
       print("Seu pelotão A larga às 5:30")
   else:
       print("Seu pelotão geral larga às 5:50")

print(f"Confirme seus dados:\n nome: {nome}\n idade: {idade}\n CPF: {cpf}\n sexo: {sexo}\n endereço: {endereço}\n telefone: {telefone}\n e-mail: {email}")
conf = input("Seus dados estão corretos?")
if conf == "Não":
    print("Corrija seus Dados")
    nome = input("Informe seu nome completo:\n") # Guilherme Oliveira de Araújo
    idade = input(f"Qual sua idade {nome}?\n") # 19 anos
    cpf = input("Qual seu CPF?\n") # 168.593.226-67 
    sexo = input("Qual seu sexo?\nMasculino\nFeminino\n") # Masculino
    endereço = input("Qual seu endereço?\n") # Rua Shirley Martins Guimarães nº 9, Jardim dos Comerciários 
    telefone = input("Qual seu telefone?\n") # (31) 99935-5860
    email = input("Qual seu e-mail?\n") # guilhermeoliveiradearaujo015@gmail.com
else:
    print(input("Confirmar inscrição?"))                                                     