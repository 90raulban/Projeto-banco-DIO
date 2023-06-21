menu = """

Selecione a opção desejada:

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
saldo_atual = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
ordem = [f"saldo inicial: R$ {saldo:.2f}"]

while True:

    opcao = input(menu)

    if opcao == "1":
        entrada = float(input("Valor a depositar:"))
        if entrada < 0:
            print("\n Não é possível realizar uma operação negativa")
        else:
            saldo_atual  = saldo + saldo_atual + entrada
            ordem.append(f"Depósito: R$ {entrada:.2f}")
            print("\n Deposito realizado com sucesso!")

    elif opcao == "2":
        if numero_saques < LIMITE_SAQUES:
            saque = float(input("Informe a quantidade desejada:"))
            if saque < 0:
                print("\n Não é possível realizar uma operação negativa")
            elif saque <= limite and saque <= saldo_atual:
                saldo_atual = saldo_atual + saldo - saque
                numero_saques = numero_saques + 1
                ordem.append(f"Saque: R$ {saque:.2f}")
                print("\n saque efetuado com sucesso")
            elif saque > limite:
                print ("\n Valor a cima do limite por operação")
            elif saque > saldo_atual:
                print ("\n Saldo insuficiente")
        elif numero_saques >= LIMITE_SAQUES:
            print("\n Limites de saques diários atingidos, por favor retorne outro dia")

    elif opcao == "3":
        print("====================== Extrato ======================")
        ordem.append(f"Saldo Atual: R$ {saldo_atual:.2f}")
        for ord in ordem:
            print(ord)
        print("=====================================================")

    elif opcao == "0":
        break

    else:
        print("opção invalida, favor selecionar as opções abaixo:")
