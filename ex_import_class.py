from math import ceil
totalPeso = 0
totalCaixa = 0
pesoMaximo = float(input('Qual o peso máximo suportado? '))
while True:

    peso = float(input('Qual o peso da caixa? '))
    quantidadecx = 1
    totalPeso += peso
    totalCaixa += quantidadecx
    levavel = totalPeso / pesoMaximo
    if peso > 0:
        print(f'O total de peso foi: {totalPeso}, o total de caixa foi {totalCaixa} e as viagens necessárias é: {ceil(levavel)}')
    else:

        break
