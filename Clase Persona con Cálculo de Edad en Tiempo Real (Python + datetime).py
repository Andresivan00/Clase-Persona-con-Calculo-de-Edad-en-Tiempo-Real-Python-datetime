'''
  ============================================
  Importamos la librería datetime
  ============================================
  Sirve para trabajar con fechas y horas. 
  En este caso se usará para obtener el año actual y calcular la edad.
'''
from datetime import datetime

'''
  ============================================
  DEFINICIÓN DE UNA CLASE "Persona"
  ============================================
'''
class Persona:
  '''
   Método constructor de la clase
   Se ejecuta automáticamente al crear un objeto Persona
  '''
  def __init__(self,nombre,apellido,cc,anoNac,pais,sexo):
    # Guardamos los valores en atributos internos del objeto
    self._nombre = nombre
    self._apellido = apellido
    self._cc = cc                # cédula o número de identificación
    self._anoNac = anoNac        # año de nacimiento
    self._pais = pais
    self._sexo = sexo

  '''
   ============================================
   Método para imprimir la información de la persona
   ============================================
  '''
  def imprimir(self): 
    # Retorna un texto con todos los datos de la persona
    return f'''
    Nombre: {self._nombre}
    Apellido: {self._apellido}
    Identificacion: {self._cc}
    Pais de nacimiento: {self._pais}
    Genero: {self._sexo}
    '''
  '''
   ============================================
   Método para calcular la edad
   ============================================
  '''
  def calcularEdad(self): 
    ano_Actual = datetime.now().year   # Obtiene el año actual desde el sistema
    edad = ano_Actual - self._anoNac   # Resta el año actual menos el año de nacimiento
    return edad                        # Devuelve la edad

  '''
  ============================================
  CREACIÓN DE UN OBJETO DE LA CLASE "Persona"
  ============================================
  '''
  # Se crea una persona con datos de ejemplo
p = Persona("Johana", "Garcia", "12345", 2000, "Colombia", "Femenino")

'''
 ============================================
 USO DE LOS MÉTODOS DE LA CLASE
 ============================================
'''
print(p.imprimir())                        # Muestra en pantalla todos los datos
print("La edad es: ", p.calcularEdad())    # Calcula y muestra la edad
