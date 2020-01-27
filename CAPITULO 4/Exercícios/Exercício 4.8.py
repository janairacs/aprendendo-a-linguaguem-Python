#Exercício 4.8 - Escreva um programa que leia dois números
#e que pergunte qual operação você deseja realizar. Você dever
#poder calcular soma(+), subtração (-), multiplicação(*),
# e divisão (/). Exiba o resultado da operação solicitada.

# estrutura aninhadas
tela = print ('''Este programa é uma calculadora.
Temos as seguintes operações:
opção 1 = soma (+)
opção 2 = subtração (-)
opção 3 = multiplicação(*)
opção 4 = divisão (/)                 
                 ''')
valor_1 = float(input ("Digite o primeiro valor: "))
valor_2 = float(input ("Digite o segundo valor: "))
op =  int (input("Digite a operação: "))

if op == 1:
    resultado = (valor_1 + valor_2)
    print (resultado)
else:
    if op == 2:
        resultado = (valor_1 - valor_2)
        print (resultado)
    else:
        if op == 3:
            resultado = (valor_1 * valor_2)
            print (resultado)
        else:
            if op ==4:
                resultado = (valor_1 / valor_2)
                print (resultado)
            else:
                print ("Não existe opção valida")
                op = 0
                
    


#else:
