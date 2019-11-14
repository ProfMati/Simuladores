#============================================================================
# Esperanza de Dados
# Este script está hecho para mostrar cómo funciona el cocepto de esperanza
# matemática utilizando, para eso, varios lanzamientos de varios dados.
# Por Matías Sáez Ulloa. Versión: 0.1
#============================================================================

import random

#============================================================================
# Configuración
#============================================================================

#----------------------------------------------------------------------------
# * Lista de dados
# A continuación está a lista de dados a utilizar, es editable.
#----------------------------------------------------------------------------

Dados = [
    [1,2,3,4,5,6],
#    [5,5,5,5,5,5]
#    [6,6,6,6,6,6]
    [0,4,4,4,4,4],  # Dado Shy Guy
    #[0,0,1,8,9,10], # Dado Bowser
    #[0,0,2,3,4,8],  # Dado Rosalina
    #[3,3,3,3,3,3],
    #[0,0,0,7,7,7],  # Dado Diddy Kong
    ] # No borrar

#----------------------------------------------------------------------------
# * Número de lanzamientos
# El número de veces que se lanzará cada dado
#----------------------------------------------------------------------------

N = 1000

#============================================================================
# Inicio del programa
#============================================================================

def sample(lista):
    n = len(lista)
    r = random.randint(0,n-1)
    return lista[r]

def lanzar_dado(lista,n=N):
    global N
    suma = 0
    for i in range(0,n):
        suma += sample(lista)
    return suma

def esperanza(lista):
    largo     = len(lista)
    esperanza = 0 
    for i in lista:
        esperanza += i*(1/largo)
    return esperanza

def lanzar_dados(promedio = False, espt = False):
    global Dados, N
    text  = ""
    text += "*"*70 + "\n"
    text += "Se procederá a lanzar los Dados " + str(N) + " veces.\n"
    for i in range(len(Dados)):
        suma = lanzar_dado(Dados[i])
        text += "Suma del dado N°" + str(i+1)+ ": " + str(suma)
        if promedio: text += " Promedio: " + str(round(suma/N,1))
        if espt: text += " Esperanza: " + str(round(esperanza(Dados[i]),1))
        text += "\n"
    text += "*"*70
    print(text)

def varianza(lista):
    p    = 1/len(lista)
    e    = esperanza(lista)
    suma = 0
    for i in lista:
        suma += ((i-e)**2)*p
    return suma

def desvesta(lista):
    ecuadrado  = esperanza(lista)**2
    excuadrado = esperanza([x**2 for x in lista])
    return (excuadrado - ecuadrado)**0.5


lanzar_dados()









