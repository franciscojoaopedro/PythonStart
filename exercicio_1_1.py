#media do aluno


print("Calcular media do aluno")

primeira_nota=3;
segunda_nota=8;

media=(primeira_nota+segunda_nota)/2

messagem=["Aprovado","Reprovado","Aprovado com Distinção"]

if media>=10:
    print("{} com média {:.2f}".format(messagem[2],media))
elif media >=7:
    print("{} com média {:.2f}".format(messagem[0],media))
elif media<7:
        print("{} com média {:.2f}".format(messagem[1],media))