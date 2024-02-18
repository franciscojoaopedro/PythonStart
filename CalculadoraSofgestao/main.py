import os

print("========= Calculadora ==========")
print(" 0 : Soma")
print(" 1 : Subtração")
print(" 2 : Multiplicação")
print(" 3 : Divisão")
print(" 4 : Exponenciação")

opcao=True
usar=""
while opcao:
    os.system("clear")
    print("Escolha a operação que deseja realizar")
    operacao=int(input())
     # Operação soma
    if operacao ==0:
        print("O Operação '+' soma escolhida")
        print("=========== Operação Soma ===========")
        primeiro_valor_da_soma=float(input("Digite o primeiro valor da soma:"))
        segundo_valor_da_soma=float(input("Digite o segundo valor da soma:"))
        soma=primeiro_valor_da_soma + segundo_valor_da_soma
        print("A soma entre '{}' '+' '{}' eh igual: {:.2f} "
              .format(primeiro_valor_da_soma,segundo_valor_da_soma,soma))
        print("Para continuar a usar a Calculadora digite: '1' para utilizar, '0' para cancelar e sair. ")
        usar=int(input())
        if usar ==1: 
            opcao=True
            continue
        else: 
            opcao:False
            print("Saindo...........")
            print("Saindo.....")
            print("Saindo...")
            break
    # Operação subtração
    elif operacao ==1:
        print("O Operação '-' subtração escolhida")
        print("=========== Operação Soma ===========")
        primeiro_valor_da_subtracao=float(input("Digite o primeiro valor:"))
        segundo_valor_da_subtracao=float(input("Digite o segundo valor:"))
        subtracao=primeiro_valor_da_subtracao - segundo_valor_da_subtracao
        print("A diferensa entre '{}' '-' '{}' eh igual: {:.2f} "
              .format(primeiro_valor_da_subtracao,segundo_valor_da_subtracao,subtracao))
        print("Para continuar a usar a Calculadora digite: '1' para utilizar, '0' para cancelar e sair. ")
        usar=int(input())
        if usar ==1: 
            opcao=True
            continue
        else: 
            opcao:False
            print("Saindo...........")
            print("Saindo.....")
            print("Saindo...")
            break
    # Operação multiplicacao
    elif operacao ==2:
        print("O Operação 'x' multiplicação escolhida")
        print("=========== Operação multiplicação ===========")
        primeiro_valor_da_multiplicacao=float(input("Digite o primeiro valor:"))
        segundo_valor_da_multiplicacao=float(input("Digite o segundo valor:"))
        multiplicacao=primeiro_valor_da_multiplicacao * segundo_valor_da_multiplicacao
        print("O produto entre '{}' 'x' '{}' eh igual: {:.2f} "
              .format(primeiro_valor_da_multiplicacao,segundo_valor_da_multiplicacao,multiplicacao))
        print("Para continuar a usar a Calculadora digite: '1' para utilizar, '0' para cancelar e sair. ")
        usar=int(input())
        if usar ==1: 
            opcao=True
            continue
        else: 
            opcao:False
            print("Saindo...........")
            print("Saindo.....")
            print("Saindo...")
            break
    elif operacao ==3:
        print("O Operação '/' divisão escolhida")
        print("=========== Operação divisão ===========")
        primeiro_valor_da_divisao=float(input("Digite o primeiro valor:"))
        segundo_valor_da_divisao=float(input("Digite o segundo valor:"))
        divisao=primeiro_valor_da_divisao / segundo_valor_da_divisao
        print("O Resutado entre '{}' '/' '{}' eh igual: {:.2f} "
              .format(primeiro_valor_da_divisao,segundo_valor_da_divisao,divisao))
        print("Para continuar a usar a Calculadora digite: '1' para utilizar, '0' para cancelar e sair. ")
        usar=int(input())
        if usar ==1: 
            opcao=True
            continue
        else: 
            opcao:False
            print("Saindo...........")
            print("Saindo.....")
            print("Saindo...")
            break
    elif operacao ==4:
        print("O Operação 'x' Exponenciação escolhida")
        print("=========== Operação Exponencial ===========")
        valor_de_base=float(input("Digite o valor da base:"))
        valor_do_potencia=float(input("Digite o valor da potencia:"))
        exponencial=valor_de_base**valor_do_potencia
        print("A potencia de '{}' '**' '{}' eh igual: {:.2f} "
              .format(valor_de_base,valor_do_potencia,exponencial))
        print("Para continuar a usar a Calculadora digite: '1' para utilizar, '0' para cancelar e sair. ")
        usar=int(input())
        if usar ==1: 
            opcao=True
            continue
        else: 
            opcao:False
            print("Saindo...........")
            print("Saindo.....")
            print("Saindo...")
            break