#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime

from util.comparador import Comparador


class Pessoa():

	def __init__(
			self, email: str, genero: str, id: str, data_nasc: datetime,
			altura: float, peso: float):
		self.email = email
		self.genero = genero
		self.uid = id
		self.data_nasc = data_nasc
		self.altura = altura
		self.peso = peso

	def clone(self):
		return Pessoa(
			self.email, self.genero, self.uid, self.data_nasc, self.altura,
			self.peso
		)

	def __str__(self) -> str:
		return f"{self.email},{self.genero},{self.uid},{self.data_nasc.date()},{self.altura},{self.peso}"

	def __repr__(self) -> str:
		return str(self)

	def __eq__(self, outro):
		return self.uid == outro.uid

	def __lt__(self, outro):
		return self.uid < outro.uid

	def __le__(self, outro):
		return self.uid <= outro.uid

	def __gt__(self, outro):
		return self.uid > outro.uid

	def __ge__(self, outro):
		return self.uid >= outro.uid


class ComparadorUid(Comparador[Pessoa]):

	@staticmethod
	def compararCom(pessoa_1: Pessoa, pessoa_2: Pessoa) -> int:

		result: int = 0

		if (pessoa_1.uid > pessoa_2.uid):
			result = 1

		elif (pessoa_1.uid < pessoa_2.uid):
			result = -1

		return result


class ComparadorEmail(Comparador[Pessoa]):

	@staticmethod
	def compararCom(pessoa_1: Pessoa, pessoa_2: Pessoa) -> int:

		result: int = 0

		if (pessoa_1.email > pessoa_2.email):
			result = 1

		elif (pessoa_1.email < pessoa_2.email):
			result = -1

		return result


class ComparadorDataNasc(Comparador[Pessoa]):

	@staticmethod
	def compararCom(pessoa_1: Pessoa, pessoa_2: Pessoa) -> int:

		result: int = 0

		if (pessoa_1.data_nasc > pessoa_2.data_nasc):
			result = 1

		elif (pessoa_1.data_nasc < pessoa_2.data_nasc):
			result = -1

		return result


class ComparadorAltura(Comparador[Pessoa]):

	@staticmethod
	def compararCom(pessoa_1: Pessoa, pessoa_2: Pessoa) -> int:

		result: int = 0

		if (pessoa_1.altura > pessoa_2.altura):
			result = 1

		elif (pessoa_1.altura < pessoa_2.altura):
			result = -1

		return result


class ComparadorPeso(Comparador[Pessoa]):

	@staticmethod
	def compararCom(pessoa_1: Pessoa, pessoa_2: Pessoa) -> int:

		result: int = 0

		if (pessoa_1.peso > pessoa_2.peso):
			result = 1

		elif (pessoa_1.peso < pessoa_2.peso):
			result = -1

		return result
