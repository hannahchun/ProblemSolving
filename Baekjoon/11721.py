# https://www.acmicpc.net/problem/11721
# Solution 1
# Python

word=input()
for i in range(0, len(word), 10) :
    print(word[i:i+10])

# Break down the word into parts so that each part has a length of 10 with an allowance of a smaller length than 10 in the last part. 
# Print the divided words