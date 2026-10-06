from datetime import date

import pytest

from src.edad import calcular_edad

HOY = date(2026, 9, 30)
NACIMIENTO_BISIESTO = date(2004, 2, 29)


# ---------- RF1: calcular la edad ----------
def test_edad_cuando_ya_cumplio_anios_este_anio():
    assert calcular_edad(date(2000, 5, 15), HOY) == 26


# ---------- RF2: cumpleanios pendiente ----------
def test_edad_cuando_aun_no_cumple_anios_este_anio():
    assert calcular_edad(date(2000, 12, 10), HOY) == 25


def test_edad_el_dia_del_cumpleanios():
    assert calcular_edad(date(2000, 9, 30), HOY) == 26


# ---------- RF3: fecha no valida ----------
def test_fecha_nacimiento_futura_lanza_excepcion():
    with pytest.raises(ValueError, match="posterior a la fecha actual"):
        calcular_edad(date(2027, 1, 1), HOY)


# ---------- RF4: anios bisiestos ----------
def test_bisiesto_un_dia_antes_del_cumpleanios():

    assert calcular_edad(NACIMIENTO_BISIESTO, date(2025, 2, 28)) == 20


def test_bisiesto_cumple_el_1_de_marzo():
    assert calcular_edad(NACIMIENTO_BISIESTO, date(2025, 3, 1)) == 21


def test_bisiesto_en_anio_bisiesto():
    assert calcular_edad(NACIMIENTO_BISIESTO, date(2028, 2, 29)) == 24