#  Back end of cypher

import collections
import string


def moduleTest(name):
    print("Hello World!")
    print("Hello " + name + ", how old art thu?")


def encrypt(word, rotationnum):
    if word and rotationnum != "":
        alphLib = collections.deque(string.ascii_lowercase)
        word = word.lower()
        rotationNum = int(rotationnum)
        alphLib.rotate(rotationNum)
        alphLib = ''.join(list(alphLib))
        secret = ''

        for letter in word:
            if letter in string.ascii_lowercase:
                position = string.ascii_lowercase.index(letter)
                newletter = alphLib[position]
                secret = secret + newletter
            else:
                secret = secret + letter
    else:
        secret = "Invalid Input... :("
    return secret
