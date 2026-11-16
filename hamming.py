
data = input("Enter data bits: ")
m = len(data)
r = 0

while 2**r < m+r+1:
    r += 1

a = ['0'] * (m+r)
j = 0

for i in range(1, m+r+1):
    if i & (i-1):
        a[i-1] = data[j]
        j += 1

for i in range(r):
    p = 2**i
    a[p-1] = str(sum(int(a[j-1]) for j in range(1, m+r+1)
                     if j & p) % 2)

print("Hamming Code:", ''.join(a))
