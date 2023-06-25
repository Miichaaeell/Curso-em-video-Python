def voto(nascimento):
    from datetime import date
    idade = date.today().year - nascimento
    if idade < 18:
        return print(f'Com {idade} anos NÂO VOTA')
    elif idade <= 64:
        return(print(f'Com {idade} anos VOTO OBBRIGATÓRIO'))
    elif idade >= 65:
        return(print(f'Com {idade} anos VOTO OPCIONAL'))

voto(int(input('Em que ano você nasceu?')))