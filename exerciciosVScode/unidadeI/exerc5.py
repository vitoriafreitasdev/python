class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor 
        self.emprestado = False
    
    def __str__(self):
        status = "Emprestado" if self.emprestado else "Disponível"
        return f"{self.titulo} - {self.autor} ({status})"
    
class Biblioteca:
    def __init__(self):
        self.livros = []
    
    def adicionar_livro(self, titulo, autor):
        self.livros.append(Livro(titulo, autor))
        print(f"Livro '{titulo}' adicionado à biblioteca.")

    def listar_livros_disponiveis(self):
        disponiveis = [livro for livro in self.livros if not livro.emprestado]
        if disponiveis:
            print("\nLivros disponíveis:")
            for livro in disponiveis:
                print(f"- {livro}")
        else:
            print("Nenhum livro disponível no momento.")
            
    def listar_livros_emprestados(self):  # Corrigido o nome do método
        emprestados = [livro for livro in self.livros if livro.emprestado]
        if emprestados:
            print("\nLivros emprestados:")
            for livro in emprestados:
                print(f"- {livro}")
        else:
            print("Nenhum livro emprestado no momento.")

    def emprestar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                if not livro.emprestado:
                    livro.emprestado = True
                    print(f"Livro '{titulo}' emprestado com sucesso.")
                else:
                    print(f"O livro '{titulo}' já está emprestado.")
                return
        print(f"O livro '{titulo}' não foi encontrado na biblioteca.")  # Corrigida a referência

    def devolver_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                if livro.emprestado:
                    livro.emprestado = False 
                    print(f"Livro '{titulo}' devolvido com sucesso.")
                else:
                    print(f"O livro '{titulo}' não estava emprestado.")
                return
        print(f"O livro '{titulo}' não foi encontrado na biblioteca.")  # Corrigida a referência


def exibir_menu():
    print("\nMenu:")
    print("1. Adicionar livro")
    print("2. Listar livros disponíveis")
    print("3. Listar livros emprestados")
    print("4. Emprestar livro")
    print("5. Devolver livro")
    print("6. Sair")

# Programa principal
biblioteca = Biblioteca()

while True:
    exibir_menu()
    try:
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            titulo = input("Digite o título do livro: ").strip()
            autor = input("Digite o autor do livro: ").strip()
            biblioteca.adicionar_livro(titulo, autor)
        elif opcao == 2:
            biblioteca.listar_livros_disponiveis()
        elif opcao == 3:
            biblioteca.listar_livros_emprestados()  # Corrigido o nome do método
        elif opcao == 4:
            titulo = input("Digite o título do livro a ser emprestado: ").strip()
            biblioteca.emprestar_livro(titulo)
        elif opcao == 5:
            titulo = input("Digite o título do livro a ser devolvido: ").strip()
            biblioteca.devolver_livro(titulo)
        elif opcao == 6:
            print("Encerrando...")
            break
        else:
            print("Opção inválida")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número correspondente à opção.")