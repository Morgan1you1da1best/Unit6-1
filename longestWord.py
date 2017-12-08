#Morgan Baughman
#12/6/17
#fileDemo.py - how to read a file

dictionary = open('engmix.txt')

longest = 0
word = ''

for words in dictionary:
    length = len(word)
    if length > longest:
        lenght = longest
        words = word
    
    
print('The longest word is', word)