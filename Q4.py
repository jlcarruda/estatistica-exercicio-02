from math import trunc, sqrt

print('Questão 3')
print('Um novo medicamento para cicatrização está sendo testado e um experimento é feito para estudar o tempo (em dias) de completo fechamento em cortes provenientes de cirurgia. Uma amostra em trinta cobaias forneceu os valores:')

dataset = [14, 16, 15, 14, 16, 17, 16, 15, 15, 16, 14, 17, 13, 15,
           14, 13, 16, 15, 16, 17, 17, 16, 15, 15, 13, 15, 17, 15, 14, 13]

print(dataset)

# (a, b, v); a=Inicio da classe; b=fim da classe; v=frequencia absoluta
table = []

# Vai identificar se a tabela será printada com intervalo fechado em seu final, ou com intervalo aberto
tableIntervalExcludesLast = True

classSpacing = 18
frequencySpacing = 10


def getFrequencyClass(a, b, v):
    if v >= a and v < b:
        return 1
    return 0


def getIntervalBins(dataset, width=0):
    n = len(dataset)
    Range = trunc(max(dataset)) - trunc(min(dataset))
    intervals = sqrt(n)
    intervalWidth = max(
        [round((Range / intervals) if width == 0 else width), 2])

    interval = trunc(min(dataset))
    bins = []
    while(interval <= trunc(max(dataset)) + intervalWidth):
        bins.append((round(interval, 2), round(
            interval + intervalWidth, 2)))
        interval += intervalWidth
    return bins


def formatTable(cSpacing, fSpacing):
    return '{:<%d} {:<%d} {:<%d}' % (cSpacing, fSpacing, fSpacing)


def printTable(dataset, intervals):
    print(formatTable(classSpacing, frequencySpacing).format(
        "Intervalos", "Freq. Abs.", "Freq. Rel.(%)"))
    for a, b in intervals:
        count = 0
        for v in dataset:
            count += getFrequencyClass(a, b, v)
        freqRel = count / len(dataset)
        table.append((a, b, count, freqRel))
        if (count > 0):
            print(formatTable(classSpacing, frequencySpacing).format(
                f'{a} {"|--" if tableIntervalExcludesLast else "--"} {b if tableIntervalExcludesLast else b - 1}', count, f'{round(freqRel*100, 2)}%'))


print("===== Letra A =====")
print("Tabela de Frequencia")

printTable(dataset, getIntervalBins(dataset))

print("===== Letra B =====")
below16Days = len(list(filter(lambda x: x < 16, dataset)))
print(f'Resultado: De {len(dataset)} cobaias para o medicamento, {(below16Days/len(dataset)) * 100}% das cobaias apresentaram cicatrização em um tempo abaixo de 16 dias')
