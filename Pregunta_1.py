import random


def CrearLista():
    miLista = []

    for i in range(0, 10):
        miLista.append(random.randint(0, 40))
    print(miLista)
    return miLista


def NumerosNoRepetidos(conjunto):
    NoRepetidos = []

    for numero in conjunto:
        if conjunto.count(numero) == 1:
            NoRepetidos.append(numero)
    return NoRepetidos


ListaDeAleatorios = CrearLista()
print("lista de numeros aleatorios: {}".format(ListaDeAleatorios))

ListaDeAleatoriosNoRepetidos = NumerosNoRepetidos(ListaDeAleatorios)
print("Lista de aleatorios no repetidos: {}".format(
    ListaDeAleatoriosNoRepetidos))
