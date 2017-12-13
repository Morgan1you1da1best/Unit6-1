#Morgan Baughman
#12/13/17
#quiz6.py 

"""dictionary = open('engmix.txt')

for word in dictionary:
    word = word.strip()
    if 'c' and 'c' and 'c' and 'p' and 'p' in word:
        print(word)
"""





"""dictionary = open('engmix.txt')
def howManyWords():
    wordCount = 0
    for word in dictionary:
        word = word.strip()
        if word == '':
            if word[0] == 'r':
                wordCount += 1
                print(wordCount)
                
howManyWords()"""




"""
dictionary = open('engmix.txt')

num = int(input('Enter the number of letters'))

for word in dictionary:
    word = word.strip()
    if len(word) > 0:
        if len(word) == num:
            print(word)"""
            
            
            
"""            
dictionary = open('engmix.txt')
def program4():
    letter = input("Enter a letter: ")
    notCounter = 0
    for words in dictionary:
        if letter not in words:
            notCounter += 1
            print(notCounter)
program4()"""
            
            