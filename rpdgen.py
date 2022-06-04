import random

ARR1 = ['abcdefghigklmnopqrstuvwxyz']
ARR2 = [char.upper() for char in ARR1]
ARRNUM = ['0123456789']
ARRSPEC = ["!@#$%^&*()~{}"]
ARRTOTAL = ARR1 + ARR2 + ARRNUM +ARRSPEC


def main(nchars) -> dict:

    dictionary = dict()
    llist = list()

    """Generating the key of a dict"""
    for i in range(0, nchars):
        r = random.randint(0, 3)
        choice = random.choice([char for char in ARRTOTAL[r]])
        llist.append(choice)

    random.shuffle(llist)
    namestringkey = ''.join(llist)

    """Generating value of the dict"""
    for i in range(0, nchars):
        r = random.randint(0, 3)
        choice = random.choice([char for char in ARRTOTAL[r]])
        llist.append(choice)
    random.shuffle(llist)
    namestringval = ''.join(llist)

    dictionary.update({namestringkey: namestringval})

    return dictionary


if __name__ == '__main__':

    dictionaryy = main(60)
    with open('handlers/813gxzp7zc.txt', 'w') as file:
        file.write(str(dictionaryy))

