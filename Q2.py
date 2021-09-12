from matplotlib import pyplot as plt
from math import sqrt, trunc

# Questão 2
# Letra a)
print('Questão 2')
print('===== Letra A =====')
horses = [20.6, 23.1, 16.8, 21.3, 22.1, 20.1, 21.4, 24.2, 21, 23.6,
          25.1, 18.5, 22.8, 20.2, 25.8, 19.2, 20.9, 23.4, 18.1, 21.9]

intervals = [(16, 19), (19, 21), (21, 23), (23, 25), (25, 27)]

# (a, b, v); a=Inicio da classe; b=fim da classe; v=frequencia absoluta
table = []

# Vai identificar se a tabela será printada com intervalo fechado em seu final, ou com intervalo aberto
tableIntervalExcludesLast = True

classSpacing = 12
frequencySpacing = 12


def getFrequencyClass(a, b, v):
    if v >= a and v < b:
        return 1
    return 0


def getIntervalBins(dataset, width=0):
    n = len(dataset)
    Range = trunc(max(dataset)) - trunc(min(dataset))
    intervals = sqrt(n)
    intervalWidth = (Range / intervals) if width == 0 else width

    interval = trunc(min(dataset))
    bins = []
    while(interval <= trunc(max(dataset)) + intervalWidth):
        bins.append(interval)
        interval += intervalWidth
    return bins


def formatTable(cSpacing, fSpacing):
    return '{:<%d} {:<%d} {:<%d}' % (cSpacing, fSpacing, fSpacing)


# Table header
print(formatTable(classSpacing, frequencySpacing).format(
    "Intervalos", "Freq. Abs.", "Freq. Rel.(%)"))

for a, b in intervals:
    count = 0
    for v in horses:
        count += getFrequencyClass(a, b, v)
    freqRel = count / len(horses)
    table.append((a, b, count, freqRel))
    print(formatTable(classSpacing, frequencySpacing).format(
        f'{a} {"|--" if tableIntervalExcludesLast else "--"} {b if tableIntervalExcludesLast else b - 1}', count, f'{freqRel*100}%'))


# Questão 2
# Letra b
print()
print('===== Letra B =====')
print('Mostrando gráfico de histograma ...')

plt.style.use('ggplot')
plt.hist(horses, bins=getIntervalBins(horses, 2))
plt.title('Histograma de Frequencia (Cavalos)')
plt.ylabel('Frequencia')
plt.xlabel('Intervalos')
plt.show()


# Questão 2
# Letra c
print()
print('===== Letra C =====')
# Pegar as Frequencias Relativas de cada classe
below22Horses = len(list(filter(lambda h: h <= 22, horses)))
below22Percentage = below22Horses / len(horses)
result = below22Percentage * 70
print(
    f'Resultado: Baseado na porcentagem de {trunc(below22Percentage * 100)}% que apresentam o valor abaixo de 22 sec em uma amostra de 20 cavalos, teriamos {trunc(result)} cavalos para uma amostra de 70 cavalos')
