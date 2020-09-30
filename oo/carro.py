"""
    Você deve criar ma classe carro que vai possuir dois atributos compostos por outras classes:

    1) Motor
    2) Direção

    O Motor tera a responsavilidade de controlar a velocidade.
    Ele oferece os seguintes atributos:
    1) Atributo de dados velocidade
    2) Metodo acelerar que devera incrementar a velocidade
    3) Metodo decrementar em 2 unidades

    A direção terá a responsabilidade de controlar a direcao. Ela oferecera os seguintes atributos:
    1) Valor de direçao com valores possiveis: Norte, Sul, Leste, Oeste
    2) Metodo girar_a_direita
    2) Metodo girar_a_esqueda

        N
    O        L
        S

    Exemplo:
    >>> # Testando o motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> # Testando Direcao
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'

    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Oeste'
"""


class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        if self.velocidade < 2:
            self.velocidade = 0
        else:
            self.velocidade -= 2


class Direcao:
    direcoes = ('Oeste', 'Norte', 'Leste', 'Sul')

    def __init__(self):
        self.index = 1
        self.valor = self.direcoes[self.index]

    def girar_a_direita(self):
        self.index += 1
        self.index = 0 if self.index >= 4 else self.index

        self.valor = self.direcoes[self.index]

    def girar_a_esquerda(self):
        self.index -= 1
        self.index = 3 if self.index < 0 else self.index

        self.valor = self.direcoes[self.index]


class Carro:
    def __init__(self, direcao, motor):
        self.direcao = direcao
        self.motor = motor

    def calcular_velocidade(self):
        return self.motor.velocidade

    def calcular_direcao(self):
        return self.direcao.valor

    def acelerar(self):
        return self.motor.acelerar()

    def frear(self):
        return self.motor.frear()

    def girar_a_direita(self):
        return self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        return self.direcao.girar_a_esquerda()
