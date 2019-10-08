from datetime import datetime

from src.util.comparador import Comparador


class Usuario():

	def __init__(
			self, email: str, genero: str, id: str, data_nasc: datetime,
			altura: float, peso: float):
		self.email = email
		self.genero = genero
		self.uuid = id
		self.data_nasc = data_nasc
		self.altura = altura
		self.peso = peso

	def clone(self):
		return Usuario(
			self.email, self.genero, self.uuid, self.data_nasc, self.altura,
			self.peso
		)

	def __str__(self) -> str:
		return f"{self.email},{self.genero},{self.uuid},{self.data_nasc},{self.altura},{self.peso}"

	def __repr__(self) -> str:
		return str(self)

	def __eq__(self, outro):
		return self.uuid == outro.uuid

	def __lt__(self, outro):
		return self.uuid < outro.uuid

	def __le__(self, outro):
		return self.uuid <= outro.uuid

	def __gt__(self, outro):
		return self.uuid > outro.uuid

	def __ge__(self, outro):
		return self.uuid >= outro.uuid


class ComparadorUuid(Comparador[Usuario]):

	@staticmethod
	def compararCom(usuario_1: Usuario, usuario_2: Usuario) -> int:

		result: int = 0

		if (usuario_1.uuid > usuario_2.uuid):
			result = 1

		elif (usuario_1.uuid < usuario_2.uuid):
			result = -1

		return result

class ComparadorEmail(Comparador[Usuario]):

	@staticmethod
	def compararCom(usuario_1: Usuario, usuario_2: Usuario) -> int:

		result: int = 0

		if (usuario_1.email > usuario_2.email):
			result = 1

		elif (usuario_1.email < usuario_2.email):
			result = -1

		return result

class ComparadorDataNasc(Comparador[Usuario]):

	@staticmethod
	def compararCom(usuario_1: Usuario, usuario_2: Usuario) -> int:

		result: int = 0

		if (usuario_1.data_nasc > usuario_2.data_nasc):
			result = 1

		elif (usuario_1.data_nasc < usuario_2.data_nasc):
			result = -1

		return result

class ComparadorAltura(Comparador[Usuario]):

	@staticmethod
	def compararCom(usuario_1: Usuario, usuario_2: Usuario) -> int:

		result: int = 0

		if (usuario_1.altura > usuario_2.altura):
			result = 1

		elif (usuario_1.altura < usuario_2.altura):
			result = -1

		return result

class ComparadorPeso(Comparador[Usuario]):

	@staticmethod
	def compararCom(usuario_1: Usuario, usuario_2: Usuario) -> int:

		result: int = 0

		if (usuario_1.peso > usuario_2.peso):
			result = 1

		elif (usuario_1.peso < usuario_2.peso):
			result = -1

		return result