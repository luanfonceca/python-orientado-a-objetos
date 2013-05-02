class Pessoa(object):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def informacoes(self):
        print "Nome: %s\nIdade: %s" % (
            self.nome, self.idade
        )
