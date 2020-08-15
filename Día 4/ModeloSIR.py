from scipy.integrate import odeint
import numpy as np

# Modelo SIR
def sir(y, t, beta, gamma):
    S, I, R, C = y
    N = S+I+R # Población total
    infectados = beta*I*S/N # Nuevos infectados
    removidos = gamma*I # Nuevos removidos
    dydt = [-infectados, infectados-removidos, removidos, infectados]
    return dydt

# Parámetros de simulación
beta = 0.52 # probabilidad de contagiarse
gamma = 1/7 # probabilidad de recuperarse o morir
poblacion = 1000 # población total
I0 = poblacion * 0.01 # infectados iniciales

y0 = [poblacion - I0, I0, 0.0, I0] # Conjunto de condiciones iniciales y(0)
t = np.linspace(0, 40, 40) # Tiempo de simulación (un paso por día)

sol = odeint(sir, y0, t, args=(beta, gamma)) # Solucionador

S = sol[:, 0] # Susceptibles a lo largo del tiempo
