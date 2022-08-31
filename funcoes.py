import os
import time
import json
import pandas as pd

def ler_banco_de_dados(nome_do_arquivo):
    with open(nome_do_arquivo) as file:
        d = json.load(file)
    return d

def escrever_banco_de_dados(dados, nome_do_arquivo):
    with open(nome_do_arquivo, "w") as file:
        json.dump(dados, file, indent=4)

def validar_opcao(lista_opcoes):
    while True:
        opcao = input("Digite o número de uma opção: ")
        if opcao in lista_opcoes:
            break
        else:
            print("Digite um número válido!")
    return opcao

def mostrar_menu(lista_opcoes):
    os.system('cls')
    print("#" * 50)
    print("=" * 50)
    print()
    for num_opcao in range(len(lista_opcoes)):
        print(f"\t {num_opcao+1} - {lista_opcoes[num_opcao]}")
    print()
    print("#" * 50)
    print()

def abrir_conta(dados_clientes):
    os.system('cls')
    print("#" * 50)
    print()
    nome = input("Digite seu nome: ").lower()
    if nome in dados_clientes:
        print("Cliente já possui conta!")
        time.sleep(3)
    else:
        senha = input("Digite uma senha:")
        dados_clientes[nome] = {
            "senha": senha,
            "saldo": 0.0,
            "movimentacoes": []
        }
        print("Conta aberta com sucesso!")
    return dados_clientes

def verificar_senha(dados_da_conta):
    for i in range(1, 4, 1):
        senha = input("Digite sua senha: ")
        if senha == dados_da_conta["senha"]:
            return True
        else:
            print("Senha incorreta!")
            print("Você ainda tem", 3 - i, "tentativas")
    return False

def extrato(dados_clientes):
    os.system('cls')
    print("#" * 50)
    print()
    conta = input("Digite seu nome: ").lower()
    if conta in dados_clientes:
        if verificar_senha(dados_clientes[conta]):
            for movimentacao in dados_clientes[conta]["movimentacoes"]:
                if movimentacao < 0:
                    print("Saque", movimentacao)
                else:
                    print("Deposito", movimentacao)
            print(dados_clientes[conta]["saldo"])
            input("Pressione enter para sair.")

def encerrar_conta(dados_clientes):
    '''Função que encerra a conta de um cliente.
    Retorna um novo dicionário de dados.'''

    os.system('cls')
    print("#" * 50)
    print()
    conta = input("Digite seu nome: ").lower()
    if conta in dados_clientes:
        if verificar_senha(dados_clientes[conta]):
            del dados_clientes[conta]
            print("Sua conta foi encerrada com sucesso!")
            print(dados_clientes)
            time.sleep(3)
    return dados_clientes

def deposito(dados_clientes):
    os.system('cls')
    print("#" * 50)
    print()
    favorecido = input("Digite o favorecido: ").lower()
    if favorecido in dados_clientes:
        valor = input("Digite o valor a ser depositado para " + favorecido + ": R$")
        valor = float(valor)
        dados_clientes[favorecido]["saldo"] += valor
        dados_clientes[favorecido]["movimentacoes"].append(valor)
        print("Valor depositado!")
        # only debug
        print(dados_clientes)
        time.sleep(2)
    else:
        print("Favorecido inexistente!")
        time.sleep(3)
    return dados_clientes

def saque(dados_clientes):
    os.system('cls')
    print("#" * 50)
    print()
    conta = input("Digite seu nome: ").lower()
    if conta in dados_clientes:
        if verificar_senha(dados_clientes[conta]):
            print("Seu saldo é:", dados_clientes[conta]["saldo"])
            valor = input("Digite o valor do saque: ")
            valor = float(valor)
            if valor > dados_clientes[conta]["saldo"]:
                print("Seu saldo é insuficiente!")
                time.sleep(3)
            else:
                dados_clientes[conta]["saldo"] -= valor
                dados_clientes[conta]["movimentacoes"].append(valor * (-1))

        print(dados_clientes)
    else:
        print("Cliente não tem conta!")
        time.sleep(3)
    return dados_clientes

def transferencia(dados_clientes):
    os.system('cls')
    print("#" * 50)
    print()
    conta = input("Digite seu nome: ").lower()
    if conta in dados_clientes:
        if verificar_senha(dados_clientes[conta]):
            favorecido = input("Digite o favorecido: ").lower()
            if favorecido not in dados_clientes:
                print("Favorecido não encontrado!")
                time.sleep(3)
                return dados_clientes
            print("Seu saldo é:", dados_clientes[conta]["saldo"])
            valor = input("Digite o valor a ser transferido: ")
            valor = float(valor)
            if valor > dados_clientes[conta]["saldo"]:
                print("Seu saldo é insuficiente!")
                time.sleep(3)
            else:
                dados_clientes[conta]["saldo"] -= valor
                dados_clientes[conta]["movimentacoes"].append(valor * (-1))
                dados_clientes[favorecido]["saldo"] += valor
                dados_clientes[favorecido]["movimentacoes"].append(valor)
                print("Transferência realizada com sucesso!")
                print(dados_clientes)
                time.sleep(3)

    return dados_clientes

def pagamento(dados_clientes):
    os.system('cls')
    print("#" * 50)
    print()
    conta = input("Digite seu nome: ").lower()
    if conta in dados_clientes:
        if verificar_senha(dados_clientes[conta]):
            cod_barra = input("Digite o código de barras: ")
            valor = input("Digite o valor do boleto: ")
            valor = float(valor)
            dados_clientes[conta]["saldo"] -= valor
            dados_clientes[conta]["movimentacoes"].append(f"Pagamento -{valor}")
            print("Esse boleto perdeu!")
            time.sleep(3)
    return dados_clientes

def relatorio_gerencia(dados_clientes):
    os.system('cls')
    print("#" * 50)
    relatorio = pd.DataFrame.from_dict(dados_clientes)
    print(relatorio)
    print()
    input("pressione ENTER para sair")






















