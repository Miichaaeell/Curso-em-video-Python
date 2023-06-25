def LeiaDinheiro(msg):
    valido = False
    while not valido:
        entradaa = str(input(msg)).strip().replace(',', '.')
        if entradaa.isalpha() or entradaa == '':
            print(f'\033[31mERRO! \"{entradaa}\" não é um valor válido\033[m')
        else:
            valido =True
            return float(entradaa)