# Exercicíos

"""
1 - Faça um algoritmo que receba três valores, representando os lados de um triângulo fornecidos 
pelo usuário. Verifique se os valores formam um triângulo e classifique como:
a) Equilátero (três lados iguais)
b) Isósceles (dois lados iguais)
c) Escaleno (três lados diferentes)
Lembre-se de que, para formar um triângulo, nenhum dos lados pode ser igual a zero, e um lado não 
pode ser maior que a soma dos outros dois.
"""
# Recebendo os valores dos lados do triângulo do usuário
num1 = int(input("Informe o valor do primeiro lado do triângulo: "))
num2 = int(input("Informe o valor do segundo lado do triângulo: "))
num3 = int(input("Informe o valor do terceiro lado do triângulo: "))

# Verificando se nenhum dos lados é igual a zero, o que é essencial para formar um triângulo
if num1 != 0 and num2 != 0 and num3 != 0:
    # Verificando se os valores fornecidos podem formar um triângulo
    if (num1 > num2 + num3) or (num2 > num1 + num3) or (num3 > num1 + num2):
        # Se algum dos lados for maior que a soma dos outros dois, não pode formar um triângulo
        print("Um lado não pode ser maior que a soma dos outros dois!")
    else:
        # Se os valores fornecidos podem formar um triângulo, classificamos o tipo de triângulo
        if num1 == num2 and num2 == num3:
            # Triângulo Equilátero: todos os lados são iguais
            print("Este é um triângulo Equilátero!")
        elif num1 == num2 or num1 == num3 or num2 == num3:
            # Triângulo Isósceles: dois lados são iguais
            print("Este é um triângulo Isósceles!")
        else:
            # Triângulo Escaleno: todos os lados são diferentes
            print("Este é um triângulo Escaleno!")
else:
    # Se algum dos lados for zero, não pode formar um triângulo
    print("Nenhum dos lados de um triângulo pode ser igual a zero!")
