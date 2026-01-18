from produto import Produto
from cliente import Cliente
from carrinho import Carrinho
from item_carrinho import ItemCarrinho
from pedido import Pedido
from pagamento import Pagamento
from frete import Frete


def main():
    print("=== LOJA VIRTUAL ===\n")

    
    cliente = Cliente(
        id_cliente=1,
        nome="Vitória Cavalcante",
        email="vitoria@email.com",
        cpf="123.456.789-00"
    )

    
    produto1 = Produto("001", "Mouse Gamer", 120.00, 10)
    produto2 = Produto("002", "Teclado Mecânico", 250.00, 5)


    carrinho = Carrinho(cliente)
    carrinho.adicionar_produto(produto1, 2)
    carrinho.adicionar_produto(produto2, 1)

    print("Carrinho criado com sucesso!")
    print(f"Total do carrinho: R$ {carrinho.calcular_total():.2f}\n")

    
    frete = Frete("CE")
    valor_frete, prazo = frete.calcular_frete()

    print(f"Frete calculado: R$ {valor_frete:.2f}")
    print(f"Prazo de entrega: {prazo} dias úteis\n")

    
    pedido = Pedido(
        cliente=cliente,
        itens=carrinho.itens,
        valor_frete=valor_frete
    )

    print(f"Pedido criado com sucesso! ID: {pedido.id}")
    print(f"Total do pedido: R$ {pedido.total_pedido():.2f}\n")

    
    pagamento = Pagamento(
        forma_pagamento="PIX",
        valor=pedido.total_pedido()
    )

    pagamento.confirmar_pagamento()
    pedido.confirmar_pagamento()

    print("\n=== COMPRA FINALIZADA COM SUCESSO ===")


if __name__ == "__main__":
    main()
