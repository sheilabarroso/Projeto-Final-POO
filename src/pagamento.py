from datetime import datetime

class Pagamento:
    def __init__(self, pedido, forma: str, valor: float):
        self.pedido = pedido
        self.forma = forma
        self.valor = valor
        self.data = datetime.now()

        self.processar()

    def processar(self):
        if self.valor < self.pedido.total():
            raise ValueError("Valor pago insuficiente")

        self.pedido.status = self.pedido.STATUS_PAGO

        for item in self.pedido.itens:
            item.produto.estoque -= item.quantidade
