divisor = int(input())
number = int(input())

for n in range(number, divisor, - 1):
    if n % divisor == 0:
        break
print(n)

