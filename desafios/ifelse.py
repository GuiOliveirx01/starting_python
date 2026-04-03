'''n1 = 13
n2 = 20
result = n1 + n2
if result%2 == 0: 
    print(f"O resultado da soma de {n1} + {n2} é {result} e ele é par")
else:
    print(f"O resultado da soma de {n1} + {n2} é {result} e ele é ímpar")
'''    
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
if (n1 + n2)%2 == 0: 
    print("Deu certo")
    #print(f"O resultado da soma de {n1} + {n2} é  e ele é par")
else:
    #print(f"O resultado da soma de {n1} + {n2} é {result} e ele é ímpar")
    print("Deu errado")