# Projeto-Final-POO
##Projeto: TEMA 9 – SISTEMA DE LOJA VIRTUAL SIMPLIFICADA

## Integrantes da Equipe:

- Sheila Matias Barroso (2025014897) - Modelagem da estrutura e Herança.
- Rubens Lopes dos Santos (2025014805) - Armazenamento de dados e settings.
- Carlos Rodrigo Ferreira da Silva (2025014304) - Gestão de Produto e Cliente.
- Viviana Barros Gomes de Sousa (2025014912) - Lógica central do carrinho, pedido e estoque.
- Vitoria Cavalcante Souza (2025019481) - Cálculos, Pagamento, Frete e Transições.
- Samuelson da Silva Lima (2025014860) - Garantia de qualidade e usabilidade.

## Principais Class do Projeto:

Classe: Produto
Atributos: sku, nome, categoria, preço_unitário, estoque
Métodos: cadastrar(), atualizar(), consultar(), substituir(), excluir()

Classe: Cliente
Atributos: id, nome, email, CPF, endereços
Métodos: cadastrar, atualizar, consultar, excluir

Classe: Carrinho
Atributos: id_carrinho, cliente, lista_produtos, valor_total
Métodos: adicionar_produto(), remover_produto(), calcular_total(), limpar_carrinho(), exibir_carrinho()

Classe: Cupom
Atributos: codigo, tipo_desconto (percentual ou valor fixo), valor_desconto, validade, uso_maximo, categorias_elegiveis
Métodos: validar(), aplicar_desconto()

Classe: Pedido
Atributos: id_pedido, cliente, itens, valor_total, status
Métodos: gerar_pedido(), cancelar_pedido(), consultar_pedido()

Classe: Frete
Atributos: origem, destino (CEP, cidade, UF), valor_frete, prazo_entrega 
Métodos: calcular_frete(), calcular_prazo()

Classe: Pagamento
Atributos:id_pagamento, pedido, forma_pagamento (Pix, débito, crédito, boleto), valor_pago, data_pagamento
Métodos: registrar_pagamento(), validar_pagamento()

# 🛒 Sistema de Loja Virtual Simplificada (CLI)

Projeto desenvolvido para a disciplina de **Programação Orientada a Objetos**, com o objetivo de simular uma loja virtual em ambiente de linha de comando (CLI), aplicando conceitos de **POO, regras de negócio, persistência de dados e testes automatizados**.

---
### 🛒 Sistema de Loja Virtual (CLI)
Este projeto é um simulador de e-commerce operando via linha de comando, desenvolvido com foco em Programação Orientada a Objetos (POO) e Persistência de Dados. O sistema gerencia desde a validação de estoque e aplicação de cupons até o faturamento com geração de Nota Fiscal.

## 🚀 Como Rodar
1. Certifique-se de ter o Python 3.8+ instalado.

2. Clone o repositório ou copie o código para um arquivo chamado main.py.

3. Execute o comando:
```bash
python main.py
```
O sistema criará automaticamente o diretório src/data/ e o arquivo database.json para armazenar os dados.

## 🏗️ Arquitetura e Classes
O projeto está dividido em responsabilidades claras:

- Modelagem (Entidades)
- Produto: Gerencia informações do item, preço e controle rigoroso de estoque via @property.
- Cliente / Endereco: Representam o comprador e o local de destino, essenciais para o cálculo de frete e emissão de nota.
- Cupom: Classe de regra de negócio que valida datas de expiração e tipos de desconto (Fixo ou Percentual).
- Pedido: O "coração" do sistema. Orquestra itens, calcula o total devido, gerencia a transação financeira e altera o estado do estoque.
- Persistência (Dados)
- GerenciadorDados: Centraliza a leitura e escrita no arquivo JSON.
- LojaEncoder: Um padrão de codificação customizado que ensina o Python a salvar objetos complexos (como datetime e Enum) em formato de texto.

## 🧠 Padrões e Conceitos de POO Aplicados
Para atender às exigências de um projeto de alta qualidade, foram utilizados:

- Encapsulamento: Uso de decoradores @property e .setter para garantir que o estoque nunca seja negativo e preços nunca sejam menores ou iguais a zero.
- Enumerações (Enum): Uso da classe StatusPedido para evitar "strings mágicas" e garantir que o pedido passe apenas por estados válidos (CRIADO, PAGO, CANCELADO).
- Composição: Um Pedido é composto por uma lista de ItemCarrinho, que por sua vez compõe um Produto.
- Tratamento de Exceções: Uso de try/except e raise ValueError para lidar com falhas de negócio (ex: tentar pagar um pedido já cancelado ou falta de estoque).

## 📊 Estrutura de Pastas Sugerida
Para organizar este código conforme os padrões de mercado, utilize:
```bash
Plaintext
loja-virtual/
├── src/
│   ├── data/
│   │   └── database.json    # Criado automaticamente
│   └── main.py              # Código principal
└── README.md
```

## 🔗 Diagrama:
<img width="913" height="685" alt="image" src="https://github.com/user-attachments/assets/6d79940b-796f-496d-b479-43a1007dcad9" />


