import hashlib


def md5(s):
    hash_md5 = hashlib.md5(s)
    return hash_md5.hexdigest()
