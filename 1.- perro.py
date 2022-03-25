class perro():
	def __init__ (self, agua, walk, hora):
		self.agua = agua
		self.walk = walk
		self.hora = hora
		self.set_tomar_agua(hora)
		self.get_hora_toma_agua()
		self.caminar(hora, agua)
		
	def set_tomar_agua(self, hora):
		print("La hora es: ",hora)
		print("")
		
	def get_hora_toma_agua(self):
		print ("El perrito tomo agua a las ", agua)
		print("")
		
	def caminar(self, hora, agua):
		if hora == agua:
			print("El perrito puede salir")
			print("")
		
		else:
			print("Aun falta para que salga")
			print("")
if __name__ == "__main__":
	hora = 1
	agua = 0
	walk = None
	firulais = perro(agua, False , hora)
	
	choice = -1
	while choice != 0:
		
		if hora == 25:
			hora = 1
		
		print("Informacion sobre su Perro")
		print("<1> Ultima vez que tomo agua")
		print("<2> Hora Actual")
		print("<3> ¿Es la hora de salida del perrito?")
		print("<4> Pasar de hora")
		print("<0> Salir")
	
		try:
			choice = int(input("Ingrese su decision: "))
			print(" ")
		
		except ValueError:
			print("Ingrese un digito valido por favor")
		
		if choice == 0:
				exit()
				
		elif choice == 1:
			hora = hora + 1
			if hora % 4 == 0:
				agua = hora
			firulais.get_hora_toma_agua()
			
				
		elif choice == 2:
			hora = hora + 1
			if hora % 4 == 0:
				agua = hora
			firulais.set_tomar_agua(hora)
			
				
		elif choice == 3:
			hora = hora + 1
			if hora % 4 == 0:
				agua = hora
			firulais.caminar(hora, agua)
			
				
		elif choice == 4:
			hora = hora + 1
			if hora % 4 == 0:
				agua = hora
			
		else:
			print("INGRESE UN DATO VALIDO")
			print("")
				
		
		
	
