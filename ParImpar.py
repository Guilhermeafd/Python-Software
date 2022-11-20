def ParImpar():
    from time import sleep
    print("=" * 50)
    numero = int(input("Digite um número: "))
    print("=" * 50)
    print("PROCESSANDO...")
    print("=" * 50)
    sleep(3)
    if (numero % 2) == 0:
        print("O número informado é PAR!")
        print("=" * 50)
    else:
        print("O número informado é IMPAR!")
        print("=" * 50)