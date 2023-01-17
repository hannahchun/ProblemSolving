# https://www.acmicpc.net/problem/11656
# Solution 1
# Python

word=input()
word_list=[]

for i in range(len(word)) :
    word_list.append(word[i:])

word_list = sorted(word_list)

for i in range(len(word_list)) :
    print(word_list[i])