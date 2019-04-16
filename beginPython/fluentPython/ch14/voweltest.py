import itertools


def vowel(c):
    return c.lower() in 'aeiou'

print(list(itertools.dropwhile(vowel,'Aardvark')))

print(list(itertools.dropwhile(vowel,'Aaiouiourdvaraaiouk')))