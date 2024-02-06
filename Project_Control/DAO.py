from Models import *


class DaoCategoria:
    @classmethod
    def salvar(cls, categoria):
        with open('Categorias.txt', "a") as arq:
            arq.writelines(categoria)
            arq.writelines('\n')

    @classmethod
    def listar(cls):
        with open('Categorias.txt', "r") as arq:
            cls.categoria = arq.readlines()
        cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria))  # Aqui estamos eliminando o \n da linha
        cat = [Categoria(i) for i in (cls.categoria)]

        return print(cat)


class DaoVenda:
    @classmethod
    def salvar(cls, venda: Venda):
        with open('Vendas.txt', "a") as arq:
            arq.writelines(
                venda.itens_vendido.nome + "|" +
                venda.itens_vendido.preco + "|" +
                venda.itens_vendido.categoria + "|" +
                venda.vendedor + "|" +
                venda.comprador + "|" +
                str(venda.quantidade) + "|" +
                venda.date
            )
            arq.writelines('\n')

    @classmethod
    def listar(cls):
        with open('Vendas.txt', "r") as arq:
            cls.venda = arq.readlines()
            cls.venda = list(map(lambda v: v.replace('\n', ''), cls.venda))
            cls.venda = list(map(lambda v: v.split('|'), cls.venda))
        ven = []
        for i in cls.venda:
            ven.append(Venda(Produtos(i[0], i[1], i[2]), i[3], i[4], i[5], i[6]))
        return ven


class DaoEstoque:
    @classmethod
    def salvar(cls, produtos: Produtos, quantidade):
        with open('Estoque.txt', "a") as arq:
            arq.writelines(
                produtos.nome + "|" +
                produtos.preco + "|" +
                produtos.categoria + "|" +
                str(quantidade)
            )
            arq.writelines('\n')

    @classmethod
    def listar(cls):
        with open('Estoque.txt', "r") as arq:
            cls.Estoque = arq.readlines()

            cls.Estoque = list(map(lambda x: x.replace('\n', ''), cls.Estoque))
            cls.Estoque = list(map(lambda v: v.split('|'), cls.Estoque))

        estoque = []
        if len(cls.Estoque) > 0:
            for i in cls.Estoque:
                estoque.append(Estoque(Produtos(i[0], i[1], i[2]), i[3]))

        return estoque


class DaoFornecedor:

    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
        with open('Fornecedor.txt', "a") as arq:
            arq.write(
                fornecedor.nome + "|" +
                fornecedor.cnpj + "|" +
                fornecedor.telefone + "|" +
                fornecedor.categoria
            )
            arq.writelines('\n')

    @classmethod
    def listar(cls):
        with open('Fornecedor.txt', "r") as arq:
            cls.Fornecedor = arq.readlines()
            cls.Fornecedor = list(map(lambda x: x.replace('\n', ''), cls.Fornecedor))
            cls.Fornecedor = list(map(lambda x: x.split('|'), cls.Fornecedor))

        forne = []
        for i in cls.Fornecedor:
            forne.append(Fornecedor(i[0], i[1], i[2], i[3]))

        return forne


# DaoFornecedor.salvar(Fornecedor('Joaquim','1234345343-0001/54','22 999517080','Legumes'))
# print(DaoFornecedor.listar())

class DaoPessoa:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open('Pessoa.txt', "a") as arq:
            arq.write(
                pessoa.nome + "|" +
                pessoa.telefone + "|" +
                pessoa.cpf + "|" +
                pessoa.email + "|" +
                pessoa.endereco
            )
            arq.writelines('\n')

    @classmethod
    def listar(cls):
        with open('Pessoa.txt', "r") as arq:
            cls.Pessoa = arq.readlines()
            cls.Pessoa = list(map(lambda x: x.replace('\n', ''), cls.Pessoa))
            cls.Pessoa = list(map(lambda x: x.split('|'), cls.Pessoa))
        pess = []
        for i in cls.Pessoa:
            pess.append(Pessoa(i[0], i[1], i[2], i[3], i[4]))
        return pess


# DaoPessoa.salvar(Pessoa('Ramom','22 9999917080', '154633232-75','Meuemailaqui@gmail.com','Rua sem Limites n° 42'))
# print(DaoPessoa.listar())

class DaoFuncionario:

    @classmethod
    def salvar(cls, funcionario: Funcionario):
        with open('Funcionarios.txt', "a") as arq:
            arq.write(
                funcionario.clt + "|" +
                funcionario.nome + "|" +
                funcionario.cpf + "|" +
                funcionario.telefone + "|" +
                funcionario.email + "|" +
                funcionario.endereco
            )
            arq.writelines('\n')

    @classmethod
    def listar(cls):
        with open('Funcionarios.txt', "r") as arq:
            cls.Funcionarios = arq.readlines()
            cls.Funcionarios = list(map(lambda x: x.replace('\n', ''), cls.Funcionarios))
            cls.Funcionarios = list(map(lambda x: x.split('|'), cls.Funcionarios))
        func = []
        for i in cls.Funcionarios:
            func.append(Funcionario([0], [1], [2], [3], [4], [5]))

        return func


#DaoFuncionario.salvar(Funcionario('2543544','Steve Jobs', '111444333444-66', '2543544222', 'meuemail@hotmail.com','Minha Rua N ° 999'))
#print(DaoFuncionario.listar())