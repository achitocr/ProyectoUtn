class Mesa(object):
    def __init__(self,ancho,altura,color,material,cants):
        self.ancho=ancho
        self.altura=altura
        self.color=color
        self.material=material
        self.cants=cants

    def imprimir(self):
        print(self.ancho)
        print(self.altura)
        print(self.color)
        print(self.material)
        print(self.cants)

class Persona(object):

    def __init__(self, bla, neg, mul, mes, mor):
        self.blanca = bla
        self.negra = neg
        self.mulata = mul
        self.mestiza = mes
        self.morena = mor




class Revista(object):

    def __init__(self, com, via, inf, faran, adolesc):
        self.comic = com
        self.viajes = via
        self.informativa = inf
        self.farandula = faran
        self.adolescentes = adolesc




class Camisa(object):

    def __init__(self, pol, cue, sin, form, infor):
        self.polo = pol
        self.cuello = cue
        self.sinmangas = sin
        self.formal = form
        self.informal = infor

lista = []
lista.append(Camisa("Polo", "Cuello", "Sin Mangas", "Formal", input("inserte un valor")))