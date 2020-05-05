import time


class Cronometro:	

	def __init__(self, hora, minuto, segundo, decima):
		self._hora = int(hora)
		self._minuto = int(minuto)
		self._segundo = int(segundo)
		self._decima = int(decima)

	def aumentoDecima(self):
		time.sleep(.10)		
		self._decima +=1

	def aumentoSegundo(self):		
		self._segundo +=1

	def aumentoMinuto(self):		
		self._minuto +=1

	def aumentoHora(self):
		self._hora +=1

	def reset(self):
		self.__init__()

	def resetDecima(self):
		self._decima = 0

	def resetSegundo(self):
		self._segundo = 0

	def resetMinuto(self):
		self._minuto = 0

	@property
	def decima(self):
		return self._decima

	@property
	def segundo(self):
		return self._segundo

	@property
	def minuto(self):
		return self._minuto

	@property
	def hora(self):
		return self._hora
	
x = True	
crono1 = Cronometro(0,0,50,8)
while x:	
		
	crono1.aumentoDecima()
	if(crono1.decima >= 10):
		crono1.aumentoSegundo()
		crono1.resetDecima()
	elif (crono1.segundo >= 59):
		crono1.aumentoMinuto()
		crono1.resetSegundo()
	elif(crono1.minuto >= 59):
		crono1.aumentoHora()
		crono1.resetMinuto()
	elif(crono1.minuto == 1 and crono1.segundo == 2):
		x = False
	
	print(crono1.hora,crono1.minuto,crono1.segundo,crono1.decima)