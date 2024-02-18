print("Calculadora de salário!")
print("Informe sua remuneração por horas")
valor_por_hora=float(input())

print("Informe quantas horas trabalhou por mês")
horas_tralhadas=float(input())

salario=valor_por_hora*horas_tralhadas

imposto_de_renda=salario*0.11
inss=(salario-imposto_de_renda)*0.08
sindicato=(salario-imposto_de_renda-inss)*0.05
salario_liquido=salario-imposto_de_renda-inss-sindicato

print("======= CALCULADORA DE SALÁRIO =======")
print("Salário bruto: {:.2f}".format(salario))
print("Valor pago de imposto de renda: {:.2f}".format(imposto_de_renda))
print("Salário pago de insss: {:.2f}".format(inss))
print("Salário pado ao sindicato: {:.2f}".format(sindicato))
print("Salário líquido: {:.2f}".format(salario_liquido))