from time import sleep
from emoji import emojize
#DECLARAÇÃO DE VARIÁVEIS

#ARMAZENAMENTO DOS DADOS DAS CIVILIZAÇÕES:

#EGIPCIOS
local1 = str('Rio Nilo')
nascimento1 = str('3.100 a.C')
escrita1 = str('Hieróglifo')
moeda1 = str('Dracma')
caracter1 = str ('Mumificação de faraós;\nPirâmides como túmulos;\nUso do calendário solar;\nGovernado pela monarquia Teocrática;\nReligião politeísta;\nEconomia fundamentada na agricultura, cultivo de animais e mineração;\nSociedade hierarquizada e pratiarcal')

#MESOPOTÂMIA
local2 = str('Entre rio Tigre e rio Eufrates')
nascimento2 = str('7.000 a.C')
escrita2 = str('Cuneiforme')
moeda2 = str('Grãos de cevada como meio de troca de mercadorias ou anéis fabricados a partir de conchas.')
caracter2 = str('A primeira civilização do mundo;\nConhecida pelas terras férteis para agricultura;\nDeu origem à literatura e escrita;\nCriou o código de Hamurabi;\nElementos da natureza e astronômicos eram divindades;\nCriação e uso do calendário Lunar.')

#CHINESA
local3 = str ('Rio Amarelo (Huang-Ho)')
nascimento3 = str ('3.000 a.C')
escrita3 = str ('Osso oráculo')
moeda3 = str ('yǐ Bí qián / Ying Yuan')
caracter3 = str ('Uma das civilizações mais antigas do mundo;\nTerra onde foram encontrados os primeiros vestígios fósseis Homem de Pequim;\nDesenvolvimento econômico baseado na agricultura;\nPioneiros na criação de muitos itens importantes para todas as fases da sociedade, inclusive a atual;\nPrecursores no desenvolvimento de técnicas medicinais;\nReligião baseada na devoção de antepassados da realeza.')

#HEBRAICA
local4 = str ('Rio Jordão')
nascimento4 = str ('2.000 a.C')
escrita4 = str ('Aramaico')
moeda4 = str ('Shekel')
caracter4 = str ('Civilização seminômade de origem semita;\nSociedade patriarcal;\nEconomia baseada em agropastoris;\nReligião monoteísta;\nPovo conhecido pela criação da literatura salmista e apocalíptica;\nReconhecida como uma das maiores Monarquias da história.')

#FENÍCIA
local5 = str ('Mar Mediterrâneo')
nascimento5 = str ('3.000 a.C')
escrita5 = str ('Abjad')
moeda5 = str ('Moeda Fenícia – Ouro')
caracter5 = str ('Cidades governadas por reis independentes;\nMercado forte em construção naval e comércio entre povos;\nDestaque no mercado de produção artesanal de joias e tecidos;\nReligião politeísta e Animista;\nTeve grande participação na arquitetura e construções de importantes templos;\nCriou o sistema de escrita, ou alfabeto, formado por 22 letras.')

#PERSA
local6 = str ('Entre Golfo Pérsico e Mar Cáspio')
nascimento6 = str ('2.000 a.C')
escrita6 = str ('Perso-árabe (fârsi)')
moeda6 = str ('Dárico')
caracter6 = str ('Governo expansionista;\nCom a grande extensão do império, criou-se uma administração política descentralizada;\nAs cidades contavam com staprias para o recolhimento de impostos;\nOs povos do império podiam seguir com suas culturas e crenças, desde que pagassem os impostos estabelecidos;\nCultura rica no artesanato de tapetes persas e itens luxuosos;\nReligião Zoroastrismo ou Masdeísmo.')

#LISTA DAS VARIAVEIS
egipcia = [local1, nascimento1, escrita1, moeda1,caracter1]
mesopotamia = [local2,nascimento2,escrita2,moeda2,caracter2]
chinesa = [local3,nascimento3,escrita3,moeda3,caracter3]
hebraica = [local4,nascimento4,escrita4,moeda4,caracter4]
fenicia = [local5,nascimento5,escrita5,moeda5,caracter5]
persa = [local6,nascimento6,escrita6,moeda6,caracter6]

