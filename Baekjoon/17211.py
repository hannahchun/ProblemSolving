# https://www.acmicpc.net/problem/17211 
# Solution 1
# Python

# number of days and current mood (0:good, 1:bad)
n, s = map(int, input().split())

# gg: the probability that my mood will be good tomorrow when today's mood is good 
# gb: the probability that my mood will be bad tomorrow when today's mood is good
# bg: the probability that my mood will be good tomorrow when today's mood is bad 
# bb: the probability that my mood will be bad tomorrow when today's mood is bad
gg, gb, bg, bb = map(float,input().split())

gCount = [0 for i in range(n)] # to store the probability of having a good mood on each day 
bCount = [0 for i in range(n)] # to store the probability of having a bad mood on each day

if s== 0 : # if my current mood is good, 
    gCount[0] = gg
    bCount[0] = gb
else :
    gCount[0] = bg
    bCount[0] = bb

# On the second day or more...
for i in range(1, n) :
    gCount[i] = gCount[i-1] * gg + bCount[i-1] * bg # (previous day: good & next day: good) or (previous day: bad & next day: good)
    bCount[i] = gCount[i-1] * gb + bCount[i-1] * bb # (previous day: good & next day: bad) or (previous day: bad & next day: bad)

print(round(gCount[n-1] * 1000))
print(round(bCount[n-1] * 1000))