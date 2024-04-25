class No(object):
    def __init__(self, pai=None, estado=None, nivel=None, 
                 anterior=None,  proximo=None):
        self.pai       = pai
        self.estado    = estado
        self.nivel     = nivel
        self.anterior  = anterior
        self.proximo   = proximo
        
class No_od(object):
    def __init__(self, pai=None, estado=None, valor1=None, 
                valor2=None, anterior=None, proximo=None):
        self.pai       = pai
        self.estado    = estado
        self.valor1    = valor1  
        self.valor2    = valor2 
        self.anterior  = anterior
        self.proximo   = proximo