print('')
print (emojize('\033[1m' + 'Sociedades\033[91m :eagle: \033[0m\033[1mAncestrais' + '\033[0m'))
print('')
print('Software destinado ao estudo de antigas civilizações terrestres.\n''\n\033[36mEm desenvolvimento\033[0m')
input('\n\033[1m''Dê Enter para começar'+'\033[0m')
sleep(0)
programa = True
while (programa == True):
    print('\033[95m'+'Escolha uma das civilizações listadas logo abaixo, utilizando o seu respectivo código.'+'\033[0m')
    print ('\033[36m'+'-=-'*10+'\033[0m')
    print('\033[94m'+'Civilização Egipcia\nCÓDIGO --> CE1'+'\033[0m')
    print ('\033[36m'+'-=-'*10+'\033[0m')
    print ('\033[94m'+ 'Civilização Mesopotâmica\nCÓDIGO --> CM2'+'\033[93m')
    print ('\033[36m'+'-=-'*10+'\033[0m')
    print ('\033[94m'+'Civilização Chinesa\nCÓDIGO --> CC3' + '\033[0m')
    print ('\033[36m'+'-=-'*10+'\033[0m')
    print ('\033[94m'+'Civilização Hebraica\nCÓDIGO --> CH4' + '\033[0m')
    print ('\033[36m'+'-=-'*10+'\033[0m')
    print ('\033[94m'+'Civilização Fenícia\nCÓDIGO --> CF5' + '\033[0m')
    print ('\033[36m'+'-=-'*10+'\033[0m')
    print ('\033[94m'+'Civilização Persa\nCÓDIGO --> CP6' + '\033[0m')
    print ('\033[36m'+'-=-'*10+'\033[0m')
    print ('\033[94m'+'Civilização Hindú\nCÓDIGO --> CH7' + '\033[0m')
    print ('\033[36m'+'-=-'*10+'\033[0m')
    print ('\033[94m'+'Civilização Persa\nCÓDIGO --> CP8' + '\033[0m')
    print ('\033[36m'+'-=-'*10+'\033[0m')
    print ('\033[94m'+'Civilização Cretense\nCÓDIGO --> CC9' + '\033[0m')
    print ('\033[36m'+'-=-'*10+'\033[0m')
    escolha = input('Introduza o código:').strip().upper()
    print('\033[7;91mPROCESSANDO...\033[0m')
    sleep(1.2)
    print('')
    print('\033[7;91mPROCESSANDO...\033[0m')
    sleep(1.4)
    print('')
    if escolha =='CE1':
        escolha_continuar_ou_encerrar = str(input('\033[1;94mVocê escolheu conhecer mais sobre os egípcios. Dados sobre essa civilização:\033[36m\n'+'-'*18+'\n'f'Local: {egipcia[0]}\n' + '-'*18 +'\n'f'Nascimento: {egipcia[1]}\n'+ '-'*18 +'\n'f'Escrita: {egipcia[2]}\n'+ '-'*18 + '\n'f'Moeda: {egipcia[3]}\n' + '-'*18 + '\n'f'Caracteristicas:\n\n{egipcia[4]}\n\033[0m\n\033[1mDeseja continuar estudando outras civilizações ou encerrar o programa?\n"Continuar ou Encerrar"\n->\033[0m')).strip().upper()
        if escolha_continuar_ou_encerrar == 'CONTINUAR':
            programa = True
        if escolha_continuar_ou_encerrar == 'ENCERRAR':
            programa = False
            print('Encerrando...')
        if escolha_continuar_ou_encerrar != ('CONTINUAR') and escolha_continuar_ou_encerrar != ('ENCERRAR'):
            segunda_escolha_continuar_ou_encerrar = input('Você não escolheu nenhuma das opções listadas.\nEscolha entre: Continuar ou Encerrar.\n->').strip().upper()
            if segunda_escolha_continuar_ou_encerrar != 'CONTINUAR':
                programa = False
            else:
                programa = True

    if escolha =='CM2':
        escolha_continuar_ou_encerrar = str(input('\033[1;94mVocê escolheu conhecer mais sobre a Mesopotâmia. Dados sobre essa civilização:\033[36m\n'+'-'*18+'\n'f'Local: {mesopotamia[0]}\n' + '-'*18 +'\n'f'Nascimento: {mesopotamia[1]}\n'+ '-'*18 +'\n'f'Escrita: {mesopotamia[2]}\n'+ '-'*18 + '\n'f'Moeda: {mesopotamia[3]}\n' + '-'*18 + '\n'f'Caracteristicas:\n\n{mesopotamia[4]}\n\033[0m\n\033[1mDeseja continuar estudando outras civilizações ou encerrar o programa?\n"Continuar ou Encerrar"\n->\033[0m')).strip().upper()
        if (escolha_continuar_ou_encerrar == 'CONTINUAR'):
            programa = True
        if (escolha_continuar_ou_encerrar == 'ENCERRAR'):
            programa = False
            print('Encerrando...')
        if escolha_continuar_ou_encerrar != ('CONTINUAR') and escolha_continuar_ou_encerrar != ('ENCERRAR'):
            segunda_escolha_continuar_ou_encerrar = input('Você não escolheu nenhuma das opções listadas.\nEscolha entre: Continuar ou Encerrar.\n->').strip().upper()
            if segunda_escolha_continuar_ou_encerrar != 'CONTINUAR':
                programa = False
            else:
                programa = True



    if escolha == 'CC3':
        escolha_continuar_ou_encerrar = str(input('\033[1;94mVocê escolheu conhecer mais sobre os chineses. Dados sobre essa civilização:\033[36m\n'+'-'*18+'\n'f'Local: {chinesa[0]}\n' + '-'*18 +'\n'f'Nascimento: {chinesa[1]}\n'+ '-'*18 +'\n'f'Escrita: {chinesa[2]}\n'+ '-'*18 + '\n'f'Moeda: {chinesa[3]}\n' + '-'*18 + '\n'f'Caracteristicas:\n\n{chinesa[4]}\n\033[0m\n\033[1m Deseja continuar estudando outras civilizações ou encerrar o programa?\n"Continuar ou Encerrar"\n->\033[0m')).strip().upper()
        if escolha_continuar_ou_encerrar == 'CONTINUAR':
            programa = True
        if escolha_continuar_ou_encerrar == 'ENCERRAR':
            programa = False
            print('Encerrando...')
        if escolha_continuar_ou_encerrar != ('CONTINUAR') and escolha_continuar_ou_encerrar != ('ENCERRAR'):
            segunda_escolha_continuar_ou_encerrar = input('Você não escolheu nenhuma das opções listadas.\nEscolha entre: Continuar ou Encerrar.\n->').strip().upper()
            if segunda_escolha_continuar_ou_encerrar != 'CONTINUAR':
                programa = False
            else:
                programa = True

    if escolha == 'CH4':
        escolha_continuar_ou_encerrar = str(input('\033[1;94mVocê escolheu conhecer mais sobre os hebraicos. Dados sobre essa civilização:\033[36m\n'+'-'*18+'\n'f'Local: {hebraica[0]}\n' + '-'*18 +'\n'f'Nascimento: {hebraica[1]}\n'+ '-'*18 +'\n'f'Escrita: {hebraica[2]}\n'+ '-'*18 + '\n'f'Moeda: {hebraica[3]}\n' + '-'*18 + '\n'f'Caracteristicas:\n\n{hebraica[4]}\n\033[0m\n\033[1m Deseja continuar estudando outras civilizações ou encerrar o programa?\n"Continuar ou Encerrar"\n->\033[0m')).strip().upper()
        if escolha_continuar_ou_encerrar == 'CONTINUAR':
            programa = True
        if escolha_continuar_ou_encerrar == 'ENCERRAR':
            programa = False
            print('Encerrando...')
        if escolha_continuar_ou_encerrar != ('CONTINUAR') and escolha_continuar_ou_encerrar != ('ENCERRAR'):
            segunda_escolha_continuar_ou_encerrar = input('Você não escolheu nenhuma das opções listadas.\nEscolha entre: Continuar ou Encerrar.\n->').strip().upper()
            if segunda_escolha_continuar_ou_encerrar != 'CONTINUAR':
                programa = False
            else:
                programa = True

    if escolha == 'CF5':
        escolha_continuar_ou_encerrar = str(input('\033[1;94mVocê escolheu conhecer mais sobre os fenícios. Dados sobre essa civilização:\033[36m\n'+'-'*18+'\n'f'Local: {fenicia[0]}\n' + '-'*18 +'\n'f'Nascimento: {fenicia[1]}\n'+ '-'*18 +'\n'f'Escrita: {fenicia[2]}\n'+ '-'*18 + '\n'f'Moeda: {fenicia[3]}\n' + '-'*18 + '\n'f'Caracteristicas:\n\n{fenicia[4]}\n\033[0m\n\033[1m Deseja continuar estudando outras civilizações ou encerrar o programa?\n"Continuar ou Encerrar"\n->\033[0m')).strip().upper()
        if escolha_continuar_ou_encerrar == 'CONTINUAR':
            programa = True
        if escolha_continuar_ou_encerrar == 'ENCERRAR':
            programa = False
            print('Encerrando...')
        if escolha_continuar_ou_encerrar != ('CONTINUAR') and escolha_continuar_ou_encerrar != ('ENCERRAR'):
            segunda_escolha_continuar_ou_encerrar = input('Você não escolheu nenhuma das opções listadas.\nEscolha entre: Continuar ou Encerrar.\n->').strip().upper()
            if segunda_escolha_continuar_ou_encerrar != 'CONTINUAR':
                programa = False
            else:
                programa = True

    if escolha == 'CP6':
        escolha_continuar_ou_encerrar = str (input('\033[1;94mVocê escolheu conhecer mais sobre os persas. Dados sobre essa civilização:\033[36m\n'+'-'*18+'\n'f'Local: {persa[0]}\n' + '-'*18 +'\n'f'Nascimento: {persa[1]}\n'+ '-'*18 +'\n'f'Escrita: {persa[2]}\n'+ '-'*18 + '\n'f'Moeda: {persa[3]}\n' + '-'*18 + '\n'f'Caracteristicas:\n\n{persa[4]}\n\033[0m\n\033[1m Deseja continuar estudando outras civilizações ou encerrar o programa?\n"Continuar ou Encerrar"\n->\033[0m')).strip().upper()
        if escolha_continuar_ou_encerrar == 'CONTINUAR':
            programa = True
        if escolha_continuar_ou_encerrar == 'ENCERRAR':
            programa = False
            print('Encerrando...')
        if escolha_continuar_ou_encerrar != ('CONTINUAR') and escolha_continuar_ou_encerrar != ('ENCERRAR'):
            segunda_escolha_continuar_ou_encerrar = input('Você não escolheu nenhuma das opções listadas.\nEscolha entre: Continuar ou Encerrar.\n->').strip().upper()
            if segunda_escolha_continuar_ou_encerrar != 'CONTINUAR':
                programa = False
            else:
                programa = True

    if (escolha != 'CE1') and (escolha != 'CM2') and (escolha != 'CC3') and (escolha != 'CH4') and (escolha != 'CF5') and (escolha != 'CP6') and (escolha != 'CONTINUAR') and (escolha != 'ENCERRAR'):
       escolha_continuar_ou_encerrar = str(input(f'\033[91mCódigo "{escolha}" inexistente.\nVocê não escolheu nenhuma das opções listadas.\033[0m\nDeseja continuar ou encerrar o programa?\n"Continuar" ou "Encerrar"?\n-> :')).strip().upper()
       if escolha_continuar_ou_encerrar == 'CONTINUAR':
        programa = True
       if escolha_continuar_ou_encerrar == 'ENCERRAR':
        programa = False
       if (escolha_continuar_ou_encerrar != 'CONTINUAR') and (escolha_continuar_ou_encerrar !='ENCERRAR'):
        segunda_escolha_continuar_ou_encerrar = input('Você não escolheu nenhuma das opções listadas.\nEscolha entre: Continuar ou Encerrar.\n->').strip().upper()
        if segunda_escolha_continuar_ou_encerrar != 'CONTINUAR':
            print('Você escolheu não continuar.')
            programa = False
        else:
            programa = True

if (programa == False):
    print('Até logo!')
    sleep(0.5)
    print('\033[1mEncerrado com sucesso.\033[0m')