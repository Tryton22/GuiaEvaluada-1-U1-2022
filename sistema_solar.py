class Sistema_solar(): 
	def __init__ (self, nombre):
		self.nombre = nombre
		self.masa = None
		self.densidad = None
		self.distancia = None
		self.numero = None
		self.dar_masa()
		self.dar_densidad()
		self.dar_distancia_sol()
		self.dar_numero_unico()
		
		
	def dar_masa(self):
		
		if self.nombre == "Mercurio":
			self.masa = "Masa = 3,285 * 10^23 kg"
			
		elif self.nombre == "Venus":
			self.masa = "Masa = 4,867 * 10^24 kg"
			
		elif self.nombre == "Tierra":
			self.masa = "Masa = 5,972 * 10^24 kg"
			
		elif self.nombre == "Marte":
			self.masa = "Masa = 6,39 * 10^23 kg"
			
		elif self.nombre == "Jupiter":
			self.masa = "Masa = 1,898 * 10^27 kg"
			
		elif self.nombre == "Saturno":
			self.masa = "Masa = 5,683 * 10^26 kg"
			
		elif self.nombre == "Urano":
			self.masa = "Masa = 8,681 * 10^25 kg"
			
		elif self.nombre == "Neptuno":
			self.masa = "Masa = 1,024 * 10^26 kg"
			
	def dar_densidad(self):
		
		if self.nombre == "Mercurio":
			self.densidad = "Densidad = 5,43 g/cm3"
			
		elif self.nombre == "Venus":
			self.densidad = "Densidad = 5,24 g/cm3"
			
		elif self.nombre == "Tierra":
			self.densidad = "Densidad = 5,51 g/cm3"
			
		elif self.nombre == "Marte":
			self.densidad = "Densidad = 3,93 g/cm3"
			
		elif self.nombre == "Jupiter":
			self.densidad = "Densidad = 1,33 g/cm3"
			
		elif self.nombre == "Saturno":
			self.densidad = "Densidad = 687 kg/m3"
			
		elif self.nombre == "Urano":
			self.densidad = "Densidad = 1,27 g/cm3"
			
		elif self.nombre == "Neptuno":
			self.densidad = "Densidad = 1,64 g/cm3"
	
	def dar_distancia_sol(self):
		
		if self.nombre == "Mercurio":
			self.distancia = "Distancia al Sol = 0,39 ua (ua = 150000000 km)"
			
		elif self.nombre == "Venus":
			self.distancia = "Distancia al Sol = 0,72 ua (ua = 150000000 km)"
			
		elif self.nombre == "Tierra":
			self.distancia = "Distancia al Sol = 1.00 ua (ua = 150000000 km)"
			
		elif self.nombre == "Marte":
			self.distancia = "Distancia al Sol = 1.52 ua (ua = 150000000 km)"
			
		elif self.nombre == "Jupiter":
			self.distancia = "Distancia al Sol = 5.20 ua (ua = 150000000 km)"
			
		elif self.nombre == "Saturno":
			self.distancia = "Distancia al Sol = 9.54 ua (ua = 150000000 km)"
			
		elif self.nombre == "Urano":
			self.distancia = "Distancia al Sol = 19.19 ua (ua = 150000000 km)"
			
		elif self.nombre == "Neptuno":
			self.distancia = "30,06 ua (ua = 150000000 km)"
		
	def dar_numero_unico(self):
		
		if self.nombre == "Mercurio":
			self.numero = "Numero Unico = 1"
			
		elif self.nombre == "Venus":
			self.numero = "Numero Unico = 2"
			
		elif self.nombre == "Tierra":
			self.numero = "Numero Unico = 3"
			
		elif self.nombre == "Marte":
			self.numero = "Numero Unico = 4"
			
		elif self.nombre == "Jupiter":
			self.numero = "Numero Unico = 5"
			
		elif self.nombre == "Saturno":
			self.numero = "Numero Unico = 6"
			
		elif self.nombre == "Urano":
			self.numero = "Numero Unico = 7"
			
		elif self.nombre == "Neptuno":
			self.numero = "Numero Unico = 8"	
		
if __name__ == "__main__":
	choice = 0
	
while 0 <= choice or choice < 8:
	
	print("Informacion de nuestro Sistema Solar.")
	print("<1> Planeta Mercurio.")
	print("<2> Planeta Venus.")
	print("<3> Planeta Tierra.")
	print("<4> Planeta Marte.")
	print("<5> Planeta Jupiter.")
	print("<6> Planeta Saturno.")
	print("<7> Planeta Urano.")
	print("<8> Planeta Neptuno.")
	print("<0> Salir.")
	
	try:
		choice = int(input("Elija el planeta a eleccion: "))
		print(" ")
		
	except ValueError:
		print("Ingrese un digito valido")
		
	if choice == 1:
		mercurio = Sistema_solar("Mercurio")
		print("Caracteristicas de Mercurio.")
		print(mercurio.masa)
		print(mercurio.densidad)
		print(mercurio.distancia)
		print(mercurio.numero)
		print(" ")
		
	elif choice == 2:
		venus = Sistema_solar("Venus")
		print("Caracteristicas de Venus.")
		print(venus.masa)
		print(venus.densidad)
		print(venus.distancia)
		print(venus.numero)
		print(" ")
	
	elif choice == 3:
		tierra = Sistema_solar("Tierra")
		print("Caracteristicas de la Tierra.")
		print(tierra.masa)
		print(tierra.densidad)
		print(tierra.distancia)
		print(tierra.numero)
		print(" ")
		
	elif choice == 4:
		marte = Sistema_solar("Marte")
		print("Caracteristicas de Marte.")
		print(marte.masa)
		print(marte.densidad)
		print(marte.distancia)
		print(marte.numero)
		print(" ")
		
	elif choice == 5:
		jupiter = Sistema_solar("Jupiter")
		print("Caracteristicas de Jupiter.")
		print(jupiter.masa)
		print(jupiter.densidad)
		print(jupiter.distancia)
		print(jupiter.numero)
		print(" ")
		
	elif choice == 6:
		saturno = Sistema_solar("Saturno")
		print("Caracteristicas de Saturno.")
		print(saturno.masa)
		print(saturno.densidad)
		print(saturno.distancia)
		print(saturno.numero)
		print(" ")
		
	elif choice == 7:
		urano = Sistema_solar("Urano")	
		print("Caracteristicas de Urano.")
		print(urano.masa)
		print(urano.densidad)
		print(urano.distancia)
		print(urano.numero)
		print(" ")
		
	elif choice == 8:
		neptuno = Sistema_solar("Neptuno")	
		print("Caracteristicas de Neptuno.")
		print(neptuno.masa)
		print(neptuno.densidad)
		print(neptuno.distancia)
		print(neptuno.numero)
		print(" ")
		
	elif choice == 0:
		exit()
		
	else:
		print("Ingrese algo valido.")
		print(" ")
