class Pessoa:
    # Atributo default/classe
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        # Atributos de instancia
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return 'Olá '+self.nome


if __name__ == '__main__':
    geison = Pessoa(nome='Geison')

   # Atributo complexo
    luiz = Pessoa(geison, nome='Luiz')
    print(luiz.cumprimentar())
    for filho in luiz.filhos:
        print(filho.nome)

    # Atributo dinamico
    luiz.sobrenome = 'Nervo'
    del luiz.filhos
    print(luiz.__dict__)
    print(geison.__dict__)

    luiz.olhos=3
    Pessoa.olhos=1
    print(Pessoa.olhos)
    print(luiz.olhos)
    print(geison.olhos)
