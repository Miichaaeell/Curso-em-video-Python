from time import sleep
def maior(* num):
    print('-='*20)
    print('Analisando os valores passados...')
    mai = 0
    for n in num:
        if n > mai:
            mai = n
        print(n, end=' ')
        sleep(0.5)
    print(f'Foram informados {len(num)} valores ao todo')
    print(f'O maior valor informado foi de {mai}')

maior(2, 9, 4, 5, 7, 1)
maior(7, 7, 0)
maior(1, 2)
maior(6)
maior()