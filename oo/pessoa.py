class Pessoa:
    # Atributo default/classe
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        # Atributos de instancia
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    # Metodo de instancia
    def cumprimentar(self):
        return 'Olá ' + self.nome

    # Metodo de classe (Nao depende da classe)
    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    pass


if __name__ == '__main__':
    geison = Pessoa(nome='Geison')

    # Atributo complexo
    luiz = Homem(geison, nome='Luiz')
    print(luiz.cumprimentar())
    for filho in luiz.filhos:
        print(filho.nome)

    # Atributo dinamico
    luiz.sobrenome = 'Nervo'
    del luiz.filhos
    print(luiz.__dict__)
    print(geison.__dict__)

    luiz.olhos = 3
    Pessoa.olhos = 1
    print(Pessoa.olhos)
    print(luiz.olhos)
    print(geison.olhos)
    print(Pessoa.nome_e_atributos_de_classe(), luiz.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(luiz, Pessoa))
