import os

operacao={
    "+":"Soma",
    "-":"Subtração",
    "*":"Multiplicação",
    "/":"Divisao",
    "^":"Exponencial"
}

while True:
    os.system("clear")
    i=0
    for op ,name in operacao.items():
        print(i,":",name)
        i+=1
    print("")
    print("Escolha a operação que deseja realizar:")
    op=int(input())
    op_string=list(operacao.keys())[op]
    
    print("")
    print("{} escolhida.".format(op_string))
    print("Qual o primeiro valor?:")
    valor_1=float(input())
    print("Qual o segundo valor?:")
    valor_2=float(input())

    if op==0:
        resultado=valor_1+valor_2
        print()
    elif op==1:
        resultado=valor_1-valor_2
        print()
    elif op==2:
        resultado=valor_1*valor_2
        print()
    elif op==3:
        resultado=valor_1-valor_2
        print()
    elif op==4:
        resultado=valor_1**valor_2
        print()
    print("=========== RESULTADO ============")
    print("{} {} {}={}".format(valor_1,op_string,valor_2,resultado))

    print("Deseja fazer mais uma operacao? (Digite 1 para sair)")
    comando=int(input())
    if  comando ==1:
        break
    


    
