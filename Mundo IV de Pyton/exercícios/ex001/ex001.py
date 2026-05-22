# Declaração de Classe
class Gafanhoto: 
    # Método Construtor
    def __init__(self, nome, idade):
        # Atributos de Instância
        self.nome = nome
        self.idade = idade

        # Métodos de Instância
        def aniversario(self): 
            self.idade = self.idade + 1
            
        def mensagem(self):         
            return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade";

            
        # Definição de Objeto
        g1 = Gafanhoto()
        g1.nome = 'João'
        g1.idade = 20
        g1.aniversario()
        print(g1.mensagem())  
        
        g2 = Gafanhoto()
        g2.nome = 'Maria'
        g2.idade = 25
        g2.aniversario()
        print(g2.mensagem())
        
        g3 = Gafanhoto()
        print(g3.mensagem())
        
      