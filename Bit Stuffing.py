
data = input("Enter data bits: ")
result = ""
count = 0

for bit in data:
    result += bit
    if bit == '1':
        count += 1
        if count == 5:
            result += '0'
            count = 0
    else:
        count = 0

print("Stuffed Data:", result)
