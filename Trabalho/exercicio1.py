print("=" * 88)
print(" " * 18 + "Bem-vindo a loja do Richard Gomes Teixeira - 4675903")
print("=" * 88)

"""
O loop while True cria um loop infinito. Ele continuará executando o código dentro dele 
repetidamente, indefinidamente, até que uma condição de parada seja encontrada. Neste 
caso, não há uma condição de parada explícita definida dentro do loop, mas ele é 
interrompido pelo 'break' quando uma entrada válida é fornecida pelo usuário.
"""
while True:
    """
    O bloco try é usado para tentar executar o código dentro dele. Se ocorrer uma exceção 
    durante a execução deste código, o controle passará para o bloco 'except'.
    """
    try:
        valorUnitario = float(input("Informe o valor unitário do produto: R$"))
        qtdProduto    = int(input("Informe a quantidade do produto: "))
        if valorUnitario <= 0 or qtdProduto <= 0:
            print("*" * 88)
            print("Os valores não podem ser 0 nem negativos. Por favor, insira valores válidos.")
            print("*" * 88)
        else:
            """
            Se os valores inseridos forem válidos, o 'break' é utilizado para sair do loop 
            'while True', interrompendo o loop e continuando a execução do código após o loop.
            """
            break
    # O bloco except ValueError é executado caso ocorra uma exceção do tipo ValueError. 
    # Isso acontece se a entrada do usuário não puder ser convertida para float ou int. Neste 
    # caso, uma mensagem é exibida indicando que a entrada é inválida.
    except ValueError:
        print("*" * 88)
        print("Entrada inválida. Por favor, insira um número válido.")
        print("*" * 88)

valorTotal    = valorUnitario * qtdProduto
desconto1     = valorTotal * 0.04 # Equivalente a 4%
desconto2     = valorTotal * 0.07 # Equivalente a 7%
desconto3     = valorTotal * 0.11 # Equivalente a 11%
print("O valor total foi R${:.2f}." .format(valorTotal))

if valorTotal < 2500:
    print("Que pena, não temos desconto. :-(")
elif (valorTotal >= 2500) and (valorTotal < 6000):
    print("Que legal, temos desconto rolando. :-)")
    print("O desconto foi de R${:.2f}. O valor total com desconto foi R${:.2f} (desconto de 4%)" .format(desconto1, valorTotal - desconto1))
elif (valorTotal >= 6000) and (valorTotal < 10000):
    print("Que legal, temos desconto rolando. :-)")
    print("O desconto foi de R${:.2f}. O valor total com desconto foi R${:.2f} (desconto de 7%)" .format(desconto2, valorTotal - desconto2))
else:
    print("Que legal, temos desconto rolando.:-)")
    print("O desconto foi de R${:.2f}. O valor total com desconto foi R${:.2f} (desconto de 11%)" .format(desconto3, valorTotal - desconto3))
print("=" * 88)