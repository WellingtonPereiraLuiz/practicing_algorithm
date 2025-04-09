from dataclasses import dataclass

@dataclass
class Veiculo:
    marca:  str
    modelo: str

    def ligar(self):
        print(f"O {self.marca}{self.modelo} esta ligado")

@dataclass
class Carro(Veiculo):
    num_portas: int
    
    def abri_portas(self, numero_porta):
        print(f"Abrindo {numero_porta} do carro {self.marca} {self.modelo}")
        
my_car = Carro(marca="Toyota", modelo="Jeep", num_portas = 4)

my_car.ligar()
my_car.abri_portas(2)