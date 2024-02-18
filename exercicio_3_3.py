print("Informe o seu nome:")
nome:str=input()


for letra in range(len(nome)+1):
    print(nome[:letra])