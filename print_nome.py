class Daoi:
    def __init__(self, nome) -> None:
        self.nome = nome
    
    def fala_o_nome(self):
        print('Oi,',self.nome)  

teste = Daoi('lucas')
teste.fala_o_nome()