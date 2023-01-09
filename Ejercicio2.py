class Stormtrooper:
    def _init_(self,nombre,rango):
        self.nombre=nombre
        self.rango=rango
    def _str_(self):
        return f"{self.nombre} {self.rango}"      
class Codigolegion(Stormtrooper):
    def _init_(self, nombre, rango, codigolegion:str) -> None:
        super()._init_(nombre, rango,codigolegion)
        self.codigolegion=codigolegion
class Identificador_coherente(Stormtrooper):
    def _init_(self,nombre,rango,identificadorcoherente:int) -> None:
        super()._init_(nombre,rango,identificadorcoherente)
        self.identificadorcoherente=identificadorcoherente
class Identificador_siglo(Stormtrooper):
    def _init_(self, nombre, rango,identificadorsiglo):
        super()._init_(nombre,rango,identificadorsiglo)
        self.identificadorsiglo=identificadorsiglo
class Identificador_escuadra(Stormtrooper):
    def _init_(self, nombre, rango,identificadorescuadra):
        super()._init_(nombre,rango,identificadorescuadra)
        self.identificadorescuadra=identificadorescuadra
class Numero_trooper(Stormtrooper):
    def _init_(self, nombre, rango,numerotrooper):
        super()._init_(nombre,rango,numerotrooper)
        self.identificadorescuadra=numerotrooper
