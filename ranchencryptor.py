#base 7
import random

def encryptor(val):
    index = alphabet.index(val)
    ran = random.randrange(-50, 51)
    return str(ran) + ', ' + alphabet[(index + ran + len(alphabet) * 10) % len(alphabet)]

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','-']

password = 'caesar-is-the-best-salad-no-doubt'
encrypt = ''

for letter in password:
    encrypt += '(' + encryptor(letter) + '), '
    
print(encrypt)