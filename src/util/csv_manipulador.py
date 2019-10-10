#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from typing import List

from pessoa import Pessoa


def convert_linha_pessoa(sep: str, linha: str, data_fmt: str) -> Pessoa:
    """
    Converte uma linha do CSV de entrada em um objeto Usuário
    :param linha: Linha a ser convertida, lida do csv
    :param sep: Caractere ou expressão delimitadora (',', ';', ...)
    :param data_fmt: Formato da data (exemplo: '%d/%m/%Y', ver Python Datetime)
    :return: Usuário instanciado com os atributos preenchidos
    """
    params = linha.split(sep)
    pessoa: Pessoa = Pessoa(
        params[0], params[1], params[2], datetime.strptime(params[3], data_fmt),
        float(params[4]), float(params[5]))

    return pessoa


def convert_arq_pessoas(
		arq_caminho: str, separador: str, data_fmt: str) -> List[Pessoa]:
    """
    Converte o arquivo de entrada (CSV) em uma lista de usuários
    :param arq_caminho: Caminho do arquivo CSV a ser lido
    :param separador: Caractere ou expressão delimitadora (',', ';', ...)
    :param data_fmt: Formato da data (exemplo: '%d/%m/%Y', ver Python Datetime)
    :return: Lista de usuários preenchida
    """
    pessoas: [Pessoa] = []
    arq = open(arq_caminho, 'r', encoding='utf-8')

    # Leia e descarte a primeira linha
    arq.readline()

    linha = arq.readline()

    # Enquanto houver conteúdo a ser lido
    while linha is not None and len(linha.strip()) > 0:
	    pessoas.append(convert_linha_pessoa(separador, linha, data_fmt))
        linha = arq.readline()

    arq.close()

    return pessoas


def convert_pessoas_arq(path_saida: str, pessoas: List[Pessoa]):

    with open(path_saida, 'w') as arq:
        arq.write('email,gender,uid,birthdate,height,weight\n')

        for i in range(len(pessoas) - 1):
	        arq.write(str(pessoas[i]) + '\n')

        arq.write(str(pessoas[-1]))

    return
