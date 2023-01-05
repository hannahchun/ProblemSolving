# https://www.acmicpc.net/problem/4659
# Solution 1
# Python

word=''
word_list=[] # a list to store the words
word_valid=[] # a list to store the validity('Yes'/'No') of each word in the word_list

while True :
    isValid=True

    word=input()

    # If the user types 'end', break out of the loop
    if word == 'end' :
        break

    # Add the word in the word list
    word_list.append(word)

    # Check whether the word includes at least one vowel(a,e,i,o,u)
    vowel_cnt=0
    for i in range(len(word)) :
        if word[i] in 'aeiou' :
            vowel_cnt+=1
    if vowel_cnt == 0 :  
        isValid=False

    # Check whether the word includes either three consecutive vowels or consonants
    for i in range(len(word)-2) :
        if word[i] in 'aeiou' and word[i+1] in 'aeiou' and word[i+2] in 'aeiou' : # if there are three consecutive vowels, not valid
            isValid=False
        if (word[i] not in 'aeiou') and (word[i+1] not in 'aeiou') and (word[i+2] not in 'aeiou') : # if there are three consecutive consonants, not valid
            isValid=False

    # Check whether the word includes two consecutive identical letters
    # Only 'ee' or 'oo' is an allowed sequence!
    for i in range(len(word)-1) : 
        if word[i] == word[i+1] :
            if word[i] != 'e' and word[i] != 'o' :
                isValid=False
    
    if isValid == True : # if the word is a valid password,
        word_valid.append('Yes')
    else :
        word_valid.append('No')
    
for i in range(len(word_list)) :
    if word_valid[i]=='Yes' :
        print("<"+word_list[i].strip()+"> is acceptable.")
    else :
        print("<"+word_list[i].strip()+"> is not acceptable.")