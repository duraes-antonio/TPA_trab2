import time

from src.sort.metodos_ordenacao import *
from src.sort.verificador_ordenacao import lista_ord_decresc, lista_ord_cresc
from src.usuario import Usuario, ComparadorUuid
from src.util.csv_manipulador import convert_arq_usuarios


# TODO: Parser de argumentos via CLI
def parse_args():
	return


def main():
	arq_path = '../dados/data_10e3.csv'
	usuarios: List[Usuario] = convert_arq_usuarios(arq_path, ',', '%Y-%m-%d')

	algs: List([MetodoOrdenacao], List[Usuario]) = [
		(HeapSort(), usuarios[:]),
		(InsertionSort(), usuarios[:]),
		(MergeSort(), usuarios[:]),
		(QuickSort(), usuarios[:]),
		(SelectionSort(), usuarios[:]),
		(TimSort(), usuarios[:])
	]

	for alg_ord, lista in algs:

		# Começar contagem de tempo
		crono_ini = time.time()

		# Chamar algorítimo de ordenação
		fun_ord: MetodoOrdenacao = alg_ord
		nova: List[Usuario] = fun_ord.ordenar(ComparadorUuid, lista)

		# Finalizar contagem de tempo
		crono_fim = time.time()

		crono_dif = crono_fim - crono_ini

		print("\nORD DESC:\t", lista_ord_decresc(ComparadorUuid, nova))
		print("ORD CRESC:\t", lista_ord_cresc(ComparadorUuid, nova))

		# TODO: Escrever resultado em um CSV no caminho de saída recebido via CLI

		# Imprimir a duração e o número de registros ordenados
		print('\n%s\t %d\t %.10f' % (fun_ord.id, len(lista), crono_dif))


	return 0


main()
