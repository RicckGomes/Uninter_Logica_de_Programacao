#Exercícios de Fixação

#Expressões algébricas

# a) O somatório dos 5 primeiros números inteiros e positivos
print('=' * 55);
print("A soma dos números é:", 1+2+3+4+5);
print('=' * 55);

# b) A média entre 23, 19 e 31
print("A média dos números é:", (23+19+31)/3);
print('=' * 55);

# c) O número de vezes que 73 cabe em 403
print("O número de vezes que 73 cabe em 403 é:", 403//73);
print('=' * 55);

# d) A sobra quando 403 é dividido por 73
print("O resto da divisão é:", 403%73);
print('=' * 55);

# e) 2 elevado à 10ª potência
print("O resultado de 2 elevado à 10ª potência é:", 2**10);
print('=' * 55);

# f) O valor absoluto da diferença entre 54 e 57
print("O valor absoluto da diferença entre 54 e 57 é:", abs(54-57));
print('=' * 55);

# g) O menor valor entre 34, 29 e 31
print("O menor valor entre 34, 29 e 31 é:", min(34, 29, 31));
print('=' * 55);

# Atribuição

# Escreva as expressões em Python para:

# a) Atribuir o valor inteiro 3 à variável 'a'
a = 1;
print("O valor atribuido à variável 'a' é:", a);
print('=' * 55);

# b) Atribuir o valor 4 à variável 'b'
b = 4;
print("O valor atribuido à variável 'b' é:", b);
print('=' * 55);

# c) Atribuir à variàvel 'c' o valor da expressão a*a+b*b
c = a*a+b*b;
print("O valor atribuido à variável 'c' é:", c);
print('=' * 55);

# Strings

# Execute as seguintes atribuições:

# s1 = 'ant'
# s2 = 'bat'
# s3 = 'cod'

s1 = 'ant';
s2 = 'bat';
s3 = 'cod';

# Agora, utilizando operadores + e *, crie as saídas a seguir:

# a) 'ant bat cod'
print(s1 + ' ' + s2 + ' ' + s3);
print('=' * 55);

# b) 'ant ant ant ant ant ant ant ant ant ant '
print((s1 + ' ') * 10);
print('=' * 55);

# c) 'ant bat bat cod cod cod'
print(s1 + ' ' + (s2 + ' ') * 2 + (s3 + ' ') * 3);
print('=' * 55);

# d) 'ant bat ant bat ant bat ant bat ant bat ant bat ant bat '
print((s1 + ' ' + s2 + ' ') * 7);
print('=' * 55);

# e) 'batbatcod batbatcod batbatcod batbatcod batbatcod '
print((s2 * 2 + s3 + ' ') * 5);
print('=' * 55);

# Exercícios

"""
1 - Desenvolva um algoritmo que solicite ao usuário o preço de um produto e um percentual de 
desconto a ser aplicado a ele. 
Calcule e exiba o valor do desconto e o preço final do produto (exercício da apostila - aula 2)
""" 

valorProduto = float(input('Por gentileza informe o preço do produto: '));
percentualDesconto = float(input('Qual o percentual de desconto deve ser aplicado? '));
print('-' * 55);
Desconto = valorProduto * (percentualDesconto / 100);
valorFinal = valorProduto - Desconto;
print('O percentual de desconto aplicado é {:.2f}%, o desconto em reais é de R${:.2f} e o preço final é R${:.2f}!' .format(percentualDesconto, Desconto, valorFinal));
print('=' * 55);

"""
2 - Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário,
assim como a quantidade de dias pelos quais o carro foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por km rodado.
"""

valorKmRodado = 0.15;
valorDiariaAluguel = 60;
kmPercorridos = int(input('Por gentileza, informe a quantidade de km rodado: '));
qtdDiasAlugado = int(input('Agora nos informe a quantidade de dias que o usuário ficou com o carro: '));
print('-' * 55);
valorTotalKm = kmPercorridos * valorKmRodado;
valorTotalDiarias = qtdDiasAlugado * valorDiariaAluguel;
valorTotalPagar = valorTotalKm + valorTotalDiarias;
print('O valor total dos {}Km rodados é R${:.2f}.' .format(kmPercorridos, valorTotalKm));
print('O valor total das {} diárias ficou R${:.2f}.' .format(qtdDiasAlugado, valorTotalDiarias));
print('O usuário deverá pagar o valor total de R${:.2f}.' .format(valorTotalPagar));
print('=' * 55);

"""
3 - Crie uma variável de string que receba uma frase qualquer. Crie uma segunda variável, 
agora contendo a metade da string digitada. Imprima na tela somente os dois últimos caracteres da 
segunda variável do tipo string.
"""

frase1 = input('Digite uma frase: ');
print('-' * 55);
tamanho = len(frase1);
frase2 = frase1[:tamanho // 2]
ultimosCaracteres = frase2[-2:]
print('Os dois últimos caracteres da metade da frase são:', ultimosCaracteres);
print('=' * 55);