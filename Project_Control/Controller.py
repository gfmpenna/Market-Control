from Models import *
from DAO import *
from datetime import datetime


class ControllerCategoria:

    def cadastrarCategoria(self, novoCategoria):
        existeCategoria = False
        x = DaoCategoria.listar()
        for i in x:
            if i.categoria == novoCategoria:
                existeCategoria = True

        if not existeCategoria:
            DaoCategoria.salvar(novoCategoria)
            print('Categoria Cadastrada com sucesso!')
        else:
            print('Categoria Existente')

    def deletarCategoria(self, deletaCategoria):
        C = DaoCategoria.listar()

        categoria_list = list(filter(lambda x: x.categoria == deletaCategoria, C))

        if len(categoria_list) <= 0:
            print('Categoria que deseja remover no existe')
        else:
            for i in range(len(C)):
                if C[i].categoria == deletaCategoria:
                    del C[i]
                    break
            print('Categoria removido com sucesso!')
            # TODO: COLOCAR SEM CATEGORIA NO ESTOQUE
            with open('Categorias.txt', "w") as arq:
                for i in C:
                    arq.write(i.categoria)
                    arq.write('\n')

    def alterarCategoria(self, alterarCategoria, alteradaCategoria):
        x = DaoCategoria.listar()

        cat = list(filter(lambda x: x.categoria == alterarCategoria, x))
        if len(cat) > 0:
            cat_anterada = list(filter(lambda x: x.categoria == alteradaCategoria, x))
            if len(cat_anterada) == 0:
                x = list(map(lambda x: Categoria(alteradaCategoria) if (x.categoria == alterarCategoria) else (x), x))
                print('Categoria alterada com Sucesso')
                # TODO: ALTERAR CATEGORIA TAMBEM NO ESTOQUE
            else:
                print('Categoria que deseja alterar já existe')
        else:
            print('Categoria que deseja alterar não existe')

        with open('Categorias.txt', "w") as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.write('\n')

    def mostrarCategorias(self):
        categorias = DaoCategoria.listar()

        if len(categorias) == 0:
            print('Categorias Não existentes!')
            return 0
        for i in categorias:
            print(f'Categoria {i.categoria}')


'''
c = ControllerCategoria()
c.mostrarCategorias()
c.cadastrarCategoria('Cereais')
c.deletarCategoria('Limpeza')
c.alterarCategoria('Carnes', 'Carnes')
c.deletarCategoria('Cereais')
c = ControllerCategoria()
c.cadastrarCategoria('Cereais')
'''


class ControllerEstoque:

    def cadastrarProduto(self, nome, preco, categoria, quantidade):
        x = DaoEstoque.listar()
        y = DaoCategoria.listar()
        cat = list(filter(lambda c: c.categoria == categoria, y))
        est = list(filter(lambda n: n.produto.nome == nome, x))

        if len(cat) > 0:
            if len(est) == 0:
                produto = Produtos(nome, preco, categoria)
                DaoEstoque.salvar(produto, quantidade)
                print('Produto cadastrado com Sucesso')
            else:
                print('Produto não Cadastrado!')
        else:
            print('Categoria Inexistente')

    def deletarProduto(self, nome):
        x = DaoEstoque.listar()

        delProd = list(filter(lambda c: c.produto.nome == nome, x))

        if len(delProd) > 0:
            for i in range(len(x)):
                if x[i].produto.nome == nome:
                    del x[i]
                    break
            print('Produto Excluido com Sucesso')
        else:
            print('Produto Inexistente, impossivel remover')

        with open('Estoque.txt', "w") as arq:
            for i in x:
                arq.writelines(
                    i.produto.nome + "|" + i.produto.preco + "|" + i.produto.categoria + "|" + str(i.quantidade) + "\n")

    def alterarProduto(self, nomeAlterar, novoNome, novoPreco, novaCategoria, novaQuantidade):

        x = DaoEstoque.listar()
        y = DaoCategoria.listar()

        altNome = list(filter(lambda x: x.produto.nome == nomeAlterar, x))
        altCategoria = list(filter(lambda y: y.categoria == novaCategoria, y))

        if len(altCategoria) > 0:
            if len(altNome) > 0:
                est = list(filter(lambda x: x.produto.nome == novoNome, x))
                if len(est) == 0:
                    x = list(map(lambda n: Estoque(Produtos(novoNome, novoPreco, novaCategoria), novaQuantidade) if (
                            n.produto.nome == nomeAlterar) else (n), x))
                    print(f'Produto Alterado com sucesso')
                else:
                    print(f'Produto já Existe')
            else:
                print('Produto Não Exites nos  Cadastros!')

            with open('Estoque.txt', "w") as arq:
                for i in x:
                    arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" + i.produto.categoria + "|" + str(
                        i.quantidade))
                    arq.writelines("\n")
        else:
            print('Produto ou Categoria não existem')

    def mostrarEstoque(self):
        estoque = DaoEstoque.listar()

        if estoque is not None:
            for i in estoque:
                print("________ PRODUTOS _____________")
                print(f'Nome: {i.produto.nome}')
                print(f'Preço: {i.produto.preco}')
                print(f'Categoria: {i.produto.categoria}')
                print(f'Quantidade: {i.quantidade}')

        else:
            print('Estoque Vazio')


c = ControllerEstoque()


# c.cadastrarProduto('Mamão', '14.99', 'Legumes', '10')
# c.alterarProduto('Mamão', 'Laranja', '15,99', 'Legumes', '10')
# c.deletarProduto('Tomate')
# c.mostrarEstoque()


class ControllerVenda:

    def cadastrarVenda(self, nomeProduto, vendedor, comprador, quantidadeVendida):
        x = DaoEstoque.listar()

        y = list(filter(lambda y: y.produto.nome == nomeProduto, x))
        z = list(filter(lambda z: z.quantidade >= quantidadeVendida, x))
        val = 0
        produto_encontrado = 0
        print(len(y), len(z))

        if len(y) > 0:

            for item in x:
                if item.produto.nome == nomeProduto:
                    produto_encontrado = item.quantidade
                    if produto_encontrado > quantidadeVendida:
                        totalVendido = float(item.produto.preco) * float(quantidadeVendida)
                        vendido = Venda(Produtos(item.produto.nome, item.produto.preco, item.produto.categoria),
                                        vendedor,
                                        comprador,
                                        float(totalVendido))
                        DaoVenda.salvar(vendido)
                        print('Venda cadastrada com sucesso. Valor total:', totalVendido)
                else:
                    if item.produto.nome == nomeProduto:
                        print(
                            f'Quantidade de produtos indisponivel, Produto {item.produto.nome} em estoque {item.quantidade}')

            if float(produto_encontrado) >= float(quantidadeVendida):
                # Atualizando a quantidade do produto
                val = float(produto_encontrado) - float(quantidadeVendida)
                # Atualizando o arquivo de estoque
                with open('Estoque.txt', "w") as arq:
                    for item in x:
                        if item.produto.nome == nomeProduto:
                            arq.writelines(
                                item.produto.nome + "|" + item.produto.preco + "|" + item.produto.categoria + "|" + str(
                                    val) + "\n")
                        else:
                            arq.writelines(
                                item.produto.nome + "|" + item.produto.preco + "|" + item.produto.categoria + "|" + str(
                                    item.quantidade) + "\n")
            else:
                print(f'Quantidade de {nomeProduto} é de {produto_encontrado} em nosso Estoque.')
        else:
            print("Produto não encontrado, verifique o nome do produto desejado!")


c = ControllerVenda()

c.cadastrarVenda('Melância', 'Juarez', 'Marcelo', '150')
