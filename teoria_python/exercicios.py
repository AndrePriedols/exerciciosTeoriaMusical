#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys

import random

def intervalos(fundamentais):
    acertos = 0
    erros = 0
    tentativas = 0
    taxa = 0.0
    resposta = ''
    encerrar = 'Menu'
    desisto = 'Des'
    while resposta.capitalize().replace(' ','') != encerrar:
        fundamental_num = random.randrange(len(fundamentais))
        intervalo = random.randrange(len(fundamentais[fundamental_num]))
        lista_intervalos = []
        for k in fundamentais[fundamental_num]: lista_intervalos.append(k)
        gabarito = lista_intervalos[intervalo]
        print('\nPara voltar, digite "Menu".\n')
        print('Qual é o intervalo de ' + lista_intervalos[intervalo] + ' de ' + fundamentais[fundamental_num]['uníssono'] + '?')
        while True:
            resposta = input('Insira a resposta (escreva "des" para ver gabarito): ')
            if resposta.capitalize().replace(' ','') == encerrar:
                break

            elif resposta.capitalize().replace(' ','') == desisto:
                print('\nA resposta correta é: ', fundamentais[fundamental_num].get(gabarito))
                erros += 1
                tentativas += 1
                print('Acertos: ', acertos)
                print('Erros: ', erros,'\n')
                break
            
            elif resposta.capitalize().replace(' ','') == fundamentais[fundamental_num].get(gabarito):
                print('\nParabéns!')
                acertos += 1
                tentativas += 1
                print('Acertos: ', acertos)
                print('Erros: ', erros,'\n')
                break
            
            else:
                print('Tente novamente!')
                erros += 1
                tentativas += 1
                print('Acertos: ', acertos)
                print('Erros: ', erros,'\n')
                
    if acertos > 0:
        taxa = acertos/tentativas*100

    print('\n')
    print('Seu desempenho em Intervalos:\n')
    print('Tentativas: ', tentativas)
    print('Acertos: ', acertos)
    print('Erros: ', erros)
    print('Taxa de acertos: {:.2f}'.format(taxa), '%\n')

def escalas(fundamentais, escalas):
    acertos = 0
    erros = 0
    tentativas = 0
    taxa = 0.0
    resposta = ''
    escala_resposta = []
    encerrar = 'Menu'
    desisto = 'Des'

    fundamentais_maiores = ['C', 'D', 'D_b', 'E', 'E_b', 'F',
                    'F_sus', 'G', 'G_b', 'A', 'A_b', 'B', 'B_b']

    fundamentais_menores = ['C', 'C_sus', 'D', 'D_sus', 'E', 'E_b', 'F',
                    'F_sus', 'G', 'G_sus', 'A', 'B', 'B_b']

    nomes_escalas = ['Maior', 'menor','menor harmônica', 'menor melódica']
    
    while resposta.capitalize().replace(' ','') != encerrar:
        tons = []
        
        tipo_escala_num = random.randrange(len(escalas))

        tipo_escala = escalas[tipo_escala_num]

        if tipo_escala[0] == 'Maior':
            for tom in fundamentais:
                if tom['uníssono'] in fundamentais_maiores:
                    tons.append(tom)
                    
        elif tipo_escala[0] == 'menor' or 'menor harmônica' or 'menor melódica':
            for tom in fundamentais:
                if tom['uníssono'] in fundamentais_menores:
                    tons.append(tom)

        tom_num = random.randrange(len(tons))

        tom = tons[tom_num]

        escala_gabarito = []

        for grau in range(1, len(tipo_escala)):
            escala_gabarito.append(tom.get(tipo_escala[grau]))

        print('\nPara voltar, digite "Menu".\n')
        if tipo_escala[0] in nomes_escalas:
            print('Digite as notas da escala separadas por vírgula.\n')
            print('Qual é a escala ' + tipo_escala[0] + ' de ' + tom['uníssono'] + '?')
        else:
            print('Digite as notas do modo separadas por vírgula.\n')
            print('Qual é o modo ' + tipo_escala[0] + ' de ' + tom['uníssono'] + '?')

        while True:
            escala_resposta = []
            resposta = input('Insira a resposta (escreva "des" para ver o gabarito): ')
            notas = resposta.split(',')
            for nota in range(len(notas)):
                escala_resposta.append(notas[nota].capitalize().replace(' ',''))

            if resposta.capitalize().replace(' ','') == encerrar:
                break
            
            elif resposta.capitalize().replace(' ','') == desisto:
                print('\nA resposta correta é: ', escala_gabarito)
                erros += 1
                tentativas += 1
                print('Acertos: ', acertos)
                print('Erros: ', erros,'\n')
                break
            
            elif escala_resposta == escala_gabarito:
                print('\nParabéns!')
                acertos += 1
                tentativas += 1
                print('Acertos: ', acertos)
                print('Erros: ', erros,'\n')
                break

            else:
                print('Tente novamente!')
                erros += 1
                tentativas += 1
                print('Acertos: ', acertos)
                print('Erros: ', erros,'\n')
                
    if acertos > 0:
        taxa = acertos/tentativas*100

    print('\n')
    print('Seu desempenho em Escalas/Modos:\n')
    print('Tentativas: ', tentativas)
    print('Acertos: ', acertos)
    print('Erros: ', erros)
    print('Taxa de acertos: {:.2f}'.format(taxa), '%\n')
