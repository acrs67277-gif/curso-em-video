# 1. O Molde (Classe)
class Pessoa:
    # O construtor define as características que todo cachorro terá ao nascer
    def __init__(self, nome, idade):
        self.nome = nome  # Atributo
        self.idade = idade  # Atributo

    # Uma ação que o cachorro sabe fazer
    def falar(self):  # Método
        return f"{self.nome} diz: Olá, Mundo!!! {self.nome} diz: Vocẽs não iram me fazer desistir."
    


# 2. O Objeto Real (Instância)
# Aqui estamos dando vida a uma pessoa escifica
minha_pessoa = Pessoa(nome="Thor", idade=3)

# Usando o objeto:
print(minha_pessoa.nome)  # Acessando um atributo -> Saída: Thor
print(minha_pessoa.falar())  # Chamando um método -> Saída: Thor diz: Olá, Mundo!!!