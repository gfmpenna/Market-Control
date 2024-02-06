from datetime import datetime


class Categoria:
    def __init__(self, categoria):
        self.categoria = categoria


class Produtos:
    def __init__(self, nome, preco, categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria


class Estoque:
    def __init__(self, produto: Produtos, quantidade):
        self.produto = produto
        self.quantidade = quantidade


class Venda:
    def __init__(self, itensVendido: Produtos, vendedor, comprador, quantidadeVendida, date=datetime.now().strftime("%d/%m/%Y")):
        self.itens_vendido = itensVendido
        self.vendedor = vendedor
        self.comprador = comprador
        self.quantidade = quantidadeVendida
        self.date = date


class Fornecedor:
    def __init__(self, nome, cnpj, telefone, categoria):
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone
        self.categoria = categoria


class Pessoa:
    def __init__(self, nome, telefone, cpf, email, endereco):
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.email = email
        self.endereco = endereco


class Funcionario(Pessoa):
    def __init__(self, clt, nome, cpf, telefone, email, endereco):
        self.clt = clt
        super(Funcionario, self).__init__(nome, cpf, telefone, email, endereco)
