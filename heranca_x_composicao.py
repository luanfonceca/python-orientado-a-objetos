class Pessoa(object):
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print "%s diz: Ola!" % self.nome

class Crianca(Pessoa):
    def __init__(self, nome, idade):
        super(Crianca, self).__init__(nome)
        self.idade = idade

    def falar(self):
        super(Crianca, self).falar()
        print "Eu tenho %s anos." % self.idade

class Carro(object):
    def __init__(self, nome, dono):
        self.nome = nome
        self.dono = Pessoa(dono)
