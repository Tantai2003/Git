alp1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
alp2 = ['N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alp3 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
alp4 = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
inp = []
while True:
    n = input()
    if n == 'end':
        break
    inp.append(n)

for i in range(0, len(inp)):
    ans = ''
    for j in range(0, len(inp[i])):
        if "A" <= inp[i][j] <= "Z":
            for x in range(0, 13):
                if alp1[x] == inp[i][j]:
                    ans += alp2[x]
                elif alp2[x] == inp[i][j]:
                    ans += alp1[x]
        elif "a" <= inp[i][j] <= "z":
            for a in range(0, 13):
                if alp3[a] == inp[i][j]:
                    ans += alp4[a]
                elif alp4[a] == inp[i][j]:
                    ans += alp3[a]
        else:
            ans += inp[i][j]
    print(ans)
