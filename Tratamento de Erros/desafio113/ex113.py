from desafio113.funções import numero
try:
    int = numero.leiaint('Digite um valor inteiro: ')
except KeyboardInterrupt:
    print('\n\033[31mUsuário decidiu não informar esse valor\033[m')
    int = 0
try:
    real = numero.leiafloat('Digite um valor real: ')
except ValueError:
    print('\033[31mERRO! Dados inseridos de forma incorreta\033[m')
    real = str('não foi informado corretamente')
except KeyboardInterrupt:
    print('\n\033[31mUsuário decidiu não informar esse valor\033[m')
    real = 0
finally:
    print(f'O valor inteiro é {int} e o real {real}')

