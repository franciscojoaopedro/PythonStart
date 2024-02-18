

#idade:int,salario:float,sexo:str,estado_civil:str
def validacao_de_dados(nome:str,idade:int,salario:float,sexo:str,estado_civil:str):  
    while True:
        if len(nome)<=3:
            print("O nome deve conter mais de três [3] caratecter")
            print("Informe o nome:")
            nome=input()
            nome
        elif salario<=0:
            print("O salario dever ser maior que zero.")
            print("Infome o salário")
            salario=input()
        elif idade<=0:
            print("A idade tem que ser maior que zero.")
            print("Infome a idade")
            idade=input()
        elif sexo not in ["m","f"]:
            print("O sexo deve ser 'm' ou 'f'.")
            print("Infome o sexo")
            idade=input()
        elif estado_civil not in ["s","c"]:
            print("O estado civi deve ser 's' ou 'c'.")
            print("Infome o estado civil!")
            estado_civil=input()
  



validacao_de_dados("Francisco",21,100,"m","s")

