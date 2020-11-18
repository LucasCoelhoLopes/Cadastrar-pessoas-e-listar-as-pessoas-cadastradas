import os
from Tratamento_de_erros import tratar_pessoa
from Tratamento_de_erros import tratar_nome

def cadastro():
    os.system('cls')
    pessoa = input('Informe o nome da pessoa que deseja cadastar: ')

    return_tratar_nome = tratar_nome(pessoa)

    if return_tratar_nome == True:
        return_tratar_pessoa = tratar_pessoa(pessoa)
        
        if return_tratar_pessoa == True:
            from inicio import inicio

            print('Cadastro realizado com sucesso!')
            os.system('Pause')
            inicio()

        else:
            print('Essa pessoa já foi cadastrada!')
            os.system('Pause')
            cadastro()
    
    else:
        print('Nome inválido.')
        os.system('Pause')
        cadastro()
