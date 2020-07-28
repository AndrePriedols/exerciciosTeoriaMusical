#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys

import random
import notas
import exercicios
import escalas

fundamentais = notas.fundamentais

escalas = escalas.escalas



def main():

    while True:
        opcao = 0
        print('Escolha a opção: ')
        opcao = int(input('1 - intervalos; 2 - escalas e modos; 3 - encerrar: '))
        if opcao == 1: exercicios.intervalos(fundamentais)
        elif opcao == 2: exercicios.escalas(fundamentais, escalas)
        elif opcao == 3: break
        else: opcao = int(input('1 - intervalos; 2 - escalas e modos; 3 - encerrar: '))
            
    print('\nAté logo!')

main()
