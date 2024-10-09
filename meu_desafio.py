menu = """

Bem vindo ao BRA - Banco Regional Anônimo
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Por gentileza informe o valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Seu depósito foi de: R$ {valor:.2f}\n"

        else:
            print("Temos um problema! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Qual valor deseja sacar: "))

        saldo_insuficiente = valor > saldo

        limite_excedido = valor > limite

        saques_excedidos = numero_saques >= LIMITE_SAQUES

        if saldo_insuficiente:
            print("Temos um problema! Você não tem saldo suficiente.")

        elif limite_excedido:
            print("Temos um problema! O valor do saque excede o limite.")

        elif saques_excedidos:
            print("Temos um problema! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Temos um problema! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("\n================== BRA ==================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo disponível: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        print("Obrigado por ser nosso cliente. BRA agradece!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")