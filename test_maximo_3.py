import pytest

import maximo_3 as max3

def test_3_numeros():
  assert max3.maximo_3(1,2,3) == 3

def test_avalia_se_tem_apenas_numeros():
  with pytest.raises(TypeError) as e:
    assert max3.maximo_3("casa","panela",1)

def test_3_numeros_iguais():
  assert max3.maximo_3(1,1,1) == 1


