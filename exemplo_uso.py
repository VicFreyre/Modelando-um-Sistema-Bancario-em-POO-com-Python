# main.py
from banco import Banco

def main():
    banco = Banco()

    # Criar cliente
    cliente1 = banco.criar_cliente("João Silva", "1990-05-15", "12345678901", "Rua A, 123 Centro São Luís/MA")

    # Criar conta para o cliente
    conta1 = banco.criar_conta_corrente("12345678901")

    # Realizar depósito
    conta1.depositar(1500)

    # Realizar saque
    conta1.sacar(500)

    # Visualizar extrato
    conta1.visualizar_extrato()

    # Listar contas
    banco.listar_contas()

if __name__ == "__main__":
    main()
