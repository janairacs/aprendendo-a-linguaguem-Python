#Exercício 3.11 - Escreva um programa que solicite o preço de uma mercadoria e o percentual de desconto.
#Exiba o valor do desconto e o preço a pagar

mercadoria = float (input ("Digite o preço da mercadoria  "))
porcentagem = int (input ("Digite a porcentagem de desconto da mercadoria: "))
desconto = mercadoria * porcentagem /100
desconto_mercadoria =  mercadoria - desconto  
print ("O desconto da mercadoria : ",desconto, "E o novo preço é: ",desconto_mercadoria)
