import pdb

x=[1,2,3]
y=2
z=3

try:
    x+y
    x=1
    y=2
except Exception as error :
    print("Erro {}".format(error))
finally:
    print("Olá!")

print("Continuação")