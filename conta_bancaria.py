# conta_bancaria.py

class ContaBancaria:
    def __init__(self, cliente, agencia="0001"):
        self.agencia = agencia
        self.numero_conta = ContaBancaria.gerar_numero_conta(cliente.cpf)
        self.cliente = cliente
        self.saldo = 0
        self.extrato = []
        self.numero_saques = 0
        self.limite_saques = 3
        self.limite = 500.00
    
    @staticmethod
    def gerar_numero_conta(cpf):
        return sum(ord(c) for c in cpf) % 1000000  # Gerando número simples baseado no CPF

    def depositar(self, valor):
        if valor <= 0:
            print("Erro: O valor do depósito deve ser positivo.")
            return
        self.saldo += valor
        self.extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    
    def sacar(self, valor):
        if self.numero_saques >= self.limite_saques:
            print("Erro: Limite de saques diários atingido.")
            return
        if valor > self.saldo:
            print("Erro: Saldo insuficiente.")
            return
        if valor > self.limite:
            print(f"Erro: O valor máximo para saque é R$ {self.limite:.2f}.")
            return
        self.saldo -= valor
        self.extrato.append(f"Saque: R$ {valor:.2f}")
        self.numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
    
    def visualizar_extrato(self):
        print("\n--- Extrato ---")
        if not self.extrato:
            print("Nenhuma movimentação realizada.")
        for movimento in self.extrato:
            print(movimento)
        print(f"\nSaldo atual: R$ {self.saldo:.2f}")
