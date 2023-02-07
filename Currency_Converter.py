def currency_converter():
    print("Currency Convertor\n")
    conversion_rates = {
        'RON': 1.0,
        'EUR': 0.2,
        'GBP': 0.18,
        'USD': 0.22
    }
    # Inputs from users
    amount = float(input("Enter the amount: "))
    from_currency = input(
        "Enter the initial currency (RON, EUR, GBP, USD): ").upper()
    to_currency = input(
        "Enter the target currency (RON, EUR, GBP, USD): ").upper()

    # Converter
    if from_currency != 'RON':
        amount = amount / conversion_rates[from_currency]
    amount = round(amount * conversion_rates[to_currency], 2)
    return amount


result = currency_converter()
print(result)
