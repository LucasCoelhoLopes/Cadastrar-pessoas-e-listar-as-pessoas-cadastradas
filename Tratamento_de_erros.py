
def tratar_opcao(opcao):
    opcoes_disponiveis = ('1', '2')

    if opcao in opcoes_disponiveis:
        return True

    else:
        return False

def tratar_nome(nome):
    nome_separado = nome.split(' ')

    for nome in nome_separado:
        if nome.isalpha() == True:
            pass

        else:
            return False

    return True

def tratar_pessoa(pessoa):
    diretorio_pessoas = 'C:\\Python Projects\\Exercício 4\\Pessoas\\Pessoas.txt'
    lista_pessoas = []

    try:
        with open(diretorio_pessoas) as conteudo:
            for line in conteudo:
                lista_pessoas.append(line)
    
    except FileNotFoundError:
        arquivo = open(diretorio_pessoas, 'w')
        arquivo.write(pessoa)
        arquivo.close()
        return True

    if pessoa in lista_pessoas:
        return False

    else:
        arquivo = open(diretorio_pessoas, 'a')
        arquivo.write(f'{pessoa}\n')
        arquivo.close()
        return True
