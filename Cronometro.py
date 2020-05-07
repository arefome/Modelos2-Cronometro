import time
import datetime

class Cronometro:	
	
	def __init__(self):
		self._hora = 0
		self._minuto = 0
		self._segundo = 0
		self._decima = 0
		self._activo = True
		
	def aumentoDecima(self):
		time.sleep(.001)		
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
	
	def iniciar(self):
		if(self._activo):
			self.aumentoDecima()
			if(self.decima >= 99):
				self.aumentoSegundo()
				self.resetDecima()
			elif (self.segundo >= 59):
				self.aumentoMinuto()
				self.resetSegundo()
			elif(self.minuto >= 59):
				self.aumentoHora()
				self.resetMinuto()
			
	def mostrarTiempo(self):
		tiempo = datetime.time(self.hora,self.minuto,
							self.segundo, self.decima).strftime("%H:%M:%S.%f")
		return tiempo
				
	def reiniciar(self):
		self.resetDecima()
		self.resetSegundo()
		self.resetMinuto()
	
		
	def detener(self):
		self._activo = False if self._activo else True
			

	