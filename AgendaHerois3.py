import csv

# Crie a tabela hash com 26 slots, um para cada letra do alfabeto
tabela_hash = [[] for _ in range(26)]

# Função para formatar texto com cores
def colorize(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

# Define o menu com cores
menu = f"""
    1 - {colorize("Adicionar super herói", "32")}
    2 - {colorize("Buscar super herói", "34")}
    3 - {colorize("Mostrar todos os super heróis por letra", "33")}
    4 - {colorize("Remover super herói", "31")}
    5 - {colorize("Sair", "36")}
"""

print(menu)

# Função para calcular o índice da tabela hash com base na letra inicial do nome
def calcular_indice(letra):
    if 'A' <= letra <= 'Z':
        return ord(letra) - ord('A')
    elif 'a' <= letra <= 'z':
        return ord(letra) - ord('a')
    else:
        raise ValueError("A letra deve estar entre A-Z ou a-z.")

def abrir_arquivo():
    try:
        with open('agenda.csv', 'r') as arquivo:
            return arquivo.readlines()
    except FileNotFoundError:
        print('Arquivo não encontrado')
        return []

def salvar_arquivo(heroi):
    with open('agenda.csv', 'a') as arquivo:
        arquivo.write(heroi)

def adicionar_heroi():
    nome = input('Digite o nome do super herói: ').upper()
    poder = input('Digite o poder do super herói: ')
    editora = input('Digite a editora do super herói: ')
    heroi = f'{nome};{poder};{editora}\n'
    salvar_arquivo(heroi)
    
    # Adicionar o herói à tabela hash
    letra_inicial = nome[0]
    indice = calcular_indice(letra_inicial)
    tabela_hash[indice].append((nome, poder, editora))

def buscar_heroi():
    nome = input('Digite o nome do super herói: ')
    arquivo = abrir_arquivo()
    for linha in arquivo:
        if nome in linha:
            print(linha)
    
    # Buscar na tabela hash
    letra_inicial = nome[0]
    indice = calcular_indice(letra_inicial)
    for heroi in tabela_hash[indice]:
        if heroi[0] == nome:
            print(f"Nome: {heroi[0]}, Poder: {heroi[1]}, Editora: {heroi[2]}")

def mostrar_herois():
    letra = input('Digite a letra inicial: ').upper()
    arquivo = abrir_arquivo()
    for linha in arquivo:
        if linha.startswith(letra):
            print(linha)
    
    # Mostrar na tabela hash
    indice = calcular_indice(letra)
    for heroi in tabela_hash[indice]:
        print(f"Nome: {heroi[0]}, Poder: {heroi[1]}, Editora: {heroi[2]}")

def remover_heroi():
    nome = input('Digite o nome do super herói: ')
    arquivo = abrir_arquivo()
    linhas_atualizadas = []
    for linha in arquivo:
        if nome not in linha:
            linhas_atualizadas.append(linha)
    with open('agenda.csv', 'w') as arquivo:
        arquivo.writelines(linhas_atualizadas)
    
    # Remover da tabela hash
    letra_inicial = nome[0]
    indice = calcular_indice(letra_inicial)
    tabela_hash[indice] = [(n, p, e) for n, p, e in tabela_hash[indice] if n != nome]

def sair():
    exit()

def opcoes_menu(opcao):
    if opcao == '1':
        adicionar_heroi()
    elif opcao == '2':
        buscar_heroi()
    elif opcao == '3':
        mostrar_herois()
    elif opcao == '4':
        remover_heroi()
    elif opcao == '5':
        sair()
    else:
        print('Opção inválida')

while True:
    opcao = input('Digite uma opção: ')
    opcoes_menu(opcao)
    print(menu)
