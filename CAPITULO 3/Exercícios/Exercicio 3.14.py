#Exercício 3.14 - Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado,
#pelo usuário, assim com a quantidade de dias pelos quais o carro foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia, e R$ 0.15 por km
km = int (input("Digite a quantidade de km :"))
dia = int(input("Digite a quantidade de dia(s) :" ))
resultado = (km *0.15) + (dia *60)
print ("O valor é: " ,resultado)

