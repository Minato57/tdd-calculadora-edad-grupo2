MENSAJE_FECHA_FUTURA = "La fecha de nacimiento no puede ser posterior a la fecha actual"

def validar_fecha_nacimiento(fecha_nacimiento, fecha_actual):
    if fecha_nacimiento > fecha_actual:
        raise ValueError(MENSAJE_FECHA_FUTURA)


def ya_cumplio_anios(fecha_nacimiento, fecha_actual):
    return (fecha_actual.month, fecha_actual.day) >= (fecha_nacimiento.month, fecha_nacimiento.day)


def calcular_edad(fecha_nacimiento, fecha_actual):
    validar_fecha_nacimiento(fecha_nacimiento, fecha_actual)
    edad = fecha_actual.year - fecha_nacimiento.year
    if not ya_cumplio_anios(fecha_nacimiento, fecha_actual):
        edad -= 1
    return edad