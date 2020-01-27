#Exercício 4.4 - Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento.
# Para salário superiores a R$1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais de 15%.

salario =  float (input("Digite o valor do salário: "))
base = salario
if base > 1250:
    valor = (base * 10/100)
    print ("O valor do salario com 10%:", valor )
if base <= 1250:
    valor_2 = (base * 15/100)
    print("O valor do salario com 15%: ", valor_2)
