#Exercício 3.9 -  Escreva um program que leia a quantidade de dias,
#horas, minutos e segundos dos usuário. Calcule o total em segundos.

dias = int (input ("Digite a quantidade de dias:  "))
horas = int(input("Digite a quantidade de horas:  "))
minutos = int (input ("Digite a quantidade de minutos:  "))
segundos = int (input ("Digite a quantidade de segundos: "))

calculo_dias = dias * 24 * 60 * 60
calculo_horas = horas * 60 * 60
calculo_minutos = minutos * 60
resultado =  calculo_dias + calculo_horas + calculo_minutos + segundos
print("O resultado final em segundos e:",resultado)
 
#print(calculo_dias)
#print(calculo_horas)
#print(calculo_minutos)
#print(segundos)

#dias = int (input("Digite a quantidade de dias: "))
#resultado = dias *24*60*60
#print("resultado em segundo é:", resultado)
