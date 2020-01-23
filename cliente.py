class Cliente:
    
    def __init__(self, nome):
        self.__nome = nome

    @property #@propety transforma a função em uma propreiedade, sendo assim não necessitando colocar os parênteses quando a função for chamada 
    def nome(self):
        print("chamando @ propety name()")
        return self.__nome.title()

    @nome.setter #@ .setter transforma a função e possibilita chamar a mesma sem colocar os parênteses quando a função for chamada
    def nome(self, nome):
        print("chamando setter nome()")
        self.__nome = nome