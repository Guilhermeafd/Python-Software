def ConversorDeMoedas():
    print("=" *  50)
    print("Conversor de Moedas")
    print("=" *  50)
    Moeda = int(input("Qual moeda você deseja converter? \n1- Euro \n2 - Dolar \n3 - Libra Esterlina\n"))

    if Moeda == 1:
        Euro = float(input("Qual valor você tem em R$? "))
        print("=" * 50)
        print("\nNa cotação de hoje R$ {:.2f} equivale a € {:.2f}".format(Euro, (Euro / 5.57)))
        print("=" * 50)

    if Moeda == 2:
        Dolar = float(input("Qual o valor você tem em R$? "))
        print("=" * 50)
        print("\nNa cotação de hoje R$ {:.2f} equivale a US$ {:.2f}".format(Dolar, (Dolar / 5.38)))
        print("=" * 50)

    if Moeda == 3:
        LibraEsterlina = float(input("Qual o valor você tem em R$? "))
        print("=" * 50)
        print("\nNa cotação de hoje R$ {:.2f} equivale a £ {:.2f}".format(LibraEsterlina, (LibraEsterlina / 6.40)))
        print("=" * 50)
