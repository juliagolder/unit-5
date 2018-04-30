#julia golder
#4/23/18
#longestWord.py

word = input('Enter some words: ').split(' ')

longest = 0
LONGword = ''


for item in word:
    if longest < (len(item)):
        longest = (len(item))
        LONGword = item

print(LONGword)
