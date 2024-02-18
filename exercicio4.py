

print("Bem vindo a loja de Tinta")
print("Informa a áera que você deseja pintar:")
area=float(input())
volume_necessario=area/3
latas=int(volume_necessario/18)
custo =latas*80


print("você precisará de {} latas e elas custarão {} kwanzas.".format(latas,custo))