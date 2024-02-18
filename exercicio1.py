#criar um programa que recebe altura,peso e calcula o imc

import time

print("Calculadora IMC")
altura=float(input("\n Digite a sua altura:"))
peso=float(input("\n Digite a sua altura:"))

imc=peso/(altura**2)
mensagem="O imc calculado eh de {:.2f}".format(imc)
print(mensagem)