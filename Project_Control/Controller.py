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


#c = ControllerEstoque()
#c.cadastrarProduto('Pepino','12.99','Legumes','15')