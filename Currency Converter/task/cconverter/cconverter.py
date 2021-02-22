def convert_conicoins():
    # Amount of each currency equivalent to 1 conicoin
    exchange_rates = {
        "rub": 2.98,
        "ars": 0.82,
        "hnl": 0.17,
        "aud": 1.9622,
        "mad": 0.208
    }
    coins = float(input())
    if coins.is_integer():
        coins = int(coins)
    for curr_type, rate in exchange_rates.items():
        print(f"I will get {round((coins * rate),2)} {curr_type.upper()} from the sale of {coins} conicoins.")


convert_conicoins()

