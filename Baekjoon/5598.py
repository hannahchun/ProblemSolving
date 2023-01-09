# https://www.acmicpc.net/problem/5598
# Solution 1
# Python

bf='ABCDEFGHIJKLMNOPQRSTUVWXYZ' # Original alphabet
af='DEFGHIJKLMNOPQRSTUVWXYZABC' # Caesar cipher

# Create a dictionary
# key: Caesar cipher 
# value: Original alphabet
alphalist = list(zip(af, bf))
alphadict = dict(alphalist)

word=input()
newWord=''

for letter in word : # For each letter in the input,
    for key in alphadict.keys() : # For each key in 'alphadict',
        if letter == key : # if the letter is the same as key, 
            newWord+=alphadict[key] # get the value in 'alphadict' using the key
print(newWord)
