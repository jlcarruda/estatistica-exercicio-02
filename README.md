# Exercicio 02 - João Lucas de Carvalho Arruda
Desenvolvi todas as soluções do exercicio utilizando Python, com as seguintes dependencias:
- Python 3.9
- Matplotlib

**As soluções estão compiladas neste README, não necessitando ser feita a execução do código.**

## Como Executar (opcional)
As soluçöes estão separadas por arquivo, onde `Q1.py` se refere as resoluções da Questão 1, e assim por diante.

Para executar o código, se faz necessário apenas a instalação das dependencias e a execução de cada arquivo via terminal
```shell
> pip install -U matplotlib # Instalar a dependencia

> python ./Q1.py
```

----------

## [Questão 1](./Q1.py)
### Os dados a seguir referem-se ao tempo, em horas, que 80 pacientes hospitalizados dormiram durante a administração de certo anestésico:
| Intervalos |  Freq. Abs  |
|:-----|:--------:|
| 0 \|-- 4   | 6 |
| 4 \|-- 8   |  14  |
| 8 \|-- 12   | 24 |
| 12 \|-- 16   | 22 |
| 16 \|-- 20   | 14 |

## Letra A: Calcular a frequência relativa de cada classe.
***Os calculos desta questão foram feitos via Python***

| Intervalos |   Freq. Abs. |   Freq. Rel. |
|:---- | :----: | ----: |
0 \|-- 4   | 6 |    0.075
4 \|-- 8   |   14 |   0.175
8 \|-- 12  |   24 |   0.3
12 \|-- 16 |   22 |   0.275
16 \|-- 20 |   14 |   0.175

## Letra B: Qual é a interpretação de frequência relativa da 2a classe?
***Os calculos desta questão foram feitos via Python***
### Resposta
 A frequencia relativa da segunda classe de intervalo indica que 17,5% dos pacientes dormiram entre 4 a 7 horas, depois de terem tomado o analgesico.

## Letra C: Qual o percentual de pacientes que dormiram menos de 8 horas?
***Os calculos desta questão foram feitos via Python***
### Resposta
De 80 pacientes, 20 deles dormiram menos que 8 horas, o que corresponde a **25.0% dos pacientes**

----------

## [Questão 2](./Q2.py)
### Em um haras, verificou-se a taxa de protrombina (em segundos) no plasma de cavalos. Os dados de uma amostra de 20 cavalos são apresentados abaixo
![alt](./Q2%20Enunciado.png)

## Letra A: Construir uma tabela de frequência usando as classes de tamanho 2,0 a partir de 16,0.
***Os calculos desta questão foram feitos via Python***
| Intervalos |   Freq. Abs. |   Freq. Rel.(%) |
|:---- | :----: | ----: |
16 \|-- 19   | 3 |    15%
19 \|-- 21   |   5 |   25%
21 \|-- 23  |   6 |   30%
23 \|-- 25 |   4 |   20%
25 \|-- 27 |   2 |   10%

## Letra B: Construir o histograma.
***Histograma desta questão foi plotado usando Python e Matplotlib***
![alt](./Q2%20-%20Letra%20b%20-%20Histograma.png)
## Letra C: Em uma amostra de 70 cavalos, quantos esperamos encontrar com a taxa de protrombina abaixo de 22,0 sec?
***Os calculos desta questão foram feitos via Python***
### Resposta
Baseado na porcentagem de 60% que apresentam o valor abaixo de 22 sec em uma amostra de 20 cavalos, teriamos **42 cavalos para uma amostra de 70 cavalos**

----------

## [Questão 3](./Q3.py)
### Duzentas baterias para automóveis de uma certa marca foram testadas quanto a sua vida util. O teste simula a utilização da bateria, acelerando seu desgaste de modo a criar uma réplica da situacao real. Os resultados de durabilidade (em meses) sao apresentados a seguir:
| Intervalos |    Freq. Rel.(%) |
|:---- | ----: |
0 \|-- 3   | 1% |
3 \|-- 6   |   4% |
6 \|-- 9  |   15% |
9 \|-- 12 |   24% |
12 \|-- 15 |   33% |
15 \|-- 18 |   23% |

## Letra A: Construir o histograma.
***Histograma desta questão foi plotado usando Python e Matplotlib***
![alt](./Q3%20-%20Letra%20a%20-%20Histograma.png)

## Letra B: Se a amostra acima for considerada representativa do desempenho dessa marca de bateria, quantas, em 2000 fabricadas, serão repostas pelo fabricante, se ele oferece 6 meses de garantia?
***Os calculos desta questão foram feitos via Python***

### Resposta
Na amostra de 200 baterias, temos um total de 5.0% de baterias que se desgastam em menos de 6 meses. Tomando esta porcentagem como base projetada em uma amostra
de 2000, o fabricante teria que repor teoricamente 100.0 baterias


## [Questão 4](./Q4.py)
### Um novo medicamento para cicatrização está sendo testado e um experimento é feito para estudar o tempo (em dias) de completo fechamento em cortes provenientes de cirurgia. Uma amostra em trinta cobaias forneceu os valores:

![alt](./Q4%20Enunciado.png)
## Letra A: Organizar uma tabela de frequência.
***Os calculos desta questão foram feitos via Python***

OBS: Os intervalos foram definidos e calculados por um algoritmo

| Intervalos |   Freq. Abs. |   Freq. Rel.(%) |
|:---- | :----: | ----: |
13 \|-- 15   | 9 |    30%
15 \|-- 17   |   16 |   53.33%
17 \|-- 19  |   5 |   16.67%

## Letra B: Qual percentagem das observações fica abaixo de 16 dias?
***Os calculos desta questão foram feitos via Python***
### Resposta
De 30 cobaias para o medicamento, 60.0% das cobaias apresentaram cicatrização em um tempo abaixo de 16 dias

