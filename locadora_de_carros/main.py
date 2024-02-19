


import time
import os
print("")
print("================== rent car ngunga dev ==================")
print("")
informacao={
    "0":"Mostrar portifólio ",
    "1":"Alugar um carro",
    "2":"Devolver um carro",
}
lista_de_carros=[
        ("Chevrolet Tracker", 120),
        ("Chevrolet Onix",90),
        ("Chevrolet Spin",120),
        ("Hyundai hb20",85),
        ("Hyundai Tucson",120),
        ("Fiat Uno",120),
        ("Fiat Mobi",70),
        ("Fiat Pulse", 130)
    ]
carros_alugados=[]
    

def mostrarCarros(carros):
    for i  , car in enumerate(carros):
        print("[{}] {} - {} kz/dia".format(i,car[0],car[1]))



        
    

while True:
   
        

    os.system("clear")
    print("=====================================")
    print("Bem vindo à locadora de carros!")
    print("=====================================")
    print("O que você deseja fazer?")
    print(informacao)
    opcao_de_entrada=int(input())

    os.system("clear")
    if opcao_de_entrada==0:
        mostrarCarros(lista_de_carros);
    elif opcao_de_entrada==1:
        mostrarCarros(lista_de_carros);
        print("Escolha o código do carro:")
        codigo_do_car=int(input())
        print("Por quantos dias você deseja alugar este carro?")
        dias=int(input());
        os.system("clear")

        print("Você escolheu {} por dias".format(lista_de_carros[codigo_do_car][0],dias))
        print("O aluguel totalizaria {} kz .Deseja alugar?".format(dias*lista_de_carros[codigo_do_car][1]))
        
        print("0-sim || 1-não")
        confirmacao=int(input())
        if confirmacao==0:
            print("Parabéns você alugou o {} por {} dias".format(lista_de_carros[codigo_do_car][0],dias))
            carros_alugados.append(lista_de_carros.pop(codigo_do_car))



    #carros alugados
    elif opcao_de_entrada==2:
        if len(carros_alugados)==0:
            print("Não há carros alugados!")
        else:
            print("Veja a lista de carros alugado. Qual você desejo devolver?")
            mostrarCarros(lista_de_carros)
            print("")
            print("Escolha o código do carro que deseja devolver:")
            codigo_do_car=int(input())
            lista_de_carros.append(carros_alugados.pop(codigo_do_car))

    else:
        print("Opção invalida,encerrando o programa...")
        time.sleep(3)
        print("Programa encerrado.")
        break
    print("===========")
    print("DIGITE [1] PARA SAIR || DIGITE [0] PARA CONTINUAR")
    comando_de_entrada=int(input())
    if comando_de_entrada==1:
        time.sleep(3)
        os.system("clear")   
        print("Programa encerrado....")
        break
    elif comando_de_entrada ==0:
        continue
    else:
        print("Opção invalida,encerrando o programa...")
        time.sleep(3)
        os.system("clear")
        print("Programa encerrado.")
        break
