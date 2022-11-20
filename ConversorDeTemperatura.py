def ConverorDeTemperatura():
    print("=" * 50)
    print("Conversor de Temperaturas")
    print("=" * 50)

    Temperatura = float(input("Qual temperatura deseja converter: \n1 - Farenheit \n2- Kelvin\n"))

    if Temperatura == 1:
        print("=" * 50)
        Farenheit = float(input("Digite a temperatura em °C: "))
    
        print("{:.1f}°C em Farenheit equivale a {:.1f}°F".format(Farenheit,(Farenheit * 1.8 + 32)))
        print("=" * 50)

    if Temperatura == 2:
        print("=" * 50)
        Kelvin = float(input("Digite a temperatura em °C: "))
        print("{:.1f}°C em Kelvin equivale a {:.1f}°K".format(Kelvin, (Kelvin + 273.15)))
        print("=" * 50)