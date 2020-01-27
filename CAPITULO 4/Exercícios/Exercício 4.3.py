#Exercício 4.3 -  Escreva um programa que leia três números e que imprima o maior e o menor.
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor :"))
maior = a
if b > a and  b > c :
    maior = b
if c > a and c > b:
    maior = c
menor = a
if b < c and  b < a :
    menor = b
if c < b and c < a:
    menor = c
print("O menor número digitado foi: ", menor)
print("O maior numero digita foi: ", maior)
  



    
