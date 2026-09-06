# B. Minus Two
# time limit per test2 seconds
# memory limit per test256 megabytes
# You are given an array a1,a2,…,an
# . You may perform the following operation:

# For all indices i
#  (1≤i≤n
# ), set ai=|ai−2|
# .
# Find the maximum possible frequency of any integer in a
#  after performing the operation an arbitrary number (possibly zero) of times.

# Input
# The first line of each input contains an integer t
#  (1≤t≤104
# ) — the number of test cases.

# The first line of each test case contains an integer n
#  (1≤n≤2⋅105
# ) — the length of a
# .

# The second line of each test case contains n
#  integers a1,a2,…,an
#  (1≤ai≤109
# ) — the array a
# .

# It is guaranteed that the sum of n
#  over all test cases does not exceed 2⋅105
# .

# Output
# For each test case, output a single integer denoting the maximum possible frequency of any integer in a
#  after performing the operation an arbitrary number of times.

# Example
# InputCopy
# 5
# 2
# 1 3
# 4
# 1 1 1 2
# 3
# 6 7 8
# 4
# 2 2 2 2
# 5
# 1 10 100 1000 100000
# OutputCopy
# 2
# 3
# 1
# 4
# 3
# Note
# In the first test case, we can perform the operation once to have a=[|1−2|,|3−2|]=[1,1]
# , which means the maximum possible frequency of any integer in a
#  is 2
# .

# In the second test case, the maximum frequency of an integer in a
#  is 3
# . It can be shown that, no matter how many operations we perform, the maximum possible frequency of an integer in a
#  will never exceed 3
# .


t = int(input())
o = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    odd = 0
    even0 = 0
    even2 = 0

    for x in a:
        if x % 2:
            odd += 1
        elif x % 4 == 0:
            even0 += 1
        else:
            even2 += 1

    o.append(max(odd, even0, even2))

for i in o:
    print(i)