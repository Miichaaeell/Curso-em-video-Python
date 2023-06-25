def leiaint(n):
    válidado = False
    while not válidado:
        validar = str(input(n)).strip()
        if not validar.isnumeric():
            print(f'\033[31m ERRO! \"{validar}\" não é um  número inteiro válido\033[m')
        else:
            válidado = True
            return int(validar)



def leiafloat(n):
    válidado = False
    while not válidado:
        validar = str(input(n)).strip().replace(',', '.')
        if validar.isalpha() or validar == '':
            print(f'\033[31mERRO! \"{validar}\" não é um numero real válido\033[m')
        else:
            válidado = True
            return float(validar)
