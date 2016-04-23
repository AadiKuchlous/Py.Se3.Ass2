digit = 0
letter = 0
i = input("Enter a senence with digits and letters \n")

for x in i:
    if ord(x) >= 97 and ord(x) <= 122 or ord(x) >= 65 and ord(x) <= 90:
        letter = letter + 1
    elif ord(x) >= 48 and ord(x) <= 57:
        digit = digit + 1

print("digits", digit)
print("letters", letter)
