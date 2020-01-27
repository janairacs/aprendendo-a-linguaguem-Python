#Exercício 3.6 - Escreva uma expressão que será utilizada para decidir se um aluno
#foi ou não aprovado. Para ser aprovado, todas as médias do aluno devem ser maiores
#que 7. Considere que o aluno cursa apenas três materias, e que a nota de cada uma está
# armazenada nas seguintes variáveis:materia1, materia2 e materia3.

materia1 = float (input("Digite sua nota da 1° materia: "))
materia2 = float (input("Digite sua nota da 2° materia: "))
materia3 = float (input("Digite sua nota da 3° materia: "))

resultado = materia1 >=7 and materia2 >=7 and materia3 >=7

print (resultado)
