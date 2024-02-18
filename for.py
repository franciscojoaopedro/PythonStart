
lista_de_numero=list(range(0,10+1))

for valor_da_lista in lista_de_numero:
     numero_par=valor_da_lista%2
     if(numero_par==0):
         print("{} eh um numero par".format(valor_da_lista))
     else:
        print("{} eh um numero impar".format(valor_da_lista))
     
    
    