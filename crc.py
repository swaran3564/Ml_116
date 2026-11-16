
data = input("Enter data bits: ")
key = input("Enter generator bits: ")

msg = data + '0' * (len(key)-1)
temp = list(msg)

for i in range(len(data)):
    if temp[i] == '1':
        for j in range(len(key)):
            temp[i+j] = str(int(temp[i+j]) ^ int(key[j]))

crc = ''.join(temp[-(len(key)-1):])
print("CRC:", crc)
print("Transmitted Data:", data + crc)

