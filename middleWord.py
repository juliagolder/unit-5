#julia golder
#4/13/18
#middleWord.py

word = input('Enter some words: ').split(' ')

total = len(word)



if total%2 != 0:
    print(word[total/2])
else:
    print(word[total/2-1])
    print(word[total/2])
