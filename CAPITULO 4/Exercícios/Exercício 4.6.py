#Exercício 4.6 -Escreva um programa que pergunte a distancia que um passageiro deseja
#percorrer em km. Calcule o preço da passagem, cobrando RS0,60 por km para viagens
# de ate 200km, e R$0,45 para viagens mais  longas.

km = int (input("Digite o valor do km a ser percorrido :"))
if km <=200:
    valor = (km * 0.60)
else:     
    valor = (km * 0.45)
print ("O valor da passagem é : ", valor)
 
