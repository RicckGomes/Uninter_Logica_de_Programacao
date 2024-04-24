# Parâmetros em Funções

def realce(s1):
    print("|","__" * 10,"|");
    print("|","__" * 10,"|");
    print(s1);
    print("|","__" * 10,"|");
    print("|","__" * 10,"|");

# Programa principal
realce(" " * 9 + "Ricck");

# Exemplo com mais de um parâmetro
def sub2(x, y):
    res = x - y;
    print(res);

# Programa principal
sub2(10, 5);