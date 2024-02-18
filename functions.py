def diga_ola(name:str):
    a:int=1
    print('Olá,{}'.format(name))



def gerador_de_numero_impares(number:int):
    if(type(number)!=int):
        print("O argumento passado na função precisa ser um número!")
    else:
      return [i for i in range(number) if i%2==1]


gerador_de_numero_impares(25).pop()