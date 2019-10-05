import abc
from typing import TypeVar, Generic

T = TypeVar('T')

class Comparador(Generic[T], abc.ABC):

    @staticmethod
    @abc.abstractmethod
    def compararCom(objeto1: T, objeto2: T) -> int:
        """
        Compara dois objetos de mesmo tipo de acordo com um atributo ou conjunto.
        :param objeto1: Primeiro objeto (seus atributos são comparados com o segundo)
        :param objeto2: Segundo objeto a ser comparado
        :return: 1 (se o 1º maior que o 2º), -1 (2ª maior que o 1º) e 0 (quando iguais)
        """
        raise NotImplementedError()