from datetime import datetime


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

#TODO: finalizar
def convert_linha_usuario(linha: str) -> Usuario:
	usuario = None
	return usuario

#TODO: finalizar
def convert_arq_para_usuarios(arq_caminho: str) -> [Usuario]:
	return None

#TODO: Implementar comparable
def main(args: [str]):

	# parseInputFileName(args)
	# parseOutputFileName(args)

	# A ← readCsv(inputName)
	arq_path = args[2]
	users = convert_arq_para_usuarios(arq_path)

	# initTime ← getCpuTime
	# xyzSort(A)
	# finishTime ← getCpuTime

	# writeCsv(A, outputName)

	# reportTime(A, initTime, finishTime)

	return 0

main([])