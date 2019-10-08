#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
from datetime import datetime

from sort.metodos_ordenacao import *
from sort.verificador_ordenacao import lista_ord_cresc
from usuario import Usuario, ComparadorUuid
from util.csv_manipulador import convert_arq_usuarios, convert_usuarios_arq


# TODO: Parser de argumentos via CLI
def parse_args():
	return


def main():
	path_dados = "../dados/"
	arq_paths = [path_dados + filename for root, dirs, files in os.walk(path_dados)
				 for filename in files]

	algs: List[MetodoOrdenacao] = [
		IntroSort, QuickSort, TimSort, MergeSort, HeapSort, InsertionSort,
		SelectionSort]

	# Para cada algoritmo na lista de métodos de ordenação
	for alg in algs:
		alg_ord: MetodoOrdenacao = alg

		# Para cada caminho de arquivo na lista de arquivos
		for arq_path in arq_paths:
			usuarios: List[Usuario] = convert_arq_usuarios(arq_path, ',', '%Y-%m-%d')

			nome = f'{alg_ord.id}_{len(usuarios)}.csv'
			arq_saida = open(nome, 'w')
			arq_saida.write(f'i exec;duracao (ms);hora início;hora fim\n')

			# Realize 10 execuções para cada caso
			for i in range(1, 11):

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

				convert_usuarios_arq(f"arq_ordenado_{alg_ord.id}_{len(usuarios)}_{i}.csv", lista)

				# Imprimir a duração e o número de registros ordenados
				print("ORD. CRESC.:", lista_ord_cresc(ComparadorUuid, lista))
				print('\n%s\t %d\t %.6f' % (alg_ord.id, len(lista), crono_dif))

			arq_saida.close()


	return 0


main()
