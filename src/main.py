#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import time
from os import path
from typing import Dict

# Importação de funções e classes customizadas
from pessoa import Pessoa, ComparadorUuid
from sort.metodos_ordenacao import *
from util.csv_manipulador import convert_arq_pessoas, convert_pessoas_arq

dic_prefix_alg: Dict[str, MetodoOrdenacao] = {
	'hea': HeapSort, 'ins': InsertionSort, 'int': IntroSort,
	'mer': MergeSort, 'qui': QuickSort, 'sel': SelectionSort,
	'tim': TimSort
}


def ler_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser()

	def file_valid(caminho: str):

		extensao = path.basename(caminho).split(".")[-1]
		if not path.exists(caminho):
			raise FileNotFoundError(
				f"O caminho recebido não existe! Path: '{caminho}'."
			)

		elif not path.isfile(caminho):
			raise FileNotFoundError(
				f"O caminho deve pertencer a um arquivo! Path: {caminho}"
			)

		elif 'csv' not in path.basename(caminho).lower():
			raise TypeError(
				f"O tipo do arquivo de entrada deve ser CSV! Recebido: {extensao}"
			)

		return caminho

	def dir_valid(caminho: str):

		nome_dir = path.dirname(caminho)
		extensao = path.basename(caminho).split(".")[-1]

		if not path.exists(nome_dir):
			raise FileNotFoundError(
				f"O diretório de saída não existe! Path: '{caminho}'."
			)

		elif 'csv' not in path.basename(caminho).lower():
			raise TypeError(
				f"O tipo do arquivo de saída deve ser CSV! Recebido: {extensao}"
			)

		return caminho

	parser.add_argument(
		"--alg", required=False,
		choices=tuple(dic_prefix_alg.keys()),
		help="Prefixo dos algorítimos a serem executados"
	)

	parser.add_argument(
		"-i", required=True, type=file_valid,
		help="Caminho e nome do arquivo CSV de entrada"
	)

	parser.add_argument(
		"-o", required=True, type=dir_valid,
		help="Caminho e nome do arquivo ordenado de saída"
	)

	return parser.parse_args()


def main():
	args = ler_args()

	algorit = args.alg
	path_dados = args.i
	path_saida = args.o

	metodos_ord: List[MetodoOrdenacao]

	# TODO (duraes-antonio): validar opção escolhida
	if algorit is not None:
		metodos_ord = [dic_prefix_alg[algorit]]

	else:
		metodos_ord = [dic_prefix_alg[key] for key in dic_prefix_alg]

	if (len(metodos_ord) > 1):
		nome_dir_saida = path.dirname(path_saida)
		nome_arq_saida = path.basename(path_saida)
		path_saida = path.join(nome_dir_saida, '{}_' + nome_arq_saida)

	# Para cada algoritmo na lista de métodos de ordenação
	for alg_ord in metodos_ord:

		pessoas: List[Pessoa] = convert_arq_pessoas(path_dados, ',', '%Y-%m-%d')

		# Copie a lista de entrada
		lista = pessoas[:]

		# Começar contagem de tempo
		crono_ini = time.time()

		# Chamar algorítimo de ordenação
		alg_ord.ordenar(ComparadorUuid, lista)

		# Finalizar contagem de tempo
		crono_fim = time.time()

		crono_dif = crono_fim - crono_ini
		crono_dif *= 1000

		if (len(metodos_ord) > 1):
			convert_pessoas_arq(path_saida.format(alg_ord.id), lista)

		else:
			convert_pessoas_arq(path_saida, lista)

		# Imprimir a duração e o número de registros ordenados
		print('\n%s\t %d\t %.6f' % (alg_ord.id, len(lista), crono_dif))

	return 0


main()
