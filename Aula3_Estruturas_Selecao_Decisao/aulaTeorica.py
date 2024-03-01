# Condicional Simples e Composta

# Condicional Simples

"""
1 - Desenvolva um programa que lê dois valores numéricos inteiros e compara se o primeiro é 
maior do que o segundo, utilizando uma condicional simples.
Caso seja (resultado verdadeiro), ele imprime na tela a mensagem informando que o primeiro valor 
digitado é maior do que o segundo.
"""
print();
num1 = int(input("Digite um número entre 1 e 100: "));
num2 = int(input("Agora digite mais um número entre 1 e 100: "));
print("=" * 50);
if num1 > num2:
    print("O primeiro número é maior que o segundo!");
print();

# Condicional Composta

"""
2- Desenvolva um programa que lê um valor inteiro e descobre se ele é par ou impar.
"""
num3 = int(input("Digite um número: "));
print("=" * 50);
if num3 % 2 == 1:
    print("O número informado é impar!");
else: 
    print("O número informado é par!");
print();

# Expressões lógicas e álgebra booleana

"""
not: Serve para negar um resultado lógico ou o resultado de uma expressão booleana, ou seja, 
o valor será sempre invertido, ex. se é False vira True e True vira False
"""
x = True;
y = False;
print(not x); # nesse caso será impresso na tela False, pois o not inverte
print(not y);

"""
and: Este operador irá prover um resultado verdadeiro se, e somente se, ambas entradas forem verdadeiras,
ex. v1 = True, v2 = True, v1 and v2 = True, qualquer outra combinação será False.
"""
print(x and y);

"""
or: Este operador irá prover um resultado verdadeiro se ao menos uma das entradas for verdadeira,
ex. v1 = False, v2 = False, o resultado da comparação seria False, se tivesse pelo menos um True o 
resultado seria True.
"""
print(x or y);

"""
Procedência dos operadores
1 - Parênteses
2 - Operadores aritméticos de potenciação ou raiz
3 - Operadores aritméticos de multiplicação, divisão e resto
4 - Operadores aritméticos de adição e subtração
5 - Operadores relacionais, < > = !=
6 - Operadores lógicos not
7 - Operadores lógicos and
8 - Operadores lógicos or
9 - Atribuições
"""

# Exemplos

# Nesse caso será calculado primeiro a comparação e depois acontecerá a negação.
x   = 10;
y   = 1;
res = not x > y;
print();
print(res);

# Nesse caso vai retornar False, pois z não é igual a y.
x = 10;
y = 1;
z = 5.5;
res = x > y and z == y;
print();
print(res);

# Exercício

"""
Um aluno, para passar de ano, precisa ser aprovado em todas as matérias que está cursando.
Assuma que a média para aprovação é a partir de 7, e que o aluno cursa 3 matérias, somente.
Escreva um algorítmo que leia a nota final do aluno em cada matéria e informe, na tela, 
se ele passou de ano ou não.
"""
print();
print("=" * 50);
mAprovacao  = 7.00;
matematica  = float(input("Informa a nota que obteve na matéria de matemática: "));
portugues   = float(input("Informa a nota que obteve na matéria de português: "));
programacao = float(input("Informa a nota que obteve na matéria de programação: "));

if matematica >= mAprovacao and portugues >= mAprovacao and programacao >= mAprovacao :
    print("Parabéns!!! Você foi aprovado!");
    print("Suas notas foram {:.2f} em matemática, {:.2f} em português e {:.2f} em programação." .format(matematica, portugues, programacao));
else:
    print("Que pena, você não foi aprovado!");
    print("É necessário no mínimo {:.2f} em cada matéria para ser aprovado." .format(mAprovacao));
    print("Suas notas foram {:.2f} em matemática, {:.2f} em português e {:.2f} em programação." .format(matematica, portugues, programacao));
print();