from datetime import datetime
from os import path

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

	def __str__():
		return f"email: '{self.email}'; genero: '{self.genero}'; uuid: '{self.uuid}'; data_nasc: {self.data_nasc}; altura: {self.altura}; peso: {self.peso};"

#TODO: finalizar
def convert_linha_usuario(separador: str, linha: str) -> Usuario:
	params = linha.split(separador)
	usuario: Usuario = Usuario(params[0], params[1], params[2], params[3], float(params[4]), float(params[5]))
	return usuario

#TODO: finalizar
def convert_arq_para_usuarios(arq_caminho: str, separador: str) -> [Usuario]:

	usuarios: [Usuario]

	with open(arq_caminho, 'r', encoding='utf-8') as arq:
		usuarios = [convert_linha_usuario(separador, linha) for i, linha in enumerate(arq.readlines()) if i > 0]

	return usuarios

#TODO: Implementar comparable
def main(args: [str]):

	# parseInputFileName(args)
	# parseOutputFileName(args)

	# A ← readCsv(inputName)
	print(path.curdir)
	arq_path =  'data_75e4.csv'
	usuarios = convert_arq_para_usuarios(arq_path, ',')
	[print(u + '\n') for u in usuarios]

	# initTime ← getCpuTime
	# xyzSort(A)
	# finishTime ← getCpuTime

	# writeCsv(A, outputName)

	# reportTime(A, initTime, finishTime)

	return 0

main([])