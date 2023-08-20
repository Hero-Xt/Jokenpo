from random import randint
from time import sleep

def carregar():
    sleep(0.5)
    print('=-' * 25)
    print('{:^50}'.format('Carregando GAME...'))
    print('=-' * 25)
    sleep(0.5)

def jokenpo_letras():
    jo = "JO..." 
    ken = 'KEN...'
    po = 'PÔ...'
    print(f'{jo: >22}', end=" ")
    sleep(0.5)
    print(f'{ken}', end=" ")
    sleep(0.5)
    print(f'{po}')
    print('=-' * 25)
    sleep(0.5)

def fimdejogo(res):
    if (res == 'NÃO') or (res == 'NAO'):
        print('=-' * 25)
        print('{:^50}'.format('Fim de Jogo!'))
        print('=-' * 25)
        quit()

res = "SIM"
user = 'PEDRA'
op = ['PEDRA', 'PAPEL', 'TESOURA'] #opções de jogada do computador

print('=-' * 25)
print('{:~^50}'.format('jokenpô!'))
print('=-' * 25)
res = str(input("Vamos jogar? [SIM/NÃO] ")).upper().strip()

if (res == 'NÃO') or (res == 'NAO'):
    print('{:^50}'.format('Fim de Jogo!'))
    print('=-' * 25)
    quit()
while (res != 'NAO') and (res != 'NÃO') and (res != 'SIM'):
    res = str(input("ERRO! Vamos jogar? [SIM/NÃO] ")).upper().strip()
    print('=-' * 25)
    fimdejogo(res)
while res == 'SIM':
    carregar()
    user = str(input('Digite sua jogada: [PEDRA/PAPEL/TESOURA] ')).upper().strip()
    print('=-' * 25)
    sleep(0.5)
    while (user != 'PEDRA') and (user != 'PAPEL') and (user != 'TESOURA'):
        print('=-' * 25)
        user = str(input('ERRO! Digite novamente: [PEDRA/PAPEL/TESOURA] ')).upper().strip()
        print('=-' * 25)
    pc = op[randint(0, 2)]
    if user == pc:
        jokenpo_letras()
        print('          Escolhir {} também! Empatados!'.format(pc))
        print('=-' * 25)
    elif (user == 'PEDRA') and (pc == 'TESOURA'):
        jokenpo_letras()
        print('          Escolhir Tesoura. Você Venceu!')
        print('=-' * 25)
    elif (user == 'PAPEL') and (pc == 'PEDRA'):
        jokenpo_letras()
        print('          Escolhir Pedra. Você Venceu!')
        print('=-' * 25)
    elif (user == 'TESOURA') and (pc == 'PEDRA'):
        jokenpo_letras()
        print('          Escolhir Pedra. Você Perdeu!')
        print('=-' * 25)
    elif (user == 'TESOURA') and (pc == 'PAPEL'):
        jokenpo_letras()
        print('          Escolhir Papel. Você Venceu!')
        print('=-' * 25)
    elif (user == 'PAPEL') and (pc == 'TESOURA'):
        jokenpo_letras()
        print('          Escolhir Tesoura. Você Perdeu!')
        print('=-' * 25)
    elif (user == 'PEDRA') and (pc == 'PAPEL'):
        jokenpo_letras()
        print('          Escolhir Papel. Você Perdeu!')
        print('=-' * 25)
    sleep(0.5)
    res = str(input("Quer continuar? [SIM/NÃO] ")).upper().strip()
    print('=-' * 25)
    fimdejogo(res)
    while (res != 'NAO') and (res != 'NÃO') and (res != 'SIM'):
        sleep(0.5)
        print('=-' * 25)
        res = str(input("ERRO! Quer continuar? [SIM/NÃO] ")).upper().strip()
        print('=-' * 25)
        fimdejogo(res)
