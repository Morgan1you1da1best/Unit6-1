#Morgan Baughman
#12/6/17
#fileDemo.py - how to read a file

dictionary = open('engmix.txt')

word2 = 1
word1 = ""

for word in dictionary:
    length = len(word1)
    if length > len(word2):
        word2 = word1
    print(word1)
    
    wordCount += 1
    
print('There are', wordCount, 'words in the dictionary.')
