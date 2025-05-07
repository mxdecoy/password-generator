# This code is licensed under the MIT License.
# Copyright (c) 2025 mxz

import random
# insert the length of the password and it creates it for you!

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ!"§$%&/()=?0987654321abcdefghijklmnopqrstuvwxyz:-_#+'
def create_pw(digit):
    '''(int) -> str
    Return a new password with the length of digit
    
    >>> print(create_pw(15))
    >>> print(create_pw(0))  
        should return "size matters" 😄
    '''
    if digit < 1:
        return 'size matters'
    elif digit > 256:
        return 'size matters'
        
    pw = ''.join(random.choices(chars, k = digit))
    return pw
# for console:
digit = int(input('How long should your password be? '))
print(create_pw(digit))
