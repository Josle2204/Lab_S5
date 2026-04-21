# Módulo de monitoreo V1

# 1. Alcance Global: Variable accesible por cualquier función
LIMITE_ALERTA_GLOBAL = 85.0

# 2. Función sin retorno (Procedimiento)
def mostrar_encabezado():
    print("=========================================")
    print("     SISTEMA DE MONITOREO INDUSTRIAL     ")
    print("=========================================")

# 3. Función con retorno
def validar_temperatura(temp_actual):
    if temp_actual > LIMITE_ALERTA_GLOBAL:
        return True     # Hay alerta
    
    return False        #Todo normal

# Ejecución principal
mostrar_encabezado()
lectura_sensor = float(input("ingrese la temperatura del motor (°C): "))

if validar_temperatura(lectura_sensor):
    print ("¡PELIGRO! Temperatura excede el lpimite operativo.")

else:
    print ("Estado del motor: Operativo y estable.")