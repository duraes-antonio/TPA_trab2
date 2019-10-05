import abc
from typing import TypeVar, Generic, List

from src.util.comparador import Comparador

T = TypeVar('T')


class MetodoOrdenacao(Generic[T], abc.ABC):

	@property
	def identificador(self):
		return None

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


# TODO: Implementar
class HeapSort(MetodoOrdenacao):
	pass


class InsertionSort(MetodoOrdenacao):

	@property
	def identificador(self):
		return 'insertsort'

	@staticmethod
	def ordenar(comparador: Comparador[T], lista: List[T]) -> List[T]:
		return InsertionSort.__insertion_sort(comparador, lista)

	@staticmethod
	def __insertion_sort(comparador: Comparador[T], lista: List[T]) -> List[T]:

		tam = len(lista)

		# Para cada índice de 0 até o (tamanho - 1)
		for i in range(tam - 1):

			item_atual = lista[i + 1]
			j = i

			while j >= 0 and comparador.compararCom(lista[j], item_atual) > 0:
				# Troque a posição do item atual com a posição do item anterior
				lista[j + 1] = lista[j]
				j -= 1

			lista[j + 1] = item_atual

		return lista


# TODO: Implementar
class MergeSort(MetodoOrdenacao):
	pass


# TODO: Implementar
class QuickSort(MetodoOrdenacao):
	pass


class SelectionSort(MetodoOrdenacao):

	@property
	def identificador(self):
		return 'selectsort'

	@staticmethod
	def ordenar(comparador: Comparador[T], lista: List[T]) -> List[T]:
		return SelectionSort.__selection_sort(comparador, lista)

	@staticmethod
	def __selection_sort(comparador: Comparador[T], lista: List[T]) -> List[T]:

		def min_indice(lista: List[T], ind_inic: int, ind_fim: int) -> int:
			"""
            Busca o índice do elemento de menor valor em uma lista

            :param lista: Lista de elementos de mesmo tipo
            :param ind_inic: Índice do primeiro elemento a ser verificado
            :param ind_fim: Índice do último elemento considerado

            :return: Inteiro com índice do menor elemento
            """
			ind_min = ind_inic

			# Busque o índice do menor elemento do índice de início ao de fim
			for i in range(ind_inic, ind_fim + 1):

				if (comparador.compararCom(lista[ind_min], lista[i]) < 0):
					ind_min = i

			return ind_min

		tam = len(lista)

		# Para cada índice de 0 até o (tamanho - 1)
		for i in range(tam):
			# Busque o índice do menor elemento da lista, começando de i até
			# o último índice da lista
			ind_min = min_indice(lista, i, tam - 1)

			# Troque a posição do item atual com a posição do menor item
			lista[i], lista[ind_min] = lista[ind_min], lista[i]

		return lista


