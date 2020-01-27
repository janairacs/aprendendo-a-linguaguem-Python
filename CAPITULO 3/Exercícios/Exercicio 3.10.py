#Exercício 3.10 - Faça um programa que solicite o preço de um mercadori e o percentual
# de desconto. Exiba o valor do desconto e o preço a pagar.

salario = float (input ("Digite o seu salário:   "))
porcentagem = int (input ("Digite a porcentagem de salario: "))
aumento = salario * porcentagem /100
novo_salario =  aumento+salario
print ("O aumento de salario e: ",aumento, "E o novo salario é: ",novo_salario)
