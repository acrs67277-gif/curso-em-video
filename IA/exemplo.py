from abc import ABC, abstractmethod

# 1. Criamos a Classe Abstrata (O conceito geral/abstrato)
class Eletrodomestico(ABC):
    
    @abstractmethod
    def ligar(self):
        """Qualquer eletrodoméstico precisa saber ligar, 
        mas cada um faz isso de um jeito."""
        pass

# 2. Criamos as Classes Concretas (O mundo real)
class Televisao(Eletrodomestico):
    def ligar(self):
        return "Sintonizando canais e acendendo a tela LED..."

class ArCondicionado(Eletrodomestico):
    def ligar(self):
        return "Disparando o compressor e esfriando o ambiente..."

# --- Testando o código ---

# Se tentarmos fazer isso, o Python vai dar erro:
# meu_eletro = Eletrodomestico()  # Erro! Não se pode instanciar uma classe abstrata.

# Mas podemos usar as classes concretas normalmente:
tv = Televisao()
ar = ArCondicionado()

print(tv.ligar())  # Saída: Sintonizando canais e acendendo a tela LED...
print(ar.ligar())  # Saída: Disparando o compressor e esfriando o ambiente...