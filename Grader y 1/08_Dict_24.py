def text2keys(text):
    tk = {'a': '2', 'b': '22', 'c': '222', 'd': '3', 'e': '33', 'f': '333', 'g': '4', 'h': '44', 'i': '444', 'j': '5', 'k': '55', 'l': '555', 'm': '6', 'n': '66',
          'o': '666', 'p': '7', 'q': '77', 'r': '777', 's': '7777', 't': '8', 'u': '88', 'v': '888', 'w': '9', 'x': '99', 'y': '999', 'z': '9999', ' ': '0'}
    text = text.lower()
    b = ''
    print(text)
    for i in range(0, len(text)):
        if 'a' <= text[i] <= 'z' or text[i] == " ":
            b += tk[text[i]] + ' '
    return b.strip()


def keys2text(keys):
    tk = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': [
        'm', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z'], '0': [' ']}
    keys = keys.split()
    b = ''
    for i in range(0, len(keys)):
        te = tk[keys[i][0]]
        b += te[len(keys[i])-1]
    return b.strip()


exec(input().strip())
