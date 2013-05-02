class Encapsulada(object):
    def __init__(self, privado):
        self._privado = privado

    @property
    def privado(self):
        return self._privado

    @privado.setter
    def privado(self, value):
        self._privado = value
