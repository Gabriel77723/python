import datetime

class ContaBancaria:
    def __init__(self, numero_conta, titular, saldo, tipo_conta):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo
        self.tipo_conta = tipo_conta
        self.movimentacoes = []

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise TypeError("Valor inválido. Deve ser um número.")
        elif valor <= 0:
            raise ValueError("Valor inválido. Deve ser maior que zero.")
        else:
            self.saldo += valor
            self.registrar_movimentacao("Depósito", valor)
            print("Depósito realizado com sucesso!")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor
            self.registrar_movimentacao("Saque", -valor)

    def transferir(self, valor, conta_destino):
        if valor > self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor
            conta_destino.saldo += valor
            self.registrar_movimentacao("Transferência", -valor)
            conta_destino.registrar_movimentacao("Transferência", valor)

    def consultar_saldo(self):
        print(f"Saldo: {self.saldo}")

    def extrato(self):
        print("Extrato:")
        for movimentacao in self.movimentacoes:
            print(f"{movimentacao['data']}: {movimentacao['tipo']}: R$ {movimentacao['valor']:.2f}")

    def registrar_movimentacao(self, tipo, valor):
        movimentacao = {
            "data": datetime.datetime.now(),
            "tipo": tipo,
            "valor": valor
        }
        self.movimentacoes.append(movimentacao)

class ContaPoupanca(ContaBancaria):
    def __init__(self, numero_conta, titular, saldo, taxa_juros):
        super().__init__(numero_conta, titular, saldo, "Poupança")
        self.taxa_juros = taxa_juros

    def render_juros(self):
        juros = self.saldo * (self.taxa_juros / 100)
        self.saldo += juros
        self.registrar_movimentacao("Rendimento de Juros", juros)

class ContaCorrente(ContaBancaria):
    def __init__(self, numero_conta, titular, saldo, limite_saque_diario, limite_transferencia):
        super().__init__(numero_conta, titular, saldo, "Corrente")
        self.limite_saque_diario = limite_saque_diario
        self.limite_transferencia = limite_transferencia

    def sacar(self, valor):
        if valor > self.limite_saque_diario:
            print("Limite de saque diário excedido")
        else:
            super().sacar(valor)

    def transferir(self, valor, conta_destino):
        if valor > self.limite_transferencia:
            print("Limite de transferência excedido")
        else:
            super().transferir(valor, conta_destino)

class SaldoInsuficienteError(Exception):
    pass

class LimiteSaqueExcedidoError(Exception):
    pass
# Criando uma conta poupança
conta_poupanca = ContaPoupanca(1234, "João Silva", 1000.0, 0.5)

# Depositando dinheiro
conta_poupanca.depositar(800.0)

# Sacando dinheiro
conta_poupanca.sacar(400.0)

# Rendendo juros
conta_poupanca.render_juros()

# Consultando saldo
conta_poupanca.consultar_saldo()

# Exibindo extrato
conta_poupanca.extrato()

# Criando uma conta corrente
conta_corrente = ContaCorrente(5678, "Maria Santos", 2000.0, 1000.0, 5000.0)

# Transferindo dinheiro
conta_corrente.transferir(800.0, conta_poupanca)

# Tentando sacar além do limite
conta_corrente.sacar(3000.0)# Criando uma conta poupança
conta_poupanca = ContaPoupanca(1234, "João Silva", 1000.0, 0.5)

# Depositando dinheiro
conta_poupanca.depositar(8000.0)

# Sacando dinheiro
conta_poupanca.sacar(300.0)

# Rendendo juros
conta_poupanca.render_juros()

# Consultando saldo
conta_poupanca.consultar_saldo()

# Exibindo extrato
conta_poupanca.extrato()

# Criando uma conta corrente
conta_corrente = ContaCorrente(5678, "Maria Santos", 2000.0, 1000.0, 5000.0)

# Transferindo dinheiro
conta_corrente.transferir(500.0, conta_poupanca)

# Tentando sacar além do limite
conta_corrente.sacar(1500.0)