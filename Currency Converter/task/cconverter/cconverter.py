def conicoins_to_dollars():
    conicoins = int(input("Please, enter the number of conicoins you have:\n"))
    exchange_rate = float(input("Please, enter the exchange rate:\n"))
    dollars = conicoins * exchange_rate
    print(f"The total amount of dollars: {dollars}")


conicoins_to_dollars()

