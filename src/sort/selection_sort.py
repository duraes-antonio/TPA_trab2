from typing import TypeVar, List

from src.sort._metodo_ordenacao import MetodoOrdenacao
from src.util.comparadores import Comparador

T = TypeVar('T')




class SelectionSort(MetodoOrdenacao):

    @staticmethod
    def ordenar(comparador: Comparador[T], lista: List[T]):
        return SelectionSort.__selection_sort(comparador, lista)

    @staticmethod
    def __selection_sort(comparador: Comparador[T], lista: List[T]):

        def min_indice(lista: List[T]) -> int:
            ind_min = 0
            tam = len(lista)

            for i in range(1, tam):

                if (comparador.compararCom(lista[ind_min], lista[i]) < 0):
                    ind_min = i

            return ind_min

        # TODO: Finalizar método
        def trocar(lista: List[T], ind_orig: int, ind_dest: int):
            temp = lista[ind_orig]

        # TODO: Finalizar