import requests
import json


def convert_currencies():
    exchange_rates = {}
    from_curr = input().lower()
    to_curr = input().lower()

    r = requests.get(f"http://www.floatrates.com/daily/{from_curr}.json")
    conversions = json.loads(r.text)

    if from_curr != "usd":
        exchange_rates["usd"] = conversions["usd"].get("rate")
    if from_curr != "eur":
        exchange_rates["eur"] = conversions["eur"].get("rate")

    while to_curr:
        from_amt = float(input())
        print("Checking the cache…")

        if to_curr in exchange_rates.keys():
            print("Oh! It is in the cache!")
            print(f"You received {round(from_amt * exchange_rates[to_curr],2)} {to_curr.upper()}.")

        else:
            exchange_rate = conversions[to_curr].get("rate")
            exchange_rates[to_curr] = exchange_rate

            print("Sorry, but it is not in the cache!")
            print(f"You received {round(from_amt * exchange_rate, 2)} {to_curr.upper()}.")

        to_curr = input().lower()


convert_currencies()

