import os

votosbolsonaro = 0
votoslula = 0

while True:
    print('=-' * 20)
    print(
        f'TOTAL BOLSONARO:{votosbolsonaro}{os.linesep}TOTAL LULA:{votoslula}')
    print('=-' * 20)

    try:
        voto = int(input(
            f'Para quem gostaria de votar?{os.linesep}1 - Bolsonaro{os.linesep}2 - Lula{os.linesep}seu voto: '))
        if voto == 1:
            votosbolsonaro += 1
        elif voto == 2:
            votoslula += 1
        else:
            pass
    except:
        print('Digite apenas 1 ou 2')
    os.system('cls')
