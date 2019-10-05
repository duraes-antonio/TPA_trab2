import time
from datetime import datetime

from src.sort.metodos_ordenacao import *
from src.usuario import Usuario, ComparadorUuid
from src.util.verificador_ordenacao import lista_ord_decresc, lista_ord_cresc


def convert_linha_usuario(sep: str, linha: str, data_fmt: str) -> Usuario:
	"""
	Converte uma linha do CSV de entrada em um objeto Usuário
	:param linha: Linha a ser convertida, lida do csv
	:param sep: Caractere ou expressão delimitadora (',', ';', ...)
	:param data_fmt: Formato da data (exemplo: '%d/%m/%Y', ver Python Datetime)
	:return: Usuário instanciado com os atributos preenchidos
	"""
	params = linha.split(sep)
	usuario: Usuario = Usuario(
		params[0], params[1], params[2], datetime.strptime(params[3], data_fmt),
		float(params[4]), float(params[5]))

	return usuario


def convert_arq_para_usuarios(arq_caminho: str, separador: str, data_fmt: str) -> List[Usuario]:
	"""
	Converte o arquivo de entrada (CSV) em uma lista de usuários
	:param arq_caminho: Caminho do arquivo CSV a ser lido
	:param separador: Caractere ou expressão delimitadora (',', ';', ...)
	:param data_fmt: Formato da data (exemplo: '%d/%m/%Y', ver Python Datetime)
	:return: Lista de usuários preenchida
	"""
	usuarios: [Usuario] = []
	arq = open(arq_caminho, 'r', encoding='utf-8')

	# Leia e descarte a primeira linha
	arq.readline()

	linha = arq.readline()

	# Enquanto houver conteúdo a ser lido
	while linha is not None and len(linha.strip()) > 0:
		usuarios.append(convert_linha_usuario(separador, linha, data_fmt))
		linha = arq.readline()

	arq.close()

	return usuarios


def parse_args():



	return


# TODO: Parser de argumentos via CLI
def main(args: List[str]):
	arq_path = '../dados/data_10e3.csv'
	usuarios: List[Usuario] = convert_arq_para_usuarios(arq_path, ',', '%Y-%m-%d')
	print('-> ARQ LIDO e CONVERTIDO')

	algs: List([MetodoOrdenacao], List[Usuario]) = [(InsertionSort(), usuarios[:50000])]

	for alg_ord, lista in algs:
		# Começar contagem de tempo
		crono_ini = time.time()

		# Chamar algorítimo de ordenação
		fun_ord: MetodoOrdenacao = alg_ord
		nova = fun_ord.ordenar(ComparadorUuid, lista)

		# Finalizar contagem de tempo
		crono_fim = time.time()

		crono_dif = crono_fim - crono_ini

		print("ORD DESC:\t", lista_ord_decresc(ComparadorUuid, nova))
		print("ORD CRESC:\t", lista_ord_cresc(ComparadorUuid, nova))

		# TODO: Escrever resultado em um CSV no caminho de saída recebido via CLI

		# Imprimir a duração e o número de registros ordenados
		print('\n%s\t %d\t %.10f' % (fun_ord.identificador, len(lista), crono_dif))

	return 0


main([])
