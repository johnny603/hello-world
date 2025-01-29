def fizzbuzz(n):
    output = ""
    if n % 3 == 0:
        output += "fizz"
    if n % 5 == 0:
        output += "buzz"
    print(n) if not output else print(output)

for i in range(1, 101):
    fizzbuzz(i)
