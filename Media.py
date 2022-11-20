def Media():
    print("=" * 50)
    print("Calculadora de Média")
    print("=" * 50)
    Nota01 = float(input("Digite a primeira nota: "))
    Nota02 = float(input("Digite a segunda nota: "))

    Media = (Nota01 + Nota02) / 2
    
    print("=" * 50)
    print("A média dele (a) foi {}".format(Media))
    print("=" * 50)

    if Media >= 6:
        print("\033[32mPARABÉNS!\033[m Esse aluno foi aprovado!")
        print("=" * 50)
    else:
        print("\033[31mREPROVADO!\033[m Estude mais...")
        print("=" * 50)