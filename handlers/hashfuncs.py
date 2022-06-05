from handlers.imports import *

ARR1 = ['abcdefghigklmnopqrstuvwxyz']
ARR2 = [char.upper() for char in ARR1]
ARRNUM = ['0123456789']
ARRTOTAL = ARR1 + ARR2 + ARRNUM

with open('handlers/userpwds.txt', 'r') as reg_file:
    reg_dict = ast.literal_eval(reg_file.read())


def hash_encode(st: str, prs: str) -> str:
    """Uses the blake2b hash function method to encode a string.
    Takes two parameters: user id and the string to encode.
    Also performs the hex digestion in order to return a string"""
    encoded_string = hashlib.blake2b(st.encode(), person=prs.encode())
    h_digest = encoded_string.hexdigest()

    return str(h_digest)


def generate_pass(nchars) -> str:
    """Generates a random string of symbols"""
    llist = list()
    for i in range(0, nchars):
        r = random.randint(0, 2)
        choice = random.choice([char for char in ARRTOTAL[r]])
        llist.append(choice)

    random.shuffle(llist)
    generated_pass = ''.join(llist)

    return generated_pass


def create_new_pass(usr: str) -> str:
    """Writes the newly generated password to the register and returns it"""
    newpass = generate_pass(36)
    h_newpass = hash_encode(newpass, usr)
    reg_dict.update({usr: h_newpass})

    with open('handlers/userpwds.txt', 'w') as file:
        file.write(str(reg_dict))

    return newpass

