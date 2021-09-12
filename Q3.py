from matplotlib import pyplot as plt
from math import trunc

# Vai identificar se a tabela será printada com intervalo fechado em seu final, ou com intervalo aberto
tableIntervalExcludesLast = False
classSpacing = 14
frequencySpacing = 13

# (a, b, v); a=Inicio do intervalo; b=fim do intervalo; v=frequencia relativa
table = [(0, 3, 0.01), (3, 6, 0.04), (6, 9, 0.15),
         (9, 12, 0.24), (12, 15, 0.33), (15, 18, 0.23)]

batteryTotal = 200


def getBatteryQuantityFromPercentage(total, percent):
    return trunc(percent*total)


# Lista com todas as frequencias relativas
dataset = list(map(lambda x: getBatteryQuantityFromPercentage(batteryTotal, x),
               list(map(lambda x: x[2], table))))
intervals = list(map(lambda x: (x[0], x[1]), table))
datasetTuple = []


def getSpacedDataset(dataset):
    # Utilizada para criar uma lista teorica de elementos que corresponde a quantidade de baterias com valores igual ao minimo do intervalo
    # Usado para criar o dataset de plotagem do histograma
    spacedDataset = []
    for n in dataset:
        i = dataset.index(n)
        a, b = intervals[i]
        count = 0
        while count < n:
            spacedDataset.append(a)
            count += 1
    return spacedDataset


def mountDataset(funcIterator):
    return list(map(funcIterator, table))


def formatTable(cSpacing, fSpacing):
    return '{:<%d} {:<%d} {:<%d}' % (cSpacing, fSpacing, fSpacing)


def printTable(dataset):
    print(formatTable(classSpacing, frequencySpacing).format(
        "Durabilidade", "Freq. Rel.(%)", "Freq. Abs."))

    for a, b, v in dataset:
        datasetTuple.append(trunc(v*100))
        print(formatTable(classSpacing, frequencySpacing).format(
            f'{a} {"|--" if tableIntervalExcludesLast else "--"} {b if tableIntervalExcludesLast else b - 1}', f'{v*100}%', getBatteryQuantityFromPercentage(batteryTotal, v)))


print("Questão 3")
print("Duzentas baterias para automóveis de uma certa marca foram testadas quanto a sua vida util. O teste simula a utilização da bateria, acelerando seu desgaste de modo a criar uma réplica da situacao real.")
printTable(table)

# Questão 3, Letra a
print('------ Letra A -------')
print('Plotando histograma ...')

plt.style.use('ggplot')
spacedDataset = getSpacedDataset(dataset)

plt.hist(spacedDataset, bins=[0, 3, 6, 9, 12, 15, 18])
plt.title('Histograma de Durabilidade de Baterias (Frequencia)')
plt.ylabel('Frequencia')
plt.xlabel('Durabilidade (meses)')
plt.show()

# Questão 3, Letra b
print('------ Letra B -------')
below6MonthPercentage = len(
    list(filter(lambda x: x < 6, spacedDataset))) / 200
print(
    f'Resultado: Na amostra de 200 baterias, temos um total de {below6MonthPercentage*100}% de baterias que se desgastam em menos de 6 meses. Tomando esta porcentagem como base projetada em uma amostra de 2000, o fabricante teria que repor teoricamente {(below6MonthPercentage*2000)} baterias')
