def total(pocket):
    tt = 0
    for x in pocket:
        tt += pocket[x] * x
    return tt


def take(pocket, money_in):
    for x in money_in:
        if x in pocket:
            pocket[x] = pocket[x] + money_in[x]
        else:
            pocket[x] = money_in[x]
    return pocket


"""
def pay(pocket, amt):
    temppocket = dict(pocket)       # copy old pocket
    paid = dict()                   # keep track of paid coin
    for i in sorted(list(pocket.keys()), reverse=True):  # sort pocket by large coin -> small coin
        if amt - i < 0:             # start new loop for smaller coin
            continue
        elif amt == 0:              # end break
            break
        for j in range(0, pocket[i]):
            if amt - i < 0:         # skip to new loop for smaller coin
                break
            amt -= i                # paid by 1 coin at a time
            paid[i] = j + 1         # keep track of paid coin
        pocket[i] = pocket[i] - paid[i]   # leftover in pocket
    if amt > 0:
        ret = dict()
        pocket.update(temppocket)   # use backed up old pocket
        return ret                  # return empty dict
    else:
        return paid
"""


def pay(pocket, amt):
    ppay = dict(pocket)
    wa = {}
    if total(pocket) < amt:
        return {}
    else:
        for x in ppay:
            if amt/x >= 1:
                wa[x] = amt//x
                amt = amt % x
        for x in wa:
            ppay[x] -= wa[x]
        for x in ppay:
            if ppay[x] < 0:
                return {}
        print(ppay)
        for x in ppay:
            pocket[x] = ppay[x]
        return wa


exec(input().strip())
