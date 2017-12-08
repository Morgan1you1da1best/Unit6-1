#Morgan Baughman
#12/08/17
#find word in dictionary

dictionary = open('engmix.txt')
word = input('Enter an word:')


counter = 0

def wordAsk():

    for words in dictionary:
        if words.strip() == word:
            print('is in the dictionary')
            counter += 1
            break

    if counter == 0:
        print('is not the dictionary')

print(wordAsk())