import csv

class Cliente:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

class GerenciadorClientes:
    def __init__(self):
        self.clientes = {}

    def adicionar_cliente(self, cliente):
        self.clientes[cliente.email] = cliente
        print(f"Cliente {cliente.nome} adicionado com sucesso!")
        self.salvar_clientes()

    def listar_clientes(self):
        print("Lista de clientes:")
        for email, cliente in self.clientes.items():
            print(f"Nome: {cliente.nome}")
            print(f"Email: {cliente.email}")
            print(f"Telefone: {cliente.telefone}")
            print("-" * 30)

    def salvar_clientes(self):
        with open("clientes.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Nome", "Email", "Telefone"])
            for cliente in self.clientes.values():
                writer.writerow([cliente.nome, cliente.email, cliente.telefone])

    def carregar_clientes(self):
        try:
            with open("clientes.csv", mode="r") as file:
                reader = csv.reader(file)
                next(reader)  # Ignora a linha de cabeçalho
                for row in reader:
                    nome, email, telefone = row
                    cliente = Cliente(nome, email, telefone)
                    self.clientes[email] = cliente
        except FileNotFoundError:
            pass

def main():
    gerenciador = GerenciadorClientes()
    gerenciador.carregar_clientes()

    while True:
        print("\nMenu:")
        print("1. Adicionar Cliente")
        print("2. Listar Clientes")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            nome = input("Digite o nome do cliente: ")
            email = input("Digite o email do cliente: ")
            telefone = input("Digite o telefone do cliente: ")
            novo_cliente = Cliente(nome, email, telefone)
            gerenciador.adicionar_cliente(novo_cliente)
        elif opcao == '2':
            gerenciador.listar_clientes()
        elif opcao == '3':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()