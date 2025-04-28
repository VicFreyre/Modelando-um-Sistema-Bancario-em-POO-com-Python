# banco.py
from cliente import Cliente
from conta_bancaria import ContaBancaria

class Banco:
    def __init__(self):
        self.clientes = []
        self.contas = []

    def criar_cliente(self, nome, data_nascimento, cpf, endereco):
        if any(cliente.cpf == cpf for cliente in self.clientes):
            print(f"Erro: CPF {cpf} já cadastrado.")
            return None
        cliente = Cliente(nome, data_nascimento, cpf, endereco)
        self.clientes.append(cliente)
        print(f"Cliente {nome} criado com sucesso!")
        return cliente

    def criar_conta_corrente(self, cpf):
        cliente = next((cliente for cliente in self.clientes if cliente.cpf == cpf), None)
        if cliente is None:
            print("Erro: Cliente não encontrado.")
            return None
        conta = ContaBancaria(cliente)
        self.contas.append(conta)
        print(f"Conta {conta.numero_conta} criada com sucesso para {cliente.nome}.")
        return conta
    
    def listar_contas(self):
        for conta in self.contas:
            print(f"Agência: {conta.agencia} | Conta: {conta.numero_conta} | Titular: {conta.cliente.nome}")
