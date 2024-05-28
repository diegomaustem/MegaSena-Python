import random

def sorteio():
    jogo = []
    while len(jogo) < 6:
        numero = random.randint(1,60)
        if numero in jogo:
            continue
        else:
            jogo.append(numero)
    print('Números sorteados:', sorted(jogo))
        
sorteio()