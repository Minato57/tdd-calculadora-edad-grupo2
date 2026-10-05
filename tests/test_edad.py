from datetime import date
from src.edad import calcular_edad


def test_edad_cuando_ya_cumplio_anios_este_anio():
    nacimiento = date(2000, 5, 15)
    hoy = date(2026, 9, 30)
    assert calcular_edad(nacimiento, hoy) == 26