#Exercício 4.2 - Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 km/h , exiba
# a mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80km/h
velocidade = int(input ("Digite a velocidade: "))
if velocidade <= 80:
    print ("Você está dentro do limite de velocidade!")
if velocidade > 80:
    multa = (velocidade - 80) * 5
    print("Você está sendo multado por passar acima de 80 KM/H, o valor da é: ", multa)
    
