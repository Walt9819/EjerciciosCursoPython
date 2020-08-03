from Ayudas import ObtenerNumeroEntero, ObtenerNumeroFlotante
import numpy as np

# Simular un día
def PasoSimulacion():
    global personas
    # TODO

# Distribución de los casos iniciales
def CasosIniciales(iniciales):
    global personas
    #TODO


# Total de personas
dimension = ObtenerNumeroEntero(pregunta='¿Cuántas personas hay en la simulación? (Se tomará floor(sqrt))')

# Casos iniciales
iniciales = ObtenerNumeroEntero(pregunta='¿Cuántos contagiados iniciales hay?: ')

# Valor de factor beta (probabilidad de contagiarse)
beta = ObtenerNumeroFlotante(min=0, max=1, pregunta='¿Cuál es el valor de beta? (probabilidad de que un suceptible se contagie): ') ##entre 0 y 1

# Valor de factor gamma (probabilidad de recuperarse)
gamma = ObtenerNumeroFlotante(min=0, max=1, pregunta='¿Cuál es el valor de gamma? (probabilidad de que un infectado se recupere o muera): ') ##entre 0 y 1

# Raíz del número de personas (la forma es un cuadrado)
dimension = int(np.sqrt(dimension))
dimensiones = (dimension, dimension)

#Arreglo de personas inicial (todos susceptibles)
personas = np.zeros(dimensiones)

# DIstribución de los caso iniciales
CasosIniciales(iniciales)

# Simular hasta que deje de haber infectados
while sum(sum(personas == 1)) != 0:
    PasoSimulacion()
