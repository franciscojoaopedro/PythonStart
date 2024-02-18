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
    

while True:
    print("O que deseja fazer?")
    print(informacao)
   
    comando=int(input())
    if comando ==0:
        for car in lista_de_carros:
            i=0
            print(lista_de_carros.index(),car)
        print("0 -CONTINUAR || 1- SAIR ")
        opcao=int(input())
        if opcao==1:
            time.sleep(3)
            os.system("clear")   
            print("Programa encerrado....")
            break
        elif opcao==0:continue
        else:
            print("Opção invalida, programa encerrado")
            break
    elif comando ==1:
        print(" Digite o codigo do carro  que pretendes alugar:")
        codigo_car=int(input())
        print(" Quantos dias pretendes ficar com carro:")
        dia_de_aluguer=int(input())

        car_test=lista_de_carros[codigo_car]
        lista_de_carros.remove(car_test)
        print("0 -CONTINUAR || 1- SAIR ")
        opcao=int(input())
        if opcao==1:
            time.sleep(3)
            os.system("clear")   
            print("Programa encerrado....")
            break
        elif opcao==0:continue
        else:
            print("Opção invalida, programa encerrado")
            break

