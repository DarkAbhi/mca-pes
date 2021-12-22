a = input("Enter a binary number = ")
decimal = 0
for digit in a:
    decimal = decimal*2 + int(digit)
print(decimal)
