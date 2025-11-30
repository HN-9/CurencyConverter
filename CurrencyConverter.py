import requests

API_URL = "https://api.exchangerate-api.com/v4/latest/{}"

def convert_currency(amount, from_currency, to_currency):
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    try:
        response = requests.get(API_URL.format(from_currency))
        data = response.json()

        if "rates" not in data:
            print("Error: Invalid currency code.")
            return None

        rate = data["rates"].get(to_currency)

        if rate is None:
            print("Error: Target currency not found.")
            return None

        converted_amount = amount * rate
        return converted_amount

    except Exception as e:
        print("Error:", e)
        return None


if __name__ == "__main__":
    print("🌍 Currency Converter (Using Real-Time Exchange Rates)\n")

    amount = float(input("Enter amount: "))
    from_curr = input("From currency (e.g., USD, INR, EUR): ")
    to_curr = input("To currency (e.g., USD, INR, EUR): ")

    result = convert_currency(amount, from_curr, to_curr)

    if result is not None:
        print(f"\n💱 {amount} {from_curr.upper()} = {result:.2f} {to_curr.upper()}")
