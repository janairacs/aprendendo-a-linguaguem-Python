#Exercício 4.1 - Analise o programa 4.1 Responda o que acontece se o
#primeiro e o segundo valores forem iguais explique.

a = int (input("Primiro valor: "))
b = int (input("Segundo valor: "))
if a > b:
    print("O primeiro valor e maior!")
if b > a:
    print("O segundo valor e maior!")
    
# O exercício acaba pulando as condições pois não encontra.
# A  solução apresentada:

if a == b or b == a:
    print("Os valores são iguais!")
 
