#Exercício 3.12 - Faça um programa que calcule o tempo de uma viagem de carro.
#Pergunte a distancia percorrer e a velocidade media esperada para viagem.

distancia = int(input("Digite a distancia ser percorrida: "))
velocidade = int (input("Digite a velocidade a ser percorrida km: "))
resultado = distancia/velocidade
print("Chegara a seu destino:", resultado, "horas")
