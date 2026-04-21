# Módulo de monitoreo V2

# 1. Alcance Global: Variable accesible por cualquier función
LIMITE_ALERTA_GLOBAL = 85.0

# ========================================================================

# 2. Definir funciones
def calibrar_sensor(temperatura, ajuste):
    temperatura_calibrada = temperatura + ajuste
    return temperatura_calibrada

def mostrar_encabezado():
    print("=========================================")
    print("     SISTEMA DE MONITOREO INDUSTRIAL     ")
    print("=========================================")

# ========================================================================

# 3. Muestra del encabezado

mostrar_encabezado()
lectura_sensor = float(input("ingrese la temperatura del motor (°C): "))

print("\n--- Modo Calibración ---")
ajuste_tecnico = 2.5
lectura_sensor = calibrar_sensor(lectura_sensor, ajuste_tecnico)
print(f"Temperatura tras calibración de {ajuste_tecnico}°C: {lectura_sensor}°C")

# ========================================================================

# 4. Función con retorno
def validar_temperatura(temp_actual):
    if temp_actual > LIMITE_ALERTA_GLOBAL:
        return True     # Hay alerta
    
    return False        #Todo normal

# ========================================================================

# 5. Ejecución

if validar_temperatura(lectura_sensor):
    print ("¡PELIGRO! Temperatura excede el límite operativo.")

else:
    print ("Estado del motor: Operativo y estable.")