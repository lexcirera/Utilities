def hash_string(string):
    h = 0
    for c in string:
        h = (h * 31 + ord(c)) & 0xffffffff
    return h



def hash256_string(string):
    h = 0
    for c in string:
        h = (h * 31 + ord(c)) & 0xffffffff
    return "{:x}".format(h).zfill(64)


string="j'aime le chocolat et les chacauètes"
sha=hash_string(string)
sha256=hash256_string(string)
print(sha)
print(sha256)