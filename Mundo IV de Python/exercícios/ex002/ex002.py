class Gafanhoto:
    def __init__(self, nome = "", idade = 0):
        self.nome = nome
        self.idade = idade
        
        """
    Essa classe cria um Gafanhoto, que é uma pessoa que tem nome e idade.
    Para criar uma nova pessoa, use
    variavel = Gafanhoto(nome, idade)
        """
        
        
        # Métodos de Intancia
           # Método de Inatância
    def aniversario(self):
        self.idade = 1 + self.idade
        
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Peso: {self.peso}")
        print(f"Sexo: {self.sexo}")
        print(f"Cidade: {self.cidade}")
        print(f"Estado: {self.estado}")
        

    def __str__(self): # Dunder Method
        #return "Olá, Mundo!!!"    
        return "Olá, Mundo!!! Eu sou o " + self.nome + " e tenho " + str(self.idade) + " anos."
    
    def __getstate__(self):
        return f"Olá, Mundo!!! Eu sou o {self.nome} e tenho {self.idade} anos."
    
    # Declaração de Objetos
if __name__ == "__main__":       
    g3 = Gafanhoto(nome = "Antonio", idade = 15)
    g3.peso = 50.0
    g3.sexo = "Masculino"
    g3.cidade = "Brasilia"
    g3.estado = "Distrito Federal"
    print(g3.__class__)
    g3.aniversario()
    
    #print(g3.__doc__) # Dunder Attribute
    #print(g3)
    g3 = Gafanhoto(nome = "André", idade = 49)
    #print(g3.__dict__) # Atributo
    print(g3.__getstate__()) # Method
    print(g3.__class__)
    
    print("=" * 50) 
    
    g4 = Gafanhoto(nome = "Maria", idade = 22)
    print(g4)
    #print(g4.__getstate__())
    print("=" * 50)
    
    
    