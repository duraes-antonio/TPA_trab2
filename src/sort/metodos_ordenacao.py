import abc
from typing import TypeVar, Generic, List, Optional

from src.util.comparador import Comparador

T = TypeVar('T')


class MetodoOrdenacao(Generic[T], abc.ABC):

	@property
	def id(self):
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


class HeapSort(MetodoOrdenacao):

	@property
	def id(self):
		return 'heapsort'

	@staticmethod
	def ordenar(comparador: Comparador[T], lista: List[T]) -> List[T]:
		return HeapSort.__heapsort(lista, comparador)

	@staticmethod
	def __heapify(
			lista: List[T], i: int, cmp: Comparador[T], tam: int):

		esq = 2 * i + 1
		dir = esq + 1
		maior = -1

		# Se houver um item à esquerda do elemento de índice i
		# E esse item for maior que o atual elemento de índice i,
		# Então: Atualize o índice do maior elemento
		if esq < tam and cmp.compararCom(lista[esq], lista[i]) > 0:
			maior = esq

		else:
			maior = i

		# Se houver um item à direita do elemento de índice i
		# E esse item for maior que o atual elemento máximo, atualize o
		# índice do maior elemento
		if (dir < tam and cmp.compararCom(lista[dir], lista[maior]) > 0):
			maior = dir

		# Se o maior elemento não for o de índice i, troque o item de índice
		# i com o elemento de maior valor
		if maior != i:
			lista[i], lista[maior] = lista[maior], lista[i]
			HeapSort.__heapify(lista, maior, cmp, tam)

	@staticmethod
	def __heapsort(lista: List[T], comparador: Comparador[T]) -> List[T]:

		# Método baseado no capítulo 6.3 do livro 'Algoritmos' (T. H. Cormen)
		tam = len(lista)

		for i in range(tam // 2, -1, -1):
			HeapSort.__heapify(lista, i, comparador, tam)

		# Percorra a lista da direita p/ esquerda, do último índice até o
		# segundo. Com o heapify sendo feito de 0 até 'i', e 'i'
		# decrementando em 1, simula-se a remoção de um nó a cada iteração.
		for i in range(tam - 1, 0, -1):
			lista[i], lista[0] = lista[0], lista[i]
			HeapSort.__heapify(lista, 0, comparador, i)

		return lista


class InsertionSort(MetodoOrdenacao):

	@property
	def id(self):
		return 'insertsort'

	@staticmethod
	def ordenar(
			comparador: Comparador[T], lista: List[T],
			inic: Optional[int] = 0, fim: Optional[int] = None) -> List[T]:
		return InsertionSort.__insertion_sort(lista, comparador, inic, fim)

	@staticmethod
	def __insertion_sort(
			lista: List[T], comparador: Comparador[T],
			inic: Optional[int] = 0, fim: Optional[int] = None) -> List[T]:

		if fim is None:
			fim = len(lista)

		else:
			fim += 1

		# Para cada índice da posição inicial até o (tamanho - 1)
		for i in range(inic, fim - 1):

			item_atual = lista[i + 1]
			j = i

			while j >= inic and comparador.compararCom(lista[j], item_atual) > 0:
				# Troque a posição do item atual com a posição do item anterior
				lista[j + 1] = lista[j]
				j -= 1

			lista[j + 1] = item_atual

		return lista


class MergeSort(MetodoOrdenacao):

	@property
	def id(self):
		return 'merge_sort'

	@staticmethod
	def ordenar(comparador: Comparador[T], lista: List[T]) -> List[T]:
		MergeSort.__merge_sort(lista, comparador, 0, len(lista) - 1)
		return lista

	# l significa esquerda e r significa direita 
	@staticmethod
	def __merge_sort(lista_original: List[T], cmp: Comparador[T], l: int, r: int):
		# Baseado na seção 2.3.1 do livro 'Algoritmos' (T. H. Cormen)
		# p.36 - 38
		if l < r:
			# separando a lista no meio
			m = (l + (r - 1)) // 2

			# separando a lista
			MergeSort.__merge_sort(lista_original, cmp, l, m)
			MergeSort.__merge_sort(lista_original, cmp, m + 1, r)
			merge(lista_original, cmp, l, m, r)


class QuickSort(MetodoOrdenacao):

	@property
	def id(self):
		return 'quicksort'

	@staticmethod
	def ordenar(comparador: Comparador[T], lista: List[T]) -> List[T]:
		return QuickSort.__quicksort(lista, comparador, 0, len(lista) - 1)

	@staticmethod
	def __quicksort(
			lista: List[T], cmp: Comparador[T], l: int, r: int) -> List[T]:

		if l < r:
			q = QuickSort.__particao(lista, cmp, l, r)
			QuickSort.__quicksort(lista, cmp, l, q - 1)
			QuickSort.__quicksort(lista, cmp, q + 1, r)

		return lista

	@staticmethod
	def __particao(
			lista: List[T], cmp: Comparador[T], i_esq: int, i_dir: int) -> int:

		pivo = lista[i_dir]
		i = i_esq - 1

		for ind in range(i_esq, i_dir):

			# Se o item atual for menor/igual que o pivô, troque-o c/ o pivô
			if cmp.compararCom(lista[ind], pivo) <= 0:
				i += 1
				lista[i], lista[ind] = lista[ind], lista[i]

		lista[i + 1], lista[i_dir] = lista[i_dir], lista[i + 1]

		return i + 1


class SelectionSort(MetodoOrdenacao):

	@property
	def id(self):
		return 'selectsort'

	@staticmethod
	def ordenar(
			comparador: Comparador[T], lista: List[T],
			inic: Optional[int] = None, fim: Optional[int] = None) -> List[T]:
		return SelectionSort.__selection_sort(comparador, lista, inic, fim)

	@staticmethod
	def __selection_sort(
			comparador: Comparador[T], lista: List[T],
			inic: Optional[int] = None, fim: Optional[int] = None) -> List[T]:

		def min_indice(lista: List[T], ind_inic: int, ind_fim: int) -> int:
			"""
			Busca o índice do elemento de menor valor em uma lista
			:param lista: Lista de elementos de mesmo tipo
			:param ind_inic: Índice do primeiro elemento a ser verificado
			:param ind_fim: Índice do último elemento considerado
			:return: Inteiro com índice do menor elemento
			"""
			indice_min = ind_inic

			# Busque o índice do menor elemento do índice de início ao de fim
			for i in range(ind_inic + 1, ind_fim + 1):

				if comparador.compararCom(lista[indice_min], lista[i]) > 0:
					indice_min = i

			return indice_min

		if inic is None:
			inic = 0

		if fim is None:
			fim = len(lista)

		else:
			fim += 1

		# Para cada índice do ínicio até o fim da lista
		for i in range(inic, fim):
			# Busque o índice do menor elemento da lista, começando de i até
			# o último índice da lista
			ind_min = min_indice(lista, i, fim - 1)

			# Troque a posição do item atual com a posição do menor item
			lista[i], lista[ind_min] = lista[ind_min], lista[i]

		return lista


# 2 Métodos extras
class TimSort(MetodoOrdenacao):
	__tam_run = 16

	@property
	def id(self):
		return 'timsort'

	@staticmethod
	def ordenar(comparador: Comparador[T], lista: List[T]) -> List[T]:
		return TimSort.__tim_sort(lista, comparador)

	@staticmethod
	def __tim_sort(lista: List[T], cmp: Comparador) -> List[T]:

		tam_lista = len(lista)
		ult_ind = tam_lista - 1

		# Ordene cada run de acordo com o tamanho pré-estabelecido
		for i in range(0, tam_lista, TimSort.__tam_run):
			run_fim = i + TimSort.__tam_run - 1
			InsertionSort.ordenar(cmp, lista, i, min(run_fim, ult_ind))

		itens_ordenados = TimSort.__tam_run

		# Enquanto houverem elementos a serem ordenados
		while itens_ordenados < tam_lista:

			# Percorra os índices da lista, de 0 até seu último índice.
			# A cada iteração, incremente i em 2 vezes (devido merge com duas
			# sublistas) a qtd de itens ordenados
			for ind_esq in range(0, tam_lista, 2 * itens_ordenados):
				# Calcule os índices de esquerda, meio e direita p/ o merge
				ind_meio = min((ind_esq - 1 + itens_ordenados), ult_ind)
				ind_dir = min((ind_esq - 1 + 2 * itens_ordenados), ult_ind)
				merge(lista, cmp, ind_esq, ind_meio, ind_dir)

			# O número de itens ordenados é o dobro da quantidade anterior,
			# já que duas sublistas (runs) foram mescladas
			itens_ordenados *= 2

		return lista


def merge(
		lista: List[T], cmp: Comparador[T], i_esq: int, i_meio: int,
		i_dir: int):
	n1 = i_meio - i_esq + 1
	n2 = i_dir - i_meio

	# Criação de lista somente com a referência de cada item, não há duplicatas
	# de usuários!
	sublista_esq = [lista[i_esq + i] for i in range(n1)]
	sublista_dir = [lista[i_meio + i + 1] for i in range(n2)]

	i = j = 0

	# No livro o pseudo código itera do início ('p') ao fim ('r').
	# Para EVITAR operações denecessárias (comparações e checagem de fim
	# de lista após alguma sublista findar), vamos interromper as
	# comparações assim qualquer sublista terminar.
	while i < n1 and j < n2:

		# Se o item atual da sublista da esquerda for menor ou igual ao
		# item da sublista da direita, faça a lista ordenada receber o item
		# da sublista da esquerda e avance o índice da sublista esquerda.
		if cmp.compararCom(sublista_esq[i], sublista_dir[j]) < 1:
			lista[i_esq] = sublista_esq[i]
			i += 1

		# Se não, insira o item da sublista direita e aponte para o próx item
		else:
			lista[i_esq] = sublista_dir[j]
			j += 1

		i_esq += 1

	# copiando os elementos restantes da lista_esquerda[], caso exista
	for it in range(i, n1):
		lista[i_esq] = sublista_esq[it]
		i_esq += 1

	# copiando os elementos restantes da lista_direira[], caso exista
	for it in range(j, n2):
		lista[i_esq] = sublista_dir[it]
		i_esq += 1
