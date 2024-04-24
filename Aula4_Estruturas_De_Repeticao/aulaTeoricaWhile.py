# Estrutura de Repetição While

# O laço while repete um bloco de instruções enquanto determinada condição se mantiver verdadeira

# Inicializa a variável 'x' com o valor 1
x = 1;

print();
print("=" * 50);
# Inicia um loop while que continuará executando enquanto o valor de 'x' for menor ou igual a 5
while x <= 5:
    # Imprime o valor atual de 'x'
    print(x);
    # Incrementa o valor de 'x' em 1
    x = x + 1;
print("=" * 50);
print();

# Variáveis contadoras  e acumuladoras
# Contadoras - Acrescentam valores constantes em uma variável
# Acumuladoras - Acumulam totais, como um somatório

# Exercicio com contador 
    
""" 
Escreva um algoritmo que impira na tela valores dentro de um intervalo especificado pelo usuário e 
que sejam número pares
"""
print("=" * 50);
# Solicita ao usuário que insira o valor inicial para a contagem
inicio = int(input("Digite o valor que deseja iniciar a contagem: "));

# Solicita ao usuário que insira o valor final para a contagem
fim = int(input("Digite o valor que deseja finalizar a contagem: "));

# Inicializa a variável 'x' com o valor inicial fornecido pelo usuário
x = inicio;

# Inicia um loop while que continuará executando enquanto o valor de 'x' for menor ou igual ao valor final fornecido pelo usuário
while x <= fim:
    # Verifica se o valor atual de 'x' é par usando o operador de módulo (%)
    if x % 2 == 0:
        # Se 'x' for par, imprime-o
        print(x);
    # Incrementa o valor de 'x' em 1 para passar para o próximo número na contagem
    x = x + 1;

print("=" * 50);
print();

# Exercício com acumulador

"""
Escreva um algoritmo que calcule a sua média de notas em determinada disciplina.
Vamos assumir que a média final é dada pela média aritmética de cinco notas digitadas.
"""
print("=" * 50);
# Inicializa a variável 'soma' para armazenar a soma das notas
soma = 0;
# Inicializa a variável 'cont' para contar as notas inseridas
cont = 1;

# Inicia um loop while que continuará executando enquanto o valor de 'cont' for menor ou igual a 5
while cont <= 5:
    # Solicita ao usuário que insira a nota atual, usando o valor de 'cont' para indicar a posição da nota
    x = float(input("Digite a {}ª nota: ".format(cont)));
    # Adiciona a nota atual à soma das notas
    soma = soma + x;
    # Incrementa o contador para passar para a próxima nota
    cont = cont + 1;

# Calcula a média das notas dividindo a soma total pelo número de notas inseridas
media = soma / (cont - 1);

# Imprime a média final formatada com duas casas decimais
print("A sua média final é: {:.2f}".format(media));

print("=" * 50);
print();

# Operadores especiais de atribuição

# Abaixo o mesmo exercício anterior feito de uma forma simplificada
print("=" * 50);
soma = 0;
cont = 1;
while cont <= 5 :
    x = float(input("Digite a {}ª nota: " .format(cont)));
    soma += x; # Equivalente à soma = soma + x
    cont += 1; # Equivalente à cont = cont + 1 
media = soma / (cont - 1);
print("A sua média final é: {:.2f}" .format(media));
print("=" * 50);
print();

"""
Crie um algoritmo que receba um valor do tipo inteiro via teclado
Obs: O programa só deve aceitar, obrigatoriamente, valores inteiros e positivos. 
Qualquer valor negativo, ou igual a zero, deve ser rejeitato pelo programa e um novo
valor deve ser solicitado.
"""
print("=" * 50);
numero = int(input("Por gentileza, digite um número inteiro e positivo: "));

while numero <= 0 :
    numero = int(input("Número inválido! Por gentileza, digite um número inteiro e positivo: "));
print("O número digitado foi {}, esse é um valor aceito." .format(numero));
print("=" * 50);
print();

# Interompendo o loop com break

"""
Escreva um algoritimo que fique recebendo frases ou palavras digitadas pelo usuário.
Encerre o algoritmo quando a palavra sair for digitada.
"""
print("=" * 50);
print("Agora serei um papagaio, tudo o que você falar eu irei repetir!")
print("Para fechar meu bico é simples, basta escrever 'sair'!")
while True :
    palavra = input("");
    print(palavra);
    if palavra == "sair":
        break;
print("Fechando meu bico...");
print("=" * 50);
print();

# Usando a instrução continue

"""
Escreva um algoritmo que realize um login em um sistema.
O usuário deve informar seu nome e senha
"""
print("=" * 50);
while True :
    nome = input("Qual o seu nome? ");
    if nome != "Ricck":
        continue;
    senha = input("Qual sua senha? ");
    if senha == "RicckGomes":
        break;
print("Acesso permitido.")
print("=" * 50);
print();

# Valores Truthy e Falsey
print("=" * 50);
nome = "";
while not nome:
    nome = input("Digite seu nome: ");
valor = int(input("Digite um número qualquer: "));
if valor:
    print("Você digitou um valor diferente de zero.");
else:
    print("Você digitou zero.");
print("=" * 50);
print();