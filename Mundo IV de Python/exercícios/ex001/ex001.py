    # Declaração de Classe
class Gama():
    def __init__(self): # Metado Construtor
        # Atributos de Instância
        self.nome = ""
        self.idade = 0
        self.peso = 0.0
        self.sexo = ""
        self.cidade = ""
        self.estado = ""

        # Método de Inatância
    def aniversario(self):
        self.idade = 1 + self.idade
        
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Peso: {self.peso}")
        print(f"Sexo: {self.sexo}")
        print(f"Cidade: {self.cidade}")
        print(f"Estado: {self.estado}")
        

            
    # Declaração de Objetos
if __name__ == "__main__":
    g1 = Gama()
    g1.nome = "André"
    g1.idade = 49
    g1.peso = 130.0
    g1.sexo = "Masculino"
    g1.cidade = "Pedra Preta"
    g1.estado = "Mato Grosso"
    g1.aniversario()
    print("=" *20)  
     
    g2 = Gama()
    g2.nome = "Juliana"
    g2.idade = 35
    g2.peso = 70.0
    g2.sexo = "Feminino"
    g2.cidade = "Cuiabá"
    g2.estado = "Mato Grosso"
    g2.aniversario()
    print("=" *20) 
        
    g3 = Gama()
    g3.nome = "Gustavo"
    g3.idade = 15
    g3.peso = 50.0
    g3.sexo = "Masculino"
    g3.cidade = "Brasilia"
    g3.estado = "Distrito Federal"
    g3.aniversario()
    print("=" *20) 
    