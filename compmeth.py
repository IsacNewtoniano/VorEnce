"""
Use for methods compresings
"""
__all__ = [
'__if__',
'__match',
'__matchin__',
'__matcheq__',
'__matchne__'
]
def __if__(_if, _True, _False):
    if _if:
        return _True
    return _False

def __ifmatch__(cases):
    iten = 0
    lenght = len(cases) - 1
    if len(cases) % 2 == 0:
        while iten < lenght:
            if cases[iten]:
                return cases[iten + 1]
            else:
                iten += 2
    else:
        what_is = f'what is {cases[lenght]}? use comparation + return\n{cases[::2]}'
        raise TypeError(what_is)
def __matchin__(object, cases):
    iten = 0
    lenght = len(cases) - 1
    if len(cases) % 2 == 0:
        while iten < lenght:
            if object in cases[iten]:
                return cases[iten + 1]
            else:
                iten += 2
    else:
        what_is = f'what is {cases[lenght]}? use comparation + return\n{cases[::2]}'
        raise TypeError(what_is)
def __matcheq__(object : str | list | float | int, cases : list):
    iten = 0
    lenght = len(cases) - 1
    if len(cases) % 2 == 0:
        while iten < lenght:
            if object == cases[iten]:
                return cases[iten + 1]
            else:
                iten += 2
        return False
    what_is = f'what is {cases[lenght]}? use comparation + return\n{cases[::2]}'
    raise TypeError(what_is)

def __matchne__(object, cases):
    iten = 0
    lenght = len(cases) - 1
    if len(cases) % 2 == 0:
        while iten < lenght:
            if object != cases[iten]:
                return cases[iten + 1]
            else:
                iten += 2
    else:
        what_is = f'what is {cases[lenght]}? use comparation + return\n{cases[::2]}'
        raise TypeError(what_is)

def __matchlt__(object, cases):
    iten = 0
    lenght = len(cases) - 1
    if len(cases) % 2 == 0:
        while iten < lenght:
            if object < cases[iten]:
                return cases[iten + 1]
            else:
                iten += 2
    else:
        what_is = f'what is {cases[lenght]}? use comparation + return\n{cases[::2]}'
        raise TypeError(what_is)

def __matchgt__(object, cases):
    iten = 0
    lenght = len(cases) - 1
    if len(cases) % 2 == 0:
        while iten < lenght:
            if object > cases[iten]:
                return cases[iten + 1]
            else:
                iten += 2
    else:
        what_is = f'what is {cases[lenght]}? use comparation + return\n{cases[::2]}'
        raise TypeError(what_is)

def __matchle__(object, cases):
    iten = 0
    lenght = len(cases) - 1
    if len(cases) % 2 == 0:
        while iten < lenght:
            if object <= cases[iten]:
                return cases[iten + 1]
            else:
                iten += 2
    else:
        what_is = f'what is {cases[lenght]}? use comparation + return\n{cases[::2]}'
        raise TypeError(what_is)

def __matchge__(object, cases):
    iten = 0
    lenght = len(cases) - 1
    if len(cases) % 2 == 0:
        while iten < lenght:
            if object >= cases[iten]:
                return cases[iten + 1]
            else:
                iten += 2
    else:
        what_is = f'what is {cases[lenght]}? use comparation + return\n{cases[::2]}'
        raise TypeError(what_is)

def __concat__(object1 : type = None, object2 : type = None):
    if type(object1) in [str]:
        if type(object2) in [str, int, float]:
            return f"{object1}{object2}"
        what_is = f'What is {object2}: Use string, integer or floater, No {type(object2)}'
        raise what_is
    what_is = f'What is {object1}? Use string, No {type(object1)}'
    raise TypeError(what_is)
def __fileor__(_file : str = '', eccoding : str = 'r'):
    if _file:
        file = open(f'{_file}', eccoding).read()
        return file
def __execute__(filename):
    f = open(filename, 'r')
    a = f.read()
    f.close()
    return a

def raiz_quadrada(x):
    if x < 0:
        raise ValueError("Não é possível calcular a raiz quadrada de um número negativo.")
    epsilon = 1e-6  # Precisão desejada
    guess = x / 2.0  # A primeira suposição
    while abs(guess * guess - x) > epsilon:
        guess = (guess + x / guess) / 2.0
    return guess

# Teste
numero = 26965
resultado = raiz_quadrada(numero)
print(f"A raiz quadrada de {numero} é aproximadamente {resultado}.")
