class Pessoa:
    def __init__(self, nome):
        self.nome = nome

p = Pessoa('pedro')

print(p.__dict__)