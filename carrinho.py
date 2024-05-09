class Negocio:
    def __init__(self, produtos_valores):
        self.produtos_valores = produtos_valores

    def get_produtos_valores(self):
        return self.produtos_valores

    def set_produtos_valores(self, produtos_valores):
        self.produtos_valores = produtos_valores

class Carrinho(Negocio):
    def __init__(self, produtos_valores):
        super().__init__(produtos_valores)

    def apresentar_carrinho(self):
        total = 0
        print("## Carrinho de Compras ##")
        for produto, valor in self.produtos_valores.items():
            print(f"{produto}: R$ {valor:.2f}")
            total += valor
        print(f"Total: R$ {total:.2f}")

# Exemplo de uso
produtos_valores = {
    "Camisa": 50.00,
    "Calça": 180.00,
    "Tênis": 220.00
}

carrinho = Carrinho(produtos_valores)

# Apresentando o carrinho
carrinho.apresentar_carrinho()
