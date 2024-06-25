from datetime import datetime

def calcular_meses_de_vida(fecha_nacimiento, fecha_actual):
    """
    Calcula los meses de vida de una persona dada su fecha de nacimiento y la fecha actual.
    
    Parámetros:
    fecha_nacimiento (datetime): La fecha de nacimiento de la persona.
    fecha_actual (datetime): La fecha actual.
    
    Retorna:
    int: El número de meses de vida.
    """
    # Calcular la diferencia en años y meses entre las dos fechas
    años = fecha_actual.year - fecha_nacimiento.year
    meses = fecha_actual.month - fecha_nacimiento.month
    
    # Si el mes de la fecha de nacimiento es mayor que el mes de la fecha actual,
    # restamos un año y ajustamos los meses
    if meses < 0:
        años -= 1
        meses += 12
    
    # Calcular los meses totales
    meses_totales = años * 12 + meses
    
    return meses_totales

# Ejemplo de uso
fecha_nacimiento = datetime(2018, 12, 18)
fecha_actual = datetime(2024, 6, 24)
meses_de_vida = calcular_meses_de_vida(fecha_nacimiento, fecha_actual)
print(f"La persona tiene {meses_de_vida} meses de vida.")
