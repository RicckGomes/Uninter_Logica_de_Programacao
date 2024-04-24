print("=" * 81)
print(" Bem-vindo(a) a GelaGuela, a deliciosa loja de gelados do Richard Gomes Teixeira")
print("=" * 81)

print("-" * 36 + "Cardápio" + "-" * 36)
print("-" * 21 + "| Tamanho | Cupuaçu (CP) | Açai (AC) |" + "-" * 21)
print("-" * 21 + "|    P    |   R$10,00    |  R$12,00  |" + "-" * 21)
print("-" * 21 + "|    M    |   R$15,00    |  R$17,00  |" + "-" * 21)
print("-" * 21 + "|    G    |   R$19,00    |  R$21,00  |" + "-" * 21)
print("-" * 80)

# Inicialização do acumulador para somar os valores dos pedidos
totalPedido = 0

while True:
    """
    O método upper() é usado para garantir que qualquer entrada seja convertida para letras maiúsculas.
    Isso é feito para facilitar a comparação com as opções válidas (CP ou AC), independentemente de 
    o usuário inserir letras maiúsculas ou minúsculas.
    """
    sabor = input("Digite o sabor desejado (CP para Cupuaçu, AC para Açaí): ").upper()
    
    if sabor not in ['CP', 'AC']:
        print("Sabor inválido. Tente novamente.")
        continue
    
    tamanho = input("Digite o tamanho desejado (P para Pequeno, M para Médio, G para Grande): ").upper()
    
    if tamanho not in ['P', 'M', 'G']:
        print("Tamanho inválido. Tente novamente.")
        continue
    
    if sabor == 'CP':
        if tamanho == 'P':
            preco = 10.00
        elif tamanho == 'M':
            preco = 15.00
        else:
            preco = 19.00
    else:
        if tamanho == 'P':
            preco = 11.00
        elif tamanho == 'M':
            preco = 17.00
        else:
            preco = 21.00
    
    # Adiciona o preço do pedido ao acumulador
    totalPedido += preco
    
    continuar = input("Deseja pedir mais alguma coisa? (S para Sim, qualquer outra coisa para Não): ").upper()
    
    # Se o usuário não deseja mais pedidos, encerra o loop
    if continuar != 'S':
        break

print("=" * 81)
print(" " * 23 + "O valor total do pedido é: R${:.2f}".format(totalPedido))
print("=" * 81)