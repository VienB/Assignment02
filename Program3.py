money = int(input("How much money do you have? "))
ApplePrice = int(input("Enter the price of the apple: "))

result = money // ApplePrice
TotalAmount = money % ApplePrice

print(f"You can buy {result} apples and your change is {TotalAmount} pesos.")