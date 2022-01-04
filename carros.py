class Carro:
	def __init__(self, marca, motor, rodas):
		self.marca = marca
		self.motor = motor
		self.rodas = rodas
		
		
	def info(self):
		print(self.marca, self.motor, self.rodas)
		
	def ligar(self):
		print("Ligando o Carro")
		
	def dirigir(self):
		print("Dirigindo o Carro")
		
	def desligar(self):
		print("Desligando o Carro")
	pass
	
	
Carro1 = Carro('Honda', 'Motor 3', 'Rodas blindadas')
Carro2 = Carro('Chevrolet', 'Motor 4', 'Rodas Off-road')
Carro3 = Carro('Wolksvagen', 'Motor 2', 'Rodas normais')

Opção = 0
while Opção != 4:
	print('''	[ 1 ] Carro 1
	[ 2 ] Carro 2
	[ 3 ] Carro 3
	[ 4 ] Sair
	''')
	Opção = int(input('Escolha uma opção: '))
	if Opção == 1:
		Carro1.info(),
		Carro1.ligar(),
		Carro1.dirigir(),
		Carro1.desligar()
	if Opção == 2:
		Carro2.info(),
		Carro2.ligar(),
		Carro2.dirigir(),
		Carro2.desligar()
	if Opção == 3:
		Carro3.info(),
		Carro3.ligar(),
		Carro3.dirigir(),
		Carro3.desligar()
print('Você saiu do programa.')