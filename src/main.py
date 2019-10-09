#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import argparse
from datetime import datetime
from os import path
from pathlib import Path

from sort.metodos_ordenacao import *
from usuario import Usuario, ComparadorUuid
from util.csv_manipulador import convert_arq_usuarios, convert_usuarios_arq


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

	parser.add_argument(
		"--alg", required=False,
		choices=('heap', 'insert', 'intro', 'merge', 'quick', 'select', 'tim'),
		help="Prefixo dos algorítimos a serem executados"
	)

	parser.add_argument(
		"-i", required=True, type=file_valid,
		help="Caminho e nome do arquivo CSV de entrada"
	)

	parser.add_argument(
		"-o", required=True, type=Path,
		help="Caminho e nome do arquivo ordenado de saída"
	)

	return parser.parse_args()


def main():
	args = ler_args()

	algorit = args.alg
	path_dados = args.i
	path_saida = args.o

	# TODO (duraes-antonio): encapsular + comentar
	dic_algs = {
		'heap': HeapSort, 'insert': InsertionSort, 'intro': IntroSort,
		'merge': MergeSort, 'quick': QuickSort, 'select': SelectionSort,
		'tim': TimSort
	}

	metodos_ord: List[MetodoOrdenacao]

	# TODO (duraes-antonio): validar opção escolhida
	if algorit is not None:
		metodos_ord = [dic_algs[algorit]]

	else:
		metodos_ord = [dic_algs[key] for key in dic_algs]

	# Para cada algoritmo na lista de métodos de ordenação
	for alg_ord in metodos_ord:

		usuarios: List[Usuario] = convert_arq_usuarios(path_dados, ',', '%Y-%m-%d')

		nome = f'{alg_ord.id}_{len(usuarios)}.csv'
		arq_saida = open(nome, 'w')
		arq_saida.write(f'i exec;duracao (ms);hora início;hora fim\n')

		# Realize 10 execuções para cada caso
		for i in range(1):
			# Copie a lista de entrada
			lista = usuarios[:]

			# Começar contagem de tempo
			data_ini = datetime.now()
			crono_ini = time.time()

			# Chamar algorítimo de ordenação
			alg_ord.ordenar(ComparadorUuid, lista)

			# Finalizar contagem de tempo
			crono_fim = time.time()
			data_fim = datetime.now()

			crono_dif = crono_fim - crono_ini
			crono_dif *= 1000
			arq_saida.write(f'{i};{crono_dif};{data_ini};{data_fim}\n')

			# convert_usuarios_arq(f"arq_ordenado_{alg_ord.id}_{len(usuarios)}_{i}.csv", lista)

			# Imprimir a duração e o número de registros ordenados
			print('\n%s\t %d\t %.6f' % (alg_ord.id, len(lista), crono_dif))

		arq_saida.close()

	return 0


main()
