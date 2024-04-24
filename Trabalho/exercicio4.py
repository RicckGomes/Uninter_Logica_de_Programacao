# Mensagem de boas-vindas
def mensagemBoasVindas():
    print("=" * 85)
    print(" " * 4 + "Bem-vindo(a) ao sistema de gerenciamento de livros do Richard Gomes Teixeira!")
    print("=" * 85)

# Função para cadastrar um livro
def cadastrarLivro(id):
    print("-" * 34 + "Menu de cadastro" + "-" * 35)
    nome    = input("Digite o nome do livro: ")
    autor   = input("Digite o autor do livro: ")
    editora = input("Digite a editora do livro: ")
    
    livro   = {'ID': id, 'Nome': nome, 'Autor': autor, 'Editora': editora}
    listaLivro.append(livro)

    print("*" * 85)
    print(" " * 28 + "Livro cadastrado com sucesso!")
    print(" " * 25 + "Número do ID do livro cadastrado:", id)
    print("*" * 85)

# Função para consultar livros
def consultarLivro():
    while True:
        print("-" * 34 + "Menu de consulta" + "-" * 35)
        try:
            opcao = int(input("Escolha uma opção:\n1. Consultar Todos\n2. Consultar por Id\n3. Consultar por Autor(a)\n4. Retornar ao menu\nOpção: "))
            print("-" * 85)
            if opcao == 1:
                print("Todos os livros cadastrados:")
                for livro in listaLivro:
                    print("Id:", livro['ID'])
                    print("Nome do livro:", livro['Nome'])
                    print("Autor(a):", livro['Autor'])
                    print("Editora:", livro['Editora'])
                    print("-" * 85)
                break
            elif opcao == 2:
                id = int(input("Digite o ID do livro que deseja consultar: "))
                for livro in listaLivro:
                    if livro['ID'] == id:
                        print("Livro encontrado:")
                        print("Id:", livro['ID'])
                        print("Nome do livro:", livro['Nome'])
                        print("Autor(a):", livro['Autor'])
                        print("Editora:", livro['Editora'])
                        return
                print("Livro com o ID fornecido não encontrado.")
                break
            elif opcao == 3:
                autor = input("Digite o nome do autor(a) que deseja consultar: ")
                print("Livros do autor(a) {}: " .format(autor))
                for livro in listaLivro:
                    if livro['Autor'] == autor:
                        print("Id:", livro['ID'])
                        print("Nome do livro:", livro['Nome'])
                        print("Autor(a):", livro['Autor'])
                        print("Editora:", livro['Editora'])
                break
            elif opcao == 4:
                break
            else:
                print("*" * 85)
                print(" " * 35 + "Opção inválida.")
                print("*" * 85)
        except ValueError:
            print("*" * 85)
            print(" " * 24 + "Por favor, digite um número inteiro.")
            print("*" * 85)

# Função para remover livro
def removerLivro():
    while True:
        try:
            id = int(input("Digite o ID do livro que deseja remover: "))
            for livro in listaLivro:
                if livro['ID'] == id:
                    listaLivro.remove(livro)
                    print("*" * 85)
                    print(" " * 29 + "Livro removido com sucesso.")
                    print("*" * 85)
                    return
            print("*" * 85)
            print(" " * 22 + "Livro com o ID fornecido não encontrado.")
            print("*" * 85)
            break
        except ValueError:
            print("*" * 85)
            print(" " * 24 + "Por favor, digite um número inteiro.")
            print("*" * 85)

# Função principal (menu)
def main():
    mensagemBoasVindas()
    while True:
        try:
            print("-" * 36 + "Menu inicial" + "-" * 37)
            print("| 1. Cadastrar Livro | 2. Consultar Livro | 3. Remover Livro | 4. Encerrar Programa |")
            print("-" * 85)
            opcao = int(input("Escolha uma opção: "))
            if opcao == 1:
                global idGlobal
                idGlobal += 1
                cadastrarLivro(idGlobal)
            elif opcao == 2:
                consultarLivro()
            elif opcao == 3:
                removerLivro()
            elif opcao == 4:
                print("=" * 85)
                print(" " * 30 + "Encerrando o programa...")
                print("=" * 85)
                break
            else:
                print("*" * 85)
                print(" " * 35 + "Opção inválida.")
                print("*" * 85)
        except ValueError:
            print("*" * 85)
            print(" " * 24 + "Por favor, digite um número inteiro.")
            print("*" * 85)

# Lista de livros
listaLivro = []
# ID global para os livros
idGlobal = 0

if __name__ == "__main__":
    main()