from testing.prueba import get_pokemones
import requests

class MockWrongResponse:
    @staticmethod
    def json():
        return{
            'abilities': []
        }
    status_code = 404

class MockCorrectResponse:
    @staticmethod
    def json():
        return{
            'abilities': []
        }
    status_code = 200



def mockWrongGet(*args, **kwargs):
    return MockWrongResponse()

def mockCorrectGet(*args, **kwargs):
    return MockCorrectResponse()



def test_get_pokemones_no_existe(monkeypatch):
    monkeypatch.setattr(requests,'get', mockWrongGet)
    resultado = get_pokemones('pikacho')
    assert resultado == 'Error con la API'

def test_get_pokemones_existe(monkeypatch):
    monkeypatch.setattr(requests,'get', mockCorrectGet)
    resultado = get_pokemones('pikachu')
    print(resultado)
    assert len(resultado['abilities']) == 0