# DECORATOR: função que executará ações dentro de outra função
def tudo_maiuscula(f):
	def maiuscula():
		return f().upper()
	return maiuscula

@tudo_maiuscula
def olamundo():
	return "Olá mundo!!"
ola = olamundo()
print(ola)
