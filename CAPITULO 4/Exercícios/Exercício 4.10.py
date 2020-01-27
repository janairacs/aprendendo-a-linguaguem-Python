#Exercício  4.10 - Escreva um programa que calcule o preço a pagar pelo fornecimento
# de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação
#R: para residências, I para indústrias e C para comércios. Calcule o preço a pagar
#pagar de acordo com a tabela a seguir.
'''
------------------------------------
Residencial | ate 500     | RS0,40 |
            |acima de 500 | RS0,65 |
-----------------------------------|
Comercial   | ate 1000    | RS0,55 |
            |acima de 1000| RS0,60 |
-----------------------------------|
Industrial  | ate 5000    | RS0,55 |
            |acima de 5000| RS0,60 |
------------------------------------

'''

fornecimento =  float (input ("Digite a quantidade de kWh consumida: "))
tipo_insta   = int (input("Digite o tipo de instalação 1 = Residencial , 2 = Industrias , 3 = Comercios: "))

if tipo_insta == 1 and fornecimento <= 500:
    resultado  = (fornecimento * 0.40)
else:
    resultado = (fornecimento * 0.65)

    if tipo_insta == 2 and fornecimento <= 1000:
        resultado  = (fornecimento * 0.55)
    else:
        resultado = (fornecimento * 0.60)
        
        if tipo_insta == 3 and fornecimento <= 5000:
            resultado  = (fornecimento * 0.55)
        else:
            resultado = (fornecimento * 0.60)
        
print(resultado)
 
