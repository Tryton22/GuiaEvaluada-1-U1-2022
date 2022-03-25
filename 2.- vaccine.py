class Vaccine:
	def __init__(self, vacuna, laboratorio, efse, numero):
		self.efse = efse
		self.vacuna = vacuna
		self.laboratorio = laboratorio
		self.set_agrega_efecto_secundario(vacuna, laboratorio, efse)
		self.mostrar_efecto_secundario(numero)
	
	def set_agrega_efecto_secundario(self, vacuna, laboratorio, efse):
		vacunas.append(vacuna)
		laboratorios.append(laboratorio)
		second_efects.append(efse)
			
	def mostrar_efecto_secundario(self, numero):
		print(vacunas[numero],":",second_efects[numero])

if __name__ == "__main__":
	
	vacunas = []
	laboratorios = []
	second_efects = []
	
	Vac1 = Vaccine("Vac1", "PF", "Diarrea", 0)
	Rangerito = Vaccine("Rangerito", "Fiscal", "Jaqueca", 1)
	Pfizer = Vaccine("Pfizer", "Biontech", "5G", 2)
	
