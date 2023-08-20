from random import randint
from time import sleep

def game(user, pc):
    if user == pc:
        print('                Escolhir {} também! Empatados!'.format(pc))
    elif (user == 'PEDRA') and (pc == 'TESOURA'):
        print('{:^62}'.format('Escolhir Tesoura. Você Venceu!'))
    elif (user == 'TESOURA') and (pc == 'PEDRA'):
        print('{:^62}'.format('Escolhir Pedra. Você Perdeu!'))
    elif (user == 'PAPEL') and (pc == 'PEDRA'):
        print('{:^62}'.format('Escolhir Pedra. Você Venceu!'))
    elif (user == 'PEDRA') and (pc == 'PAPEL'):
        print('{:^62}'.format('Escolhir Papel. Você Perdeu!'))
    elif (user == 'TESOURA') and (pc == 'PAPEL'):
        print('{:^62}'.format('Escolhir Papel. Você Venceu!'))
    elif (user == 'PAPEL') and (pc == 'TESOURA'):
        print('{:^62}'.format('Escolhir Tesoura. Você Perdeu!'))
    elif (user == 'PEDRA') and (pc == 'LAGARTO'):
        print('{:^62}'.format('Escolhir Lagarto. Você Venceu!'))
    elif (user == 'LAGARTO') and (pc == 'PEDRA'):
        print('{:^62}'.format('Escolhir Pedra. Você Perdeu!'))
    elif (user == 'LAGARTO') and (pc == 'SPOCK'):
        print('{:^62}'.format('Escolhir Spock. Você Venceu!'))
    elif (user == 'SPOCK') and (pc == 'LAGARTO'):
        print('{:^62}'.format('Escolhir Lagarto. Você Perdeu!'))
    elif (user == 'TESOURA') and (pc == 'SPOCK'):
        print('{:^62}'.format('Escolhir Spock. Você Venceu!'))
    elif (user == 'SPOCK') and (pc == 'TESOURA'):
        print('{:^62}'.format('Escolhir Tesoura. Você Perdeu!'))
    elif (user == 'LAGARTO') and (pc == 'PAPEL'): 
        print('{:^62}'.format('Escolhir Papel. Você Venceu!'))
    elif (user == 'PAPEL') and (pc == 'LAGARTO'):
        print('{:^62}'.format('Escolhir Lagarto. Você Perdeu!'))
    elif (user == 'PAPEL') and (pc == 'SPOCK'): 
        print('{:^62}'.format('Escolhir Spock. Você Venceu!'))
    elif (user == 'SPOCK') and (pc == 'PAPEL'):
        print('{:^62}'.format('Escolhir Papel. Você Perdeu!'))
    elif (user == 'SPOCK') and (pc == 'PEDRA'): 
        print('{:^62}'.format('Escolhir Spock. Você Venceu!'))
    elif (user == 'PEDRA') and (pc == 'SPOCK'):
        print('{:^62}'.format('Escolhir Pedra. Você Perdeu!'))
        
def regras():
    print('{:^62}\n'.format('REGRAS!!!')) , sleep(1)
    print('{:^62}'.format('Tesoura corta Papel')), sleep(1)
    print('{:^62}'.format('Papel cobre Pedra')), sleep(1)
    print('{:^62}'.format('Pedra quebra Lagarto')), sleep(1)
    print('{:^62}'.format('Lagarto envenena Spock')), sleep(1)
    print('{:^62}'.format('Spock esmaga Tesoura')), sleep(1)
    print('{:^62}'.format('Tesoura decapita Lagarto')), sleep(1)
    print('{:^62}'.format('Lagarto come Papel')), sleep(1)
    print('{:^62}'.format('Papel desmente Spock')), sleep(1)
    print('{:^62}'.format('Spock destrói Pedra')), sleep(1)
    print('{:^62}'.format(' e como sempre...')), sleep(1)
    print('{:^62}'.format('Pedra quebra Tesoura')), sleep(1)

def carregar():
    sleep(0.5), print('=-' * 31)
    print('{:^62}'.format('CARREGANDO GAME...'))
    print('=-' * 31), sleep(0.5)

def jokenpo_letras():
    jo, ken, po = "JO..." , 'KEN...' , 'PÔ...'
    print(f'{jo: >28}', end=" "), sleep(0.5)
    print(f'{ken}', end=" "), sleep(0.5)
    print(f'{po}'), print('=-' * 31), sleep(0.5)

def fimdejogo(res):
    if (res == 'NÃO') or (res == 'NAO'):
        print('=-' * 31), print('{:^62}'.format('Fim de Jogo!')), print('=-' * 31), quit()

res = "SIM"
user = 'PEDRA'
op = ['PEDRA', 'PAPEL', 'TESOURA', 'LAGARTO' , 'SPOCK'] #opções de jogada do computador

print('=-' * 31), print('=-=-=-=-=-=-=-=-=-=-=-=-=- jokenpô! =-=-=-=-=-=-=-=-=-=-=-=-=-'), print('=-' * 31)
res = str(input("                  Vamos jogar? [SIM/NÃO] ")).upper().strip()

if (res == 'NÃO') or (res == 'NAO'):
    print('{:^62}'.format('Fim de Jogo!'))
    print('=-' * 31), quit()
while (res != 'NAO') and (res != 'NÃO') and (res != 'SIM'):
    res = str(input("                ERRO! Vamos jogar? [SIM/NÃO] ")).upper().strip()
    print('=-' * 31), fimdejogo(res)
if res == "SIM":
    carregar(), regras()
while res == 'SIM':
    carregar()
    user = str(input('Digite sua jogada: [PEDRA/PAPEL/TESOURA/LAGARTO/SPOCK] ')).upper().strip()
    print('=-' * 31), sleep(0.5)
    while (user != 'PEDRA') and (user != 'PAPEL') and (user != 'TESOURA') and (user != 'LAGARTO') and (user != 'SPOCK'):
        print('=-' * 31)
        user = str(input('ERRO! Digite novamente: [PEDRA/PAPEL/TESOURA/LAGARTO/SPOCK] ')).upper().strip()
        print('=-' * 31)
    pc = op[randint(0, 4)]
    jokenpo_letras(), game(user, pc), print('=-' * 31), sleep(0.5)
    res = str(input("                Quer continuar? [SIM/NÃO] ")).upper().strip()
    print('=-' * 31), fimdejogo(res)
    while (res != 'NAO') and (res != 'NÃO') and (res != 'SIM'):
        sleep(0.5), print('=-' * 31)
        res = str(input("               ERRO! Quer continuar? [SIM/NÃO] ")).upper().strip()
        print('=-' * 31), fimdejogo(res)
