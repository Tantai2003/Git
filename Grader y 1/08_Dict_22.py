n = int(input())
li = {}
c = 0
for i in range(0, n):
    m = input().split()
    li[m[0]] = float(m[1])

n = int(input())
si = {}
for i in range(0, n):
    m = input().split()
    if m[0] in li:
        if m[0] in si:
            si[m[0]] += float(m[1])
        else:
            si[m[0]] = float(m[1])
if len(si) == 0:
    print("No ice cream sales")
else:
    total = 0
    topp = []
    topi = []
    for x in si:
        total += si[x]*li[x]
        topi.append([si[x]*li[x], x])
        topp.append(si[x]*li[x])
    print("Total ice cream sales:", total)
    t = []
    for i in range(0, len(topi)):
        if max(topp) == topi[i][0]:
            t.append(topi[i][1])

    t.sort()
    b = ''
    for x in range(0, len(t)):
        if x == len(t)-1:
            b += ' ' + t[x]
        else:
            b += ' ' + t[x]+','
    print('Top sales:'+b)
"""
    if m[0] in li:
        m[0] = int(m[1])
        c += 1
    print(m)
print(li)
"""
