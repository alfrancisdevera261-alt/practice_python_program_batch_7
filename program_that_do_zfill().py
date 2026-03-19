number = input("Enter a number")
digit = int(input("How many digits of number: "))

total_digits = digit - len(number)

if total_digits > 0:
    number_modified = "0" * total_digits + number
else:
    number_modified = number
print(number_modified)