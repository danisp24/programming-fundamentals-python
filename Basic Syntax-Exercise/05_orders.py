n = int(input())
total_price = 0
curr_price = 0
for orders in range(n):
    price = float(input())
    days = int(input())
    capsules = int(input())
    if price < 0.01 or price > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsules < 1 or capsules > 2000:
        continue
    total_price += capsules * days * price
    curr_price = capsules * days * price
    print(f"The price for the coffee is: ${curr_price:.2f}")
print(f'Total: ${total_price:.2f}')
