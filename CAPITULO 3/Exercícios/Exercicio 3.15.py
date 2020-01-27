#Exercício: 3.15 - Escreva um programa para calcular a rdução do tempo de vida de um fumante.
#Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
#Considere que um fumante perde 10 minutos de vida a cada cigarro, e calcule
#quantos dias de vida um fumante perdera. Exiba o total em dias.

cigarros = int(input("Digite a quantidade de cigarros fumados por dia: "))
anos  = float (input("Digite quantos anos você fumou: "))
quant_cigarros = cigarros * 10   
quant_anos = (anos * 365)   
quant_vida = quant_cigarros * quant_anos
tempo_vida = quant_vida / (24 * 60)
print (tempo_vida)


#ou

#cigarros = int(input("Digite a quantidade de cigarros fumados por dia: "))
#anos  = int (input("Digite quantos anos você fumou: "))
#dias_perdidos = (( (cigarros * 10))* (anos * 365) /(24*60))
#print (dias_perdidos)
