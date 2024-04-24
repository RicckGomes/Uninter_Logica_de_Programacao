# Função para imprimir mensagem de boas-vindas
def mensagemBoasVindas():
    print("=" * 139)
    print(" " * 45 + "Bem-vindo(a) a gráfica do Richard Gomes Teixeira" + " " * 45)
    print("=" * 139)

# Função para escolher o serviço desejado
def escolhaServico():
    print("-" * 57 + "Nossos preços por página" + "-" * 58)
    print("-" * 22 + "| Digitalização (DIG) | Impressão colorida (ICO) | Impressão preto e branco (IBO) | Fotocópia |" + "-" * 22)
    print("-" * 22 + "|       R$1,10        |          R$1,00          |             R$0,40             |   R$0,20  |" + "-" * 22)
    print("-" * 139)
    while True:
        servico = input("Digite o serviço desejado (DIG para Digitalização, ICO para Impressão Colorida, IBO para Impressão Preto e Branco, FOT para Fotocópia): ").upper()
        if servico in ['DIG', 'ICO', 'IBO', 'FOT']:
            # Retorna o valor do serviço com base na escolha do usuário
            if servico == 'DIG':
                return 1.10
            elif servico == 'ICO':
                return 1.00
            elif servico == 'IBO':
                return 0.40
            elif servico == 'FOT':
                return 0.20
        else:
            print("Opção inválida. Por favor, tente novamente.")

# Função para perguntar o número de páginas com desconto
def numPagina():
    while True:
        try:
            numPaginas = int(input("Digite o número de páginas: "))
            if numPaginas < 20:
                return numPaginas
            elif numPaginas >= 20 and numPaginas < 200:
                return numPaginas * 0.85
            elif numPaginas >= 200 and numPaginas < 2000:
                return numPaginas * 0.80
            elif numPaginas >= 2000 and numPaginas <= 20000:
                return numPaginas * 0.75
            else:
                print("*" * 139)
                print(" " * 45 + "Não aceitamos pedidos com mais de 20.000 páginas." + " " * 46)
                print("*" * 139)
        except ValueError:
            print("Por favor, digite um valor numérico válido.")

# Função para escolher o serviço adicional
def servicoExtra():
    print("-" * 47 + "Confira nossos preços de serviços adicionais" + "-" * 48)
    print("-" * 29 + "| Sem adicional (0) | Encadernação simples (1) | Encadernação de capa dura (2) |" + "-" * 30)
    print("-" * 139)
    while True:
        try:
            adicional = int(input("Escolha o serviço adicional (1 para encadernação simples, 2 para encadernação de capa dura, 0 para nenhum adicional): "))
            if adicional in [0, 1, 2]:
                return adicional
            else:
                print("Opção inválida. Por favor, tente novamente.")
        except ValueError:
            print("Por favor, digite um valor numérico válido.")

# Função principal
def main():
    mensagemBoasVindas()
    
    servico    = escolhaServico()
    numPaginas = numPagina()
    adicional  = servicoExtra()

    # Calcula o valor do serviço com base no número de páginas e no serviço adicional
    total = servico * numPaginas
    if adicional == 1:
        total += 15
    elif adicional == 2:
        total += 40

    print("=" * 139)
    print(" " * 57 + "Total a pagar: R${:.2f}".format(total) + " " * 58)
    print("=" * 139)

if __name__ == "__main__":
    main()