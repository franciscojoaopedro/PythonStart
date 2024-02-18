#um programa q pergunta o nome complento e cumprimente o mesmo pelo primeiro nome.
import time

print("Nome completo")
nome_completo=str(input("Digite o nome completo: "))


messagem="Olá {} tudo bem contigo?".format(nome_completo.split()[0])
print(messagem)