#Exercício 4.9 - Escreva um programa para aprovar o empréstimo bancário para compra
#de uma casa. O programa deve perguntar o valor da casa a comprar, o salário e
# a quantidade de anos a pagar. O valor da prestação mensal não pode ser superior a
#30% do salário. Calcule o valor da prestação como sendo o valor da casa a comprar
#divido pelo número de meses a pagar.

valor_casa = float (input("Digite o valor da casa que deseja comprar: "))
salario  = float (input ("Digite o salario: "))
qtd_anos = int (input("Digite a quantidade de anos para pagar: "))

valor_prestacao =  valor_casa / (qtd_anos * 12)
if valor_prestacao < (salario *0.30):
    print("O seu empréstimo foi aprovado")
else:
    print(("O seu empréstimo foi recusado"))
    
     
