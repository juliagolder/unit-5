#julia golder
#4/23/18
#longestWord.py

word = input('Enter some words: ').split(' ') #splits words into list

longest = 0 
LONGword = '' #label the variable


for item in word: #loop to find the longest word
    if longest < (len(item)):
        longest = (len(item))
        LONGword = item

print(LONGword) #prints longest word
