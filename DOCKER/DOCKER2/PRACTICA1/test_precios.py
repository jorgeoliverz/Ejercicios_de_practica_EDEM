from precios import precio_final
from precios import precio_finali

def test_con_descuento():
    assert precio_final(100, 20) == 80
    
def test_sin_descuento():
    assert precio_final(50) == 50
    
#EXTRA:

def test_precio_con_iva():
    assert precio_finali(100, 21) == 121