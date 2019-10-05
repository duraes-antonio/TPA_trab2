from typing import List, TypeVar

from src.util.comparadores import Comparador

T = TypeVar('T')

def lista_ordenada_decresc(comparador: Comparador[T], lista: List[T]) -> bool:
    qtd = len(lista)

    for i in range(qtd - 1):

        # Se o elemento atual for menor do que o seguinte, a lista não está ord. decrescentemente
        if(comparador.compararCom(lista[i], lista[i+1]) < 0):
            return False

    return True


def lista_ordenada_cresc(comparador: Comparador[T], lista: List[T]) -> bool:
    qtd = len(lista)

    for i in range(qtd - 1):

        # Se o elemento atual for menor do que o seguinte, a lista não está ord. decrescentemente
        if (comparador.compararCom(lista[i], lista[i + 1]) > 0):
            return False

    return True
