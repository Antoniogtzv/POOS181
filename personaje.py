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

  def recargarArma(self,municiones):
    cargador=5
    cargador = cargador + municiones
    print('El personaje '+self.__nombre+' recargó su arma y ahora tiene: '+str(cargador)+' municiones')

    def getEspecie(self):
      return self.__especie
    
    def setEspecie(self,esp):
      self.__especie= esp
    
      

