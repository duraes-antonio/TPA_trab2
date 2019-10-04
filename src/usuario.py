class Usuario():

	def __init__(
			self, email: str, genero: str, id: str, data_nasc: str,
			altura: float, peso: float):
		self.email = email
		self.genero = genero
		self.uuid = id
		self.data_nasc = data_nasc
		self.altura = altura
		self.peso = peso

	def __str__(self):
		return f"email: '{self.email}'; genero: '{self.genero}'; uuid: '{self.uuid}';" \
			f"data_nasc: {self.data_nasc}; altura: {self.altura}; peso: {self.peso};"
