import pytest
from datetime import date
from src.edad import calcular_edad


def test_edad_cuando_ya_cumplio_anios_este_anio():
    nacimiento = date(2000, 5, 15)
    hoy = date(2026, 9, 30)
    assert calcular_edad(nacimiento, hoy) == 26
    

def test_edad_cuando_aun_no_cumple_anios_este_anio():
    nacimiento = date(2000, 12, 10)
    hoy = date(2026, 9, 30)
    assert calcular_edad(nacimiento, hoy) == 25


def test_edad_el_dia_del_cumpleanios():
    nacimiento = date(2000, 9, 30)
    hoy = date(2026, 9, 30)
    assert calcular_edad(nacimiento, hoy) == 26


def test_fecha_nacimiento_futura_lanza_excepcion():
    nacimiento = date(2027, 1, 1)
    hoy = date(2026, 9, 30)
    with pytest.raises(ValueError, match="posterior a la fecha actual"):
        calcular_edad(nacimiento, hoy)



def test_bisiesto_un_dia_antes_del_cumpleanios():
    nacimiento = date(2004, 2, 29)
    hoy = date(2025, 2, 28)
    assert calcular_edad(nacimiento, hoy) == 20


def test_bisiesto_cumple_el_1_de_marzo():
    nacimiento = date(2004, 2, 29)
    hoy = date(2025, 3, 1)
    assert calcular_edad(nacimiento, hoy) == 21


def test_bisiesto_en_anio_bisiesto():
    nacimiento = date(2004, 2, 29)
    hoy = date(2028, 2, 29)
    assert calcular_edad(nacimiento, hoy) == 24