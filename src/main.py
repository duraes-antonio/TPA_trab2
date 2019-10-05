import time
from datetime import datetime

from src.usuario import Usuario, ComparadorUuid
from src.util.verificador_ordenacao import lista_ordenada_decresc, lista_ordenada_cresc


def convert_linha_usuario(separador: str, linha: str, data_fmt: str) -> Usuario:
	params = linha.split(separador)
	usuario: Usuario = Usuario(
		params[0], params[1], params[2], datetime.strptime(params[3], data_fmt),
		float(params[4]), float(params[5]))

	return usuario

def convert_arq_para_usuarios(arq_caminho: str, separador: str, data_fmt: str) -> [Usuario]:
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
	while (linha != None and len(linha.strip()) > 0):
		usuarios.append(convert_linha_usuario(separador, linha, data_fmt))
		linha = arq.readline()

	arq.close()

	return usuarios

# TODO: Implementar comparable
# TODO: Parser de argumentos via CLI
def main(args: [str]):

	arq_path =  'data_10e0.csv'
	usuarios = convert_arq_para_usuarios(arq_path, ',', '%Y-%m-%d')

	# Começar contagem de tempo
	start = time.time()

	# Chamar algorítimo de ordenação

	# Finalizar contagem de tempo
	end = time.time()


	# TODO: Escrever resultado em um CSV no caminho de saída recebido via CLI

	# Imprimir a duração e o número de registros ordenados

	print("ORD DESC:\t", lista_ordenada_decresc(ComparadorUuid, usuarios))
	print("ORD CRESC:\t", lista_ordenada_cresc(ComparadorUuid, usuarios))

	print("\nDuração: %f - Qtd. Registros: %d" %(end - start, len(usuarios)))

	return 0

main([])