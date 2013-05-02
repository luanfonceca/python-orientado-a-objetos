class ItemNaoEncontrado(Exception):
    pass

class Lista(object):
    def __init__(self, nome, itens=[]):
        self.nome = nome
        self.itens = itens

    def __repr__(self):
        return "<Lista: %s>" % self.nome

    def incluir(self, item):
        if type(item) in (list, tuple):
            self.itens.extend(item)
        else:
            self.itens.append(item)
        print self.itens

    def excluir(self, indice):
        try:
            del self.itens[indice]
            print self.itens
        except IndexError:
            raise ItemNaoEncontrado(
                "Indice invalido. Nenhum item encontrado."
            )

    def excluir_todos(self):
        self.itens = []
        print self.itens

    @property
    def qtd_itens(self):
        return len(self.itens)

