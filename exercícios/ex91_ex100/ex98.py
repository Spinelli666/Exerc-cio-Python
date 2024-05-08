from time import sleep

def contador(start, end, step):
    if step < 0:
        step *= -1
    if step == 0:
        step = 1
    print('-=' * 20)
    print(f'Contagem de {start} até {end} de {step} em {step}')
    sleep(2.5)

    if start < end:
        cont = start
        while cont <= end:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont += step
        print('FIM!')
    else:
        cont = start
        while cont >= end:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont -= step
        print('FIM!')



contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')

start = int(input('Início: '))
end = int(input('Fim: '))
step = int(input('Passo: '))
contador(start, end, step)