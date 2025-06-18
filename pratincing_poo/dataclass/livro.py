from dataclasses import dataclass

@dataclass
class Livro:
    titulo: str
    autor: str
    num_paginas: int
    
    def sobre(self):
        print(f"O livro {self.titulo} escrito por {self.autor} possui {self.num_paginas} paginas!")

livro1 = Livro(titulo="Cidadao Incomum", autor="Pedro Ivo", num_paginas= 240)

livro1.sobre()