import re
import random
import itertools


def calcula(tirada):
    suma = None
    if "+" in tirada:
        dados, suma = tirada.split("+")
    else:
        dados = tirada
    m = re.match("(?i)([\d]+)d([\d]+)", dados)
    result = 0
    for _ in itertools.repeat(None, int(m.group(1))):
        result += random.randint(1, int(m.group(2)))
    if suma:
        result += int(suma)
    return result
