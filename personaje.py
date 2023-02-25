class Personaje:
  #Creamos el constructor
  def _init_(self, esp, nom, alt):
    self.__nombre = nom
    self.__especie = esp
    self.__altura = alt
    
  def correr(self,estado):
    if estado == True:
        print('El personaje '+self.__nombre+' está corriendo')
    else:
      print('El personaje '+self.__nombre+' está quieto')
        
            
        
  def lanzarGranada(self):
    print('El personaje '+self.__nombre+' lanzó una granada')

  def recargarArma(self,municiones):
    cargador=5
    cargador = cargador + municiones
    print('El personaje '+self.__nombre+' recargó su arma y ahora tiene: '+str(cargador)+' municiones')

  def __pensar(self):
     print("estoy pensando..............")

  def recargarArma(self,municiones):
    cargador=5
    cargador = cargador + municiones
    print('El personaje '+self.__nombre+' recargó su arma y ahora tiene: '+str(cargador)+' municiones')

    def getEspecie(self):
      return self.__especie
    
    def setEspecie(self,esp):
      self.__especie= esp
      
    def getnombre(self):
        return self.__nombre
    
    def setaltura(self,esp):
         return self.__nombre
    
    def getAltura(self):
      self.__altura =alt


    
      

