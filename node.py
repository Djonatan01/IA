class No(object):
    def __init__(self, pai=None, estado=None, nivel=None, 
                 anterior=None,  proximo=None):
        self.pai       = pai
        self.estado    = estado
        self.nivel     = nivel
        self.anterior  = anterior
        self.proximo   = proximo