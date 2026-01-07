from produto import Produto
from cliente import Cliente
from carrinho import Carrinho

p1 = Produto("101", "Teclado Mecânico", "Periféricos", 250.00, 10)
p2 = Produto("202", "Mouse Gamer", "Periféricos", 150.00, 5)


cliente = Cliente(1, "Carlos Silva", "carlos@email.com", "12345678900", ["Rua A, 10"])

carrinho = Carrinho(1, cliente)
carrinho.adicionar_produto(p1, 1)
carrinho.adicionar_produto(p2, 2)
carrinho.exibir()
