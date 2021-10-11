n = int(input())
p = {}
pp = {}
for i in range(0, n):
    m = input().split()
    p[m[0]] = m[1]
    pp[m[1]] = m[0]
n = int(input())
k = []
for i in range(0, n):
    x = input()
    k.append(x)
for x in k:
    if x in p:
        print(p[x])
    elif x in pp:
        print(pp[x])
    else:
        print('Not found')
