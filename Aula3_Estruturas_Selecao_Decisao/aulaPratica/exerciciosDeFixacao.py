# Exercícios de Fixação

# Expressões booleanas

"""
1 - Escreva as seguintes expressões booleanas em linguagem Python:
Resolução do professor
""" 

# a) O somatório de 2 + 2 é igual a 4?
print(2+2 < 4); # O retorno será False, pois 2+2 não é menor que 4 e sim igual

# b) O valor de 7//3 é igual a 1+1?
print(7//3 == 1+1); # O retorno será True

# c) A soma de 3 elevado ao quadrado com 4 elevado ao quadrado é igual a 25?
print(3**2 + 4**2 == 25); # O retorno será True

# d) A soma de 2, 4 e 6 é maior do que 12?
print(2+4+6 > 12); # O retorno será False

"""
2 - Escreva as seguintes expressões booleanas em linguagem Python:
Resolução própria
"""

# a) 1387 é divisível por 19?
num1 = 1387;
num2 = 19;
a = num1 % num2 == 0;

if a == True:
    print("O número {} é divisível por {}!" .format(num1, num2));
else:
    print("O número {} não é divisivel por {}!" .format(num1, num2));

# b) 31 é par?
num = 31;

if num % 2 == 0:
    print("O número {} é par." .format(num));
else:
    print("O número {} é ímpar." .format(num));

# c) O menor valor entre: 34,29 e 31 é menor que 30?
numeros = [34, 29, 31];
minimo = min(numeros);

if minimo < 30:
    print("O menor valor entre os números 34, 29 e 31 é {}, e ele é menor que 30." .format(minimo));
else:
    print("O menor valor entre os números 34, 29 e 31 é {}, e ele não é menor que 30." .format(minimo));

# Condicional simples

"""
Traduza as afirmações a seguir para condicionais em Python
Resolução do professor
"""

# a) Se idade é maior que 60, escreva: "Você tem direito aos benefícios."
idade = int(input("Digite sua idade: "));
idadeMinima = 60;
mensagem = "Você tem direito aos benefícios."

if idade > idadeMinima:
    print(mensagem);

# b) Se o dano é maior do que 10 e escudo é igual a 0, escreva: "Você está morto!"
dano = int(input("Informe o dano causado: "));
escudo = int(input("Agora informe o escudo: "));

if dano > 10 and escudo == 0:
    print("Você está morto!");

""" c) Se pelo menos uma das variáveis booleanas norte, sul, leste e oeste resultarem em True, 
escreva: "Você escapou!"
"""
norte = False;
sul   = False;
leste = False;
oeste = True;
if norte == True or sul == True or leste == True or oeste == True:  
    print("Você escapou!");
"""
Existe outra forma de fazer uma validação para caso algum dos valores for verdadeiro, chegue a mensagem
"""
if norte or sul or leste or oeste:
    print("Você escapou!");

# Condicional composta

"""
Traduza as afirmações a seguir para condicionais em Python
Resolução própria
"""

""" 
a) Se ano é divisível por 4, escreva: "Pode ser ano bissexto". Caso contrário, 
escreva: "Definitivamente não é um ano bissexto"
"""
ano = int(input("Digite o ano: "));

if ano % 4 == 0:
    print("Pode ser ano bissexto.");
else:
    print("Definitivamente não é ano bissexto.");

"""
b) Se ambas as variáveis booleanas cima e baixo forem True, escreva: "Decida-se!", caso contrário, 
escreva: "Você escolheu um caminho!"
"""
cima  = False;
baixo = True;

if cima and baixo:
    print("Decida-se!");
else:
    print("Você escolheu um caminho!");