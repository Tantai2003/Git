n = input()
n = n.lower()
an = {}
for x in n:
    if 'A' <= x <= 'Z' or 'a' <= x <= 'z':
        if x in an:
            an[x] -= 1
        else:
            an[x] = -1
print(an)
a = []

for x in an:
    a.append([an[x], x])

a.sort()
for x in range(0, len(a)):
    print(a[x][1], '->', -1*a[x][0])
