#Morgan Baughman
#12/08/17
#find word in dictionary

dictionary = open('engmix.txt')
word = input('Enter an word:')


def wordAsk():
    counter = 0

    for words in dictionary:
        if words.strip() == word:
            print(word, 'is in the dictionary')
            counter += 1
            break

    if counter == 0:
        print(word, 'is not the dictionary')

print(wordAsk())

num = int(input('Enter the numbered word you like to look for'))

dictList = []

for word in dictionary:
    dictList.append(word)
    print(dictList[-1])