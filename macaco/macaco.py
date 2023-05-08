class macaco:
    def __init__(self,nome,bucho,comer,verbucho,digerir):
        self.nome = nome
        self.bucho = bucho
        self.comer = comer
        self.verbucho = verbucho
        self.digerir  = digerir
        
    def novoNome(self,novoNome):
        self.nome = novoNome
    
    def meuBucho(self,meuBucho):
        self.bucho = meuBucho
        
    def boraComer(self,boraComer):
        self.comer = boraComer
    
    def iaverbucho(self,iaverbucho):
        self.verbucho = iaverbucho
        
    def voudigerir(self,voudigerir):
        self.digerir = voudigerir
        
    def mostrar(self):
        print() 