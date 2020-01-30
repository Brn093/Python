# Super Classe
class Eletronico:
	def __init__(self):
		self.ligado = False
	def ligar(self):
		self.ligado = True
	def desligar(self):
		self.ligado = False
	def esta_ligado(self):
		return self.ligado
#Herança
class TV(Eletronico):
	def __init__(self):
		Eletronico.__init__(self) #método construtor da super
		self.volume = 0
	def aumentar_volume(self):
		self.volume = self.volume + 1
	def diminuir_volume(self):
		if self.volume > 0:
			self.volume = self.volume - 1 
	def obter_volume(self):
		return self.volume
#Herança
class IPhone(Eletronico):
	def __init__(self):
		Eletronico.__init__(self)#
		self.tocando_musica = False
	def tocar_musica(self):
		self.tocando_musica = True
	def parar_musica(self):
		self.tocando_musica = False
	def tocando_som(self):
		return self.tocando_musica

#tv = TV()
#print(tv.esta_ligado())
#tv.ligar()
#print(tv.esta_ligado())
#tv.aumentar_volume()
#print(tv.obter_volume())
#tv.diminuir_volume()
#print(tv.obter_volume())
#i = 0
#while i < 10:
	#tv.aumentar_volume()
	#i += 1
#print(tv.obter_volume())

iphone = IPhone()
print(iphone.tocando_som())
iphone.tocar_musica()
print(iphone.tocando_som())
iphone.parar_musica()
print(iphone.tocando_som)
