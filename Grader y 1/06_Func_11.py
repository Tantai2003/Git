n = input().split()
a = int(n[0], 2)
b = int(n[1], 2)
a = a+b
a = bin(a).split('0b')
print(a[1])
