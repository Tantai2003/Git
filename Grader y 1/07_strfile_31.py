dna0 = input()
orp = input()
ch = 0
dna = ''
for y in dna0:
    x = y.upper()
    if x == 'A' or x == 'T' or x == 'G' or x == 'C':
        ch += 1
        dna += x

if ch != len(dna0):
    print('Invalid DNA')
else:
    if orp == 'R':
        dna1 = ''
        for x in dna:
            if x == 'A':
                dna1 += 'T'
            elif x == 'T':
                dna1 += 'A'
            elif x == 'C':
                dna1 += 'G'
            elif x == 'G':
                dna1 += 'C'
        for x in range(len(dna1)-1, -1, -1):
            print(dna1[x], end='')
    elif orp == 'F':
        a = str(dna.count("A"))
        c = str(dna.count("C"))
        g = str(dna.count('G'))
        t = str(dna.count('T'))

        print("A="+a+",", "T="+t+",", "G="+g+",", "C="+c)
    elif orp == 'D':
        nd = input()
        c = 0
        for x in range(0, len(dna)-1):
            if nd == dna[x]+dna[1+x]:
                c += 1
        print(c)
