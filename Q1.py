print('Questão 1')
print('Os dados a seguir referem-se ao tempo, em horas, que 80 pacientes hospitalizados dormiram durante a administração de certo anestésico:')

# (a, b, v); a=min do intervalo; b=max do intervalo; v=freq. abs.
dataset = [(0, 4, 6), (4, 8, 14), (8, 12, 24), (12, 16, 22), (16, 20, 14)]

table = []

patients = 80

# Vai identificar se a tabela será printada com intervalo fechado em seu final, ou com intervalo aberto
tableIntervalExcludesLast = True

classSpacing = 12
frequencySpacing = 12


def formatTable(cSpacing, fSpacing):
    return '{:<%d} {:<%d} {:<%d}' % (cSpacing, fSpacing, fSpacing)


def printTable():
    # Table header
    print(formatTable(classSpacing, frequencySpacing).format(
        "Intervalos", "Freq. Abs.", "Freq. Rel."))
    for a, b, v in dataset:
        freqRel = v/patients
        table.append((a, b, v, freqRel))
        print(formatTable(classSpacing, frequencySpacing).format(
            f'{a} {"|--" if tableIntervalExcludesLast else "--"} {b if tableIntervalExcludesLast else b - 1}', v, f'{freqRel}'))


print()
print('===== Letra A ====')
printTable()

print()
print('===== Letra B =====')
print('A frequencia relativa da segunda classe de intervalo indica que 17,5% dos pacientes dormiram entre 4 a 7 horas, depois de terem tomado o analgesico.')

print()
print('===== Letra C =====')
below8Hours = 6 + 14  # Soma da Freq Absoluta das duas primeiras classes de intervalo
percentage = below8Hours / patients
print(
    f'Resultado: de 80 pacientes, {below8Hours} deles dormiram menos que 8 horas, o que corresponde a {percentage*100}% dos pacientes')
