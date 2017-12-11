#Morgan Baughman
#12/11/17
#warmUp16.py - find all the words in the dictionary taht start with the first initial and last intional of your name in it.

dictionary = open('engmix.txt')

for word in dictionary:
    word = word.strip()
    if len(word) > 0:
        if word[0] == 'm' and word[-1] == 'b':
            print(word)



