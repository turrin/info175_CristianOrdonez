class Auto(object):
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
			self.bencina=self.bencina-m
			print "mover"
		else:
			self.Apagar()
			print "debe cargar bencina para partir"

	def ObtenerKilometraje(self):
		return self.Kilometraje
	def ObtenerBencina(self):
		return self.Bencina
	def CargarBencina(self,ben):
		self.Bencina+=ben

x=Auto(0,10,19,False)
print x.ObtenerKilometraje()
print x.ObtenerBencina()
r=raw_input("cuantos kilometros desea moverse: ")
x.Mover(int (r))


