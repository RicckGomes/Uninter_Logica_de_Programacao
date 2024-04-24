# Estrutura de Repetição For

"""
Assim como o while, essa estrutura repete um bloco de instruções enquanto uma condição se mantiver 
verdadeira.
No entanto, diferentemente do while, o for é empregado em situações em que o número de vezes que o 
laço irá executar é finito e bem definido.
"""

# Exemplos

print("=" * 50);
for i in range(6):
    print(i);
print("=" * 50);
print();

print("=" * 50);
for i in range(1, 6, 1):
    print(i);
print("=" * 50);
print();

print("=" * 50);
for i in range(10, 0, -2):
    print(i);
print("=" * 50);
print();

# Exercícios

"""
Escreva um algoritmo que calcule a média de pares de 1 até 100 (1 e 100 inclusos). Implemente usando 
o laço For.
"""

print("=" * 50);
soma = 0;
qtd  = 0;
for i in range(1, 101):
    if i % 2 == 0:
        soma += i;
        qtd  += 1;
media = soma / qtd;
print("A média dos pares de 1 até 100 é: {}" .format(media));
print("=" * 50);
print();