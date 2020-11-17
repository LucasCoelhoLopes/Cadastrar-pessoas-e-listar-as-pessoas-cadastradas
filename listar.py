import os
from inicio import inicio

diretorio_pessoas = 'C:\\Python Projects\\Exercício 4\\Pessoas\\Pessoas.txt'

def lista():
    try:
        with open(diretorio_pessoas) as conteudo:
            print('\nPessoas cadastradas:')
            for line in conteudo:
                print(line, end = "")
            os.system('Pause')
            inicio()
    
    except FileNotFoundError:
        print('Nenhum usuário foi cadastrado!')
        os.system('Pause')
        inicio()
