import requests

fromcurrency = str(input("Please input the currency you wish to convert from: ")).upper()
tocurrency = str(input("Please input the currency you wish to convert to: ")).upper()
amount = float(input("Enter in the amount of money: "))
response = requests.get(f"https://api.frankfurter.app/latest?amount={amount}&from={fromcurrency}&to={tocurrency}")

print(f"{amount} {fromcurrency} is {response.json()['rates'][tocurrency]} {tocurrency}")