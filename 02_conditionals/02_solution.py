age = int(input("Provide me a age"))

day = "Wednesday"

price = 12 if age>=18 else 8
if day == "Wednesday":
    # price = price-2
    price -=2
print("Ticket pricr for you is $", price)