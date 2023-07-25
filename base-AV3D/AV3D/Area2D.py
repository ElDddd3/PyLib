import math


def areaTriangulo(Base, Altura):
    return Base * Altura / 2


def areaCudrado(Ml):
    return Ml ** 2


def areaRectangulo(Ancho, Alto):
    return Ancho * Alto


def areaRombo(D, d):
    return D * d / 2


def areaRomboide(D, d):
    return D * d


def areaTrapecio(B, b, Altura):
    return (Altura * (B + b)) / 2


def areaCirculo(radio):
    return math.pi * (radio ** 2)


def areaPoligonoRegular(Lados, l, Apotema):
    return ((Lados * l) * Apotema)/2

