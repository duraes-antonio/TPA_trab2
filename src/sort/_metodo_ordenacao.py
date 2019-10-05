import abc
from typing import TypeVar, Generic, List

from src.util.comparadores import Comparador

T = TypeVar('T')

class MetodoOrdenacao(Generic[T], abc.ABC):

    @staticmethod
    @abc.abstractmethod
    def ordenar(comparador: Comparador[T], lista: List[T]) -> List[T]:
        """
        Realiza ordenação crescente in-place da lista com base no comparador
        :param comparador: Objeto que estabelece a função de comparação p/ os objetos<T>
        :param lista: Coleção de objetos<T> a ser ordenada
        :return: Própria coleção de entrada ordenada
        """
        raise NotImplementedError()