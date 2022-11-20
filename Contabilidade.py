def Contabilidade():

    print("=" * 50)
    print("BEM VINDO A NOSSA CONTABILIDADE!")
    print("=" * 50)

    Salario = float(input("Digite o seu salário: R$ "))
    if Salario > 1250:
        NovoSalario = (Salario * 0.10) + Salario
        print("=" * 50)
        print("O seu novo salário com reajuste de 10% é de R$ {:.2f}".format(NovoSalario))
        print("=" * 50)
    else:
        Salario <= 1249
        NovoSalario = (Salario * 0.15) + Salario
        print("=" * 50)
        print("O seu novo salário com reajuste de 15% é R$ {:.2f}".format(NovoSalario))
        print("=" * 50)