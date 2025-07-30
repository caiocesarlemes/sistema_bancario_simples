# Sistema Bancário Simples

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

menu = """
======= MENU =======

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

====================
=> """

while True:
    opcao = input(menu).lower()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com suceso!")
        else:
            print("Valor inválido. O depósito precisa ser maior que zero.")

    elif opcao == "q":
        print("Encerrando o sistema. Até logo!")
        break

    elif opcao == "e":
        print("\n======= EXTRATO =======")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("=======================\n")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("O valor do saque excedeo limite por operação.")

        elif excedeu_saques:
            print("Número m´ximo de saques excedido.")

        elif valor > 0:
            saldo-= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")

        else:
            print("Valor inválido. O saque precisa ser maior que zero.")
            