def temp_converter(temp, unit):
    if unit == "C":
        return temp * (9/5) + 32
    if unit == "F":
        return (temp - 32) * (5/9)


while True:
    temp = float(input("\nEnter temperature: "))
    unit = input("Enter unit ('C' for Celsius or 'F' for Fahrenheit):").upper()
    result = temp_converter(temp, unit)
    print("Temperature in", "Fehrenheit: " if unit == "C" else "Celsius", result)
    ans = input("Continue or exit? Yes/No:").lower()
    if ans != "yes":
        break
