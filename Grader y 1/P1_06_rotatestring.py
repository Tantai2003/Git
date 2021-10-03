n = input()
a = int(input())
c = []

x = 0
for i in range(0, a):
    b = input()
    c.append(b)
v = len(c[0])
for i in range(0, len(c)):
    if len(c[i]) != v:
        x = 1
        break
if x == 0:

    if n == '90':
        for i in range(0, len(c[0])):
            p = ''
            for j in range(a-1, -1, -1):
                p += c[j][i]
            print(p)
    elif n == '180':
        for i in range(a-1, -1, -1):
            p = ''
            for j in range(len(c[0])-1, -1, -1):
                p += c[i][j]
            print(p)
    elif n == 'flip':
        for i in range(0, a):
            p = ''
            for j in range(len(c[0])-1, -1, -1):
                p += c[i][j]
            print(p)
else:
    print("Invalid size")
