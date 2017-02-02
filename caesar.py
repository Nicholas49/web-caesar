def alphabet_position(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for m in range(26):
        if alphabet[m] == letter.lower():
            return m
    return -1

def rotate_character(char, rot):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    c = alphabet_position(char)
    if c == -1:
        return char
    c += rot
    c %= 26
    d = alphabet[c]
    if char.isupper():
        d = d.upper()
    return d

def encrypt(text, rot):
    h = ""
    for g in text:
        h += rotate_character(g, rot)
    return h