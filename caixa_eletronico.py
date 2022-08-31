# Bibliotecas
import os
import funcoes

DB_FILE = "caixa_eletronico/banco_de_dados.json"

# Variáveis de dados dos clientes
dados_clientes = funcoes.ler_banco_de_dados(DB_FILE)

# Inicio do programa
while True:
    funcoes.mostrar_menu(["Cliente", "Gerente"])
    opcao = funcoes.validar_opcao(["1", "2"])
    # Se a opção for cliente
    if opcao == "1":
        funcoes.mostrar_menu(["Conta", "Depósito/Saque", "Transações"])
        opcao = funcoes.validar_opcao(["1", "2", "3"])

        # Opções de Conta
        if opcao == "1":
            funcoes.mostrar_menu(["Abrir Conta", "Extrato de Movimentações", "Encerrar Conta"])
            # Verifica se a opção é válida
            opcao = funcoes.validar_opcao(["1", "2", "3"])

            # Opção de ABRIR CONTA
            if opcao == "1":
                dados_clientes = funcoes.abrir_conta(dados_clientes)
                funcoes.escrever_banco_de_dados(dados_clientes, DB_FILE)
            # opção de EXTRATO
            elif opcao == "2":
                funcoes.extrato(dados_clientes)

            # opção de ENCERRAR CONTA
            elif opcao == "3":
                dados_clientes = funcoes.encerrar_conta(dados_clientes)
                funcoes.escrever_banco_de_dados(dados_clientes, DB_FILE)
        # Opções de Depósito/Saque
        elif opcao == "2":
            funcoes.mostrar_menu(["Depósito", "Saque"])
            # Verifica se a opção é válida
            opcao = funcoes.validar_opcao(["1", "2"])
            # Depósito
            if opcao == "1":
                dados_clientes = funcoes.deposito(dados_clientes)
                funcoes.escrever_banco_de_dados(dados_clientes, DB_FILE)
            # Saque
            elif opcao == "2":
                dados_clientes = funcoes.saque(dados_clientes)
                funcoes.escrever_banco_de_dados(dados_clientes, DB_FILE)

        # Opções de Transações
        elif opcao == "3":
            funcoes.mostrar_menu(["Transferência", "Pagamento"])
            # Verifica se a opção é válida
            opcao = funcoes.validar_opcao(["1", "2"])
            # Opção TRANSFERÊNCIA
            if opcao == "1":
                dados_clientes = funcoes.transferencia(dados_clientes)
                funcoes.escrever_banco_de_dados(dados_clientes, DB_FILE)
            # Opção PAGAMENTO
            elif opcao == "2":
                dados_clientes = funcoes.pagamento(dados_clientes)
                funcoes.escrever_banco_de_dados(dados_clientes, DB_FILE)
    # Se a opção for gerente
    elif opcao == "2":
        funcoes.mostrar_menu(["Imprimir Relatório", "Encerrar Programa"])
        opcao = funcoes.validar_opcao(["1", "2"])
        if opcao == "1":
            funcoes.relatorio_gerencia(dados_clientes)
        if opcao == "2":
            print("O programa será encerrado!")
            encerrar = input("Deseja continuar [S/N]? ")
            if encerrar in ["S", "s"]:
                break