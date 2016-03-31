class vehiculo(object):
	def __init__(self,Kilometraje,Bencina,Rendimiento,Encendido):
		self.Kilometraje=Kilometraje
		self.Bencina=Bencina
		self.Rendimiento=Rendimiento
		self.Encendido=Encendido
	def Encender (self):
			self.Encendido=True
	def Apagar(self):
			self.Encendido=False
	def Mover(self,KM):
		m=KM/self.Rendimiento
		if m<self.Bencina:
			self.Encender()
			self.bencina -=m
			print "mover"
		else:
			self.Apagar()
			print "debe cargar bencina para partir"

	def ObtenerKilometraje(self):
		return self.Kilometraje
	def ObtenerBencina(self):
		return self.Bencina
	def CargarBencina(self,ben):
		self.Bencina += ben
class acoplado(object):
	def __init__(self,ruedas,peso,carga):
		self.ruedas=ruedas
		self.peso=peso
		self.carga=carga
class camion(vehiculo):
	def __init__(self,peso,ruedas):
		vehiculo.__init__(Kilometraje,Bencina,Rendimiento,Encendido)
		self.acoplados=[]
		self.peso=peso
		self.ruedas=ruedas
	def agregar_acoplado(self, car,ru,p):
		a=acoplado(ru,p,car)
		self.acoplados.append(a)
	def quitar_acoplado():
		if len(self.acoplados)>0:
			self.acoplados.pop(len(self.acoplados)-1)
	def obtener_acoplados():
			return self.acoplados
	def obtener_ruedas():
			return self.ruedas
	def obtener_peso():
			return self.peso





