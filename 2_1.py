z = 58375
print("Maximum number in a given number ", z, end = " ")
max_digit = 0
while z%10 > 1:
    digit = z%10
    z //= 10
    if digit > max_digit:
        max_digit = digit
print(" - ", max_digit)
