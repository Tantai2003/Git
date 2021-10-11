
n = int(input())
name = {}
tel = {}
for i in range(0, n):
    k = input().split()
    name[k[0]+' '+k[1]] = k[2]
    tel[k[2]] = k[0] + ' ' + k[1]

n = int(input())
kk = []
ans = []
for i in range(0, n):
    k = input()
    kk.append(k)
    if k in name:
        ans.append(name[k])
    elif k in tel:
        ans.append(tel[k])
    else:
        ans.append('Not found')
for i in range(0, len(kk)):
    print(kk[i], '-->', ans[i])
