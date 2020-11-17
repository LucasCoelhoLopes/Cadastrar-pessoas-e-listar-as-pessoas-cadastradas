import os
from Tratamento_de_erros import tratar_opcao

import os

def inicio():
    os.system('cls')
    print('Escolha a opcção desejada:')
    print('1 - Cadastar pessoa\n2 - Listar pessoas já cadastradas')
    opcao = input('Opcao: ')

    return_tratar_opcao = tratar_opcao(opcao)

    if return_tratar_opcao == True:
        if opcao == '1':
            from cadastrar import cadastro
            cadastro()
        
        else:
            from listar import lista
            lista()

    else:
        print('Opção inválida.')
        os.system('Pause')
        inicio()