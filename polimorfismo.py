class Animal(object):
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        raise NotImplementedError(
            "Subclasses precisam implementar o metodo abstrato"
        )

class Gato(Animal):
    def falar(self):
        return '%s: Meow! Meow!' % self.nome

class Cachorro(Animal):
    def falar(self):
        return '%s: Woof! Woof!' % self.nome
