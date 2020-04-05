import hashlib

"""
 密码加密
"""

def md5(arg):
    hash = hashlib.md5()
    hash.update(bytes(arg,encoding='utf-8'))
    return hash.hexdigest()

