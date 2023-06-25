#def mensagem(msg):
#    print(msg)

#largura = float(input('LARGURA (M): '))
#comprimento = float(input('COMPRIMENTO (M): '))
#mensagem(f'A área de um terreno {largura} x {comprimento} é de {largura * comprimento}m²')

def area():
    largura = float(input('largura(m²): '))
    comprimento = float(input('Comprimento(m²): '))
    print(f'A área desse terreno é de {largura * comprimento :.2f}m²')

area()


