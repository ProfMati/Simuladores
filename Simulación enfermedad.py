#=============================================================================
# Simulador enfermedad y examen:
# Este simulador genera una lista con true o false donde true
# representa a una persona enferma y false una persona sana.
# Luego aplica una prueba que tiene alguna probabilidad de fallar
#=============================================================================

import random

#-----------------------------------------------------------------------------
# Variables Gobales
#-----------------------------------------------------------------------------

N  = 1000 # Número de casos
PE = 0.1  # Probabilidad de estar enfermo
PD = 95   # Probabilidad de un diagnóstico correcto

#-----------------------------------------------------------------------------
# Inicio de programa
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# * Función resultado_caso
# Rertorna True con probabilidad p Usar máximo 2 decimales
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# * Función resultado_enfermedad
# Simula el resultado de examen de una persona enferma o no. 
#-----------------------------------------------------------------------------


#-----------------------------------------------------------------------------
# * Función simula
# Simula N casos
#-----------------------------------------------------------------------------    


#-----------------------------------------------------------------------------
# Fin definiciones específicas
#----------------------------------------------------------------------------- 



def mostrar_elecciones(elecciones, inicio = 0,msj = "Elección:"):
    while True:
        for i in range(inicio,len(elecciones) + inicio):
            print(str(i)+":",elecciones[i-inicio])
        a = input(msj + " ")
        try:
            a = int(a)
            if not(inicio <= a < len(elecciones) + inicio):
                print("Elección inválida")
                continue
            return a
        except:
            print("Elección inválida")
    
class Simulador:
    def __init__(self):
        global N, PE, PD
        self.N  = N
        self.PE = PE
        self.PD = PD
        self.Main()

    def Main(self):
        while True:
            elec = ["Cambiar datos", "Simular"]
            elec = mostrar_elecciones(elec)
            if elec == 0:
                self.cambiar_datos()
            else:
                self.simula()

    def cambiar_datos(self):
        while True:
            print("*" + "-"*50)
            print("Recuerde que las probabilidades deben tener máximo dos decimales") 
            elec = ["Ninguna", "Número de casos", "Prob. enfermedad", "Prob. diagnóstico correcto"]
            elec = mostrar_elecciones(elec, msj = "¿Qué constante quiere cambiar?:")
            if elec == 0:
                return
            elif elec == 1:
                self.N  = int(input("Número de casos: "))
            elif elec == 2:
                self.PE = int(input("Prob. enfermedad: ").replace(",", "."))
            elif elec == 3:
                self.PD = int(input("Prob. diagnóstico correcto: ").replace(",", "."))

    def resultado_enfermedad(self, enfermo):
        if enfermo:
            return self.resultado_caso(self.PD)
        else:
            return not(self.resultado_caso(self.PD))

    def simula(self):
        lista_pacientes = []
        for i in range(self.N):
            lista_pacientes.append(self.resultado_caso(self.PE))
        resultados = []
        for i in lista_pacientes:
            resultados.append(self.resultado_enfermedad(i))
        enfermos  = lista_pacientes.count(True)
        sanos     = len(lista_pacientes) - enfermos
        positivos = resultados.count(True)
        negativos  = len(resultados) - positivos
        print("*" + "-"*50)
        print("Pacientes sanos:    ", sanos)
        print("Pacientes enfermos: ", enfermos)
        print("Examenes positivos: ", positivos)
        print("Exámenes negativos: ", negativos)
        print("*" + "-"*50)

    def resultado_caso(self, p):
        p = p*100
        r = random.randint(1,10000)
        if r <= p:
            return True
        else:
            return False

Simulador()
