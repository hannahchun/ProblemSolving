# https://www.acmicpc.net/problem/1157
# Solution 1
# Python

word=input().upper() # Convert all characters of the input into upper case
num=[] # a list to store the number of occurences of the letter from A~Z in the input (As there are 26 characters in the alphabet, there will be a total of 26 elements in the list)

for i in range(ord('A'), ord('Z')+1) : # ASCII code of 'A' ~ 'Z' = 65 ~ 90 
    num.append(word.count(chr(i))) # Count the number of occurences of the letter from A~Z in the input and store the result in 'num' 

if num.count(max(num)) == 1 : # If there is only one single most commonly used letter in the input, 
    print(chr(num.index(max(num)) + ord('A'))) # the index of that letter in 'num' + ASCII code of 'A' = ASCII code of the most commonly used letter
else :
    print("?")


"""

<chr() and ord()>

chr() function
Ex. # Convert integer 65 to ASCII Character ('A')
    y = chr(65)
    print(type(y), y) // <class 'str'> A
 
    # Print A-Z
    for i in range(65, 65+25+1):
        print(chr(i), end = " , ") // A , B , C , D , E , F , G , H , I , J , K , L , M , N , O , P , Q , R , S , T , U , V , W , X , Y , Z 

ord() function
: It does the reverse of chr().
Ex. # Convert ASCII Unicode Character 'A' to 65
    y = ord('A')
    print(type(y), y) // <class 'int'> 65
 
    # Print 65-90
    alphabet_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in alphabet_list:
        print(ord(i), end = " , ") // 65 , 66 , 67 , 68 , 69 , 70 , 71 , 72 , 73 , 74 , 75 , 76 , 77 , 78 , 79 , 80 , 81 , 82 , 83 , 84 , 85 , 86 , 87 , 88 , 89 , 90 , 


Reference
: https://www.askpython.com/python/built-in-methods/python-chr-and-ord-methods

"""