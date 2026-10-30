"""
def funcaoA(num):
    if (num == 0):
        return

    funcaoA(num - 1)
    print("A")

funcaoA(5)
"""
"""
def calculaFatorial(num):
    if (num == 0 or num == 1):
        return 1

    return num * calculaFatorial(num - 1)

fat = calculaFatorial(5)
print(fat)
"""
"""
def calculaElevado(base, expoente):
    if (expoente == 0):
        return 1

    return base * calculaElevado(base, expoente - 1)

elevado = calculaElevado(2, 3)
print(elevado)
"""

"""
def intToBin(num):
    print("converter um
     numero inteiro em binario recursivamente")
    
def binToInt(texto):
    print("converter texto binário em um numero inteiro")
""" 
"""
def intToBinary(num):
    if (num == 0):
        return "0"
    elif (num == 1):
        return "1"
    else:
        return intToBinary(num // 2) + str(num % 2)

bin = intToBinary(13)
print(bin)
"""
def binToInt(texto):
    if (texto == "0"):
        return 0
    elif (texto == "1"):
        return 1
    else:
        return int(texto[0]) * (2 ** (len(texto) - 1)) + binToInt(texto[1:])
con = binToInt("1101")
print(con)
