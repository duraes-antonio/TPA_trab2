from datetime import datetime
from typing import List

from src.usuario import Usuario


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


def convert_arq_usuarios(
		arq_caminho: str, separador: str, data_fmt: str) -> List[Usuario]:
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