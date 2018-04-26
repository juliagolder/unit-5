#julia golder
#4/26/18
#vowelWordDemo.py - how to treat strings like lists

word = input('Enter some words: ').split(' ')

for w in word:
    if w[0] in 'AEIOUaeiou': #starts with vowel'
        print(w)
    