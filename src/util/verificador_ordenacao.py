from typing import List, TypeVar

from src.util.comparador import Comparador

T = TypeVar('T')


def lista_ord_decresc(comparador: Comparador[T], lista: List[T]) -> bool:
	"""
	Verifica se uma determinada lista está ordenada DECrescentemente
	:param comparador: Objeto para realizar comparação entre os elementos
	:param lista: Lista a ser verificada
	:return: True se estiver ordenada descrescentemente; False, senão
	"""
	qtd = len(lista)

	for i in range(qtd - 1):

		# Se o elemento atual for menor do que o seguinte, a lista não está ord. decrescentemente
		if (comparador.compararCom(lista[i], lista[i + 1]) < 0):
			return False

	return True


def lista_ord_cresc(comparador: Comparador[T], lista: List[T]) -> bool:
	"""
	Verifica se uma determinada lista está ordenada crescentemente
	:param comparador: Objeto para realizar comparação entre os elementos
	:param lista: Lista a ser verificada
	:return: True se estiver ordenada crescentemente; False, senão
	"""
	qtd = len(lista)

	for i in range(qtd - 1):

		# Se o elemento atual for menor do que o seguinte, a lista não
		# está ordenada decrescentemente
		if (comparador.compararCom(lista[i], lista[i + 1]) > 0):
			return False

	return True
