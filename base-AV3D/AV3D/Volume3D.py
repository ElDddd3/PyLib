import math

import Area2D


def volumenCubo(a):
    return a ** 3


def volmenPrisma(a, b, c):
    return a * b * c


def volumenPiramide(Lados, l, Apotema, altura):
    return ((Area2D.areaPoligonoRegular(Lados, l, Apotema)) * altura) / 3


def volumenCilindro(r, altura):
    return (Area2D.areaCirculo(r)) * altura


def volumenCono(r, altura):
    return ((Area2D.areaCirculo(r)) * altura)/3


def volumenEsfera(r):
    return (4*(math.pi*r))/3
