
def reverse(d):
    # d เป็น dict ที่มี value ไม่ซ ้ำกนั
    # คืน dict ใหม่ที่เก็บ key,value ที่ค่ำเป็น value,key ของ d ที่ได ้รับ
    if len(d) != 0:
        for k in d:
            a = d[k]
            d[k] = k

    return d


def keys(d, v):
    # คืนลิสต์ที่เก็บค่ำของ keys ใน d (เรียงยังไงก็ได ้) ที่มีค่ำ value เท่ำกับ v
    key = []
    for k in d:
        key.append(k)
    return


exec(input().strip())
"""
dic = {'A': 1, 'B': 2}
print(dic)
dic['P'] = dic.pop('A')
print(dic)
"""
