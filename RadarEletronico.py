def RadarEletronico():
    print("=" * 50)
    print("RADAR A FRENTE!")
    print("=" * 50)
    Velocidade = int(input("Qual a sua velocidade em KM/H? "))
    if Velocidade >= 80:
        print("=" * 50)
        print("\033[31mMULTADO!\033[m") 
        print("=" * 50)
        print("Você terá que pagar R$ {:.2f} por excesso de velocidade!".format((Velocidade - 80)*7))
    else:
        print("=" * 50)
        print("Tenha um bom dia! Dirija com segurança!")