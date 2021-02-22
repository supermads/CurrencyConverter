import requests
import json


def convert_currencies():
    curr_choice = input().lower()
    r = requests.get(f"http://www.floatrates.com/daily/{curr_choice}.json")
    conversions = json.loads(r.text)
    print(conversions["usd"])
    print(conversions["eur"])


convert_currencies()

