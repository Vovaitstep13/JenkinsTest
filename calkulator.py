def wykonanie_zadania(num1, num2, dzialania):
    if dzialania == 'dodawanie':
        return num1 + num2
    elif dzialania == 'odejmowanie':
        return num1 - num2
    elif dzialania == 'mnozenie':
        return num1 * num2
    elif dzialania == 'dzielenie':
        return num1 / num2


num1 = float(input("WPROWADZ PIERWSZA LICZBE:"))
num2 = float(input("Wprowadz drugom liczbe:"))
dzialania = input("Wybierz dzialanie(dodawanie, odejmowanie, mnozenie, dzielenie): ")

wynik = wykonanie_zadania(num1, num2, dzialania  )
print(f"wynik:{wynik}")