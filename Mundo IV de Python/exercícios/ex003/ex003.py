class ContaBancaria:
    
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        
        def __str__(self):
            return f"A conta {self.id} de {self.titular} tem saldo de R${self.saldo:.2f} de saldo."
        
        def depositar(self, valor):
            self.saldo += valor
        
        def sacar(self, valor):
            pass
        
        
        
        conta1 = ContaBancaria(id=1112, nome="André", saldo=2500)
        conta1.depositar(500) 
        print(conta1)  
        
        