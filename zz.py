#Morgan Baughman
#12/11/17
#zz.py - Find a word in the dictionary that contains zz. 

dictionary = open('engmix.txt')

for word in dictionary:
    word = word.strip()
    if 'zz' in word:
        print(word)
