class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return 'Olá '+self.nome


if __name__ == '__main__':
    geison = Pessoa(nome='Geison')
    luiz = Pessoa(geison, nome='Luiz')
    # print(p.cumprimentar())

    print(luiz.cumprimentar())
    for filho in luiz.filhos:
        print(filho.nome)

    luiz.sobrenome = 'Nervo'
    del luiz.filhos
    print(luiz.__dict__)
    print(geison.__dict__)
