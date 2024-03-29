"""
2 - Escreva um algoritmo que leia dois valores numéricos e que pergunte ao usuário qual operação ele 
deseja realizar:adição (+), subtração (-), multiplicação (*) ou divisão (/). Exiba na tela o resultado
da operação desejada (exercício da apostila - aula 3)
"""
print("=" * 50);
print("Vamos fazer uma operação matemática?");
print("=" * 50);
num1 = int(input("Por gentileza. digite um número inteiro: "));
num2 = int(input("Por gentileza, digite mais um número inteiro: "));
print("Perfeito, os números escolhidos são: {} e {}" .format(num1, num2));
print("Agora me fale qual operação você deseja realizar:");
operacao = int(input("Digite 1 - Adição, 2 - Subtração, 3 - Multiplicação ou 4 - Divisão: "));
adicao        = num1 + num2;
subtracao     = num1 - num2;
multiplicacao = num1 * num2;
divisao       = num1 / num2;

if operacao == 1:
    print("Você escolheu somar os números {} e {}, o resultado é {}!" .format(num1, num2, adicao));
elif operacao == 2:
    print("Você escolheu soubtrair os números {} e {}, o resultado é {}!" .format(num1, num2, subtracao));
elif operacao == 3:
    print("Você escolheu multiplicar os números {} e {}, o resultado é {}!" .format(num1, num2, multiplicacao));
else:
    print("Você escolheu dividir os números {} e {}, o resultado é {:.2f}!" .format(num1, num2, divisao));
print("=" * 50);
print();