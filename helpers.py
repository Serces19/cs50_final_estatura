from datetime import datetime

def calcular_meses_de_vida(fecha_nacimiento_str, fecha_actual_str):
    """
    Calcula los meses de vida de una persona dada su fecha de nacimiento y la fecha actual.
    
    Parámetros:
    fecha_nacimiento_str (str): La fecha de nacimiento de la persona en formato 'YYYY-MM-DD'.
    fecha_actual_str (str): La fecha actual en formato 'YYYY-MM-DD'.
    
    Retorna:
    int: El número de meses de vida.
    """
    # Convertir las cadenas a objetos datetime
    fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, '%Y-%m-%d')
    fecha_actual = datetime.strptime(fecha_actual_str, '%Y-%m-%d')
    
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
fecha_nacimiento_str = '1990-05-15'
fecha_actual_str = '2024-06-12'

meses_de_vida = calcular_meses_de_vida(fecha_nacimiento_str, fecha_actual_str)
print(f"Meses de vida: {meses_de_vida}")

