# A. Young Physicist
# time limit per test2 seconds
# memory limit per test256 megabytes
# A guy named Vasya attends the final grade of a high school. One day Vasya decided to watch a match of his favorite hockey team. And, as the boy loves hockey very much, even more than physics, he forgot to do the homework. Specifically, he forgot to complete his physics tasks. Next day the teacher got very angry at Vasya and decided to teach him a lesson. He gave the lazy student a seemingly easy task: You are given an idle body in space and the forces that affect it. The body can be considered as a material point with coordinates (0; 0; 0). Vasya had only to answer whether it is in equilibrium. "Piece of cake" — thought Vasya, we need only to check if the sum of all vectors is equal to 0. So, Vasya began to solve the problem. But later it turned out that there can be lots and lots of these forces, and Vasya can not cope without your help. Help him. Write a program that determines whether a body is idle or is moving by the given vectors of forces.

# Input
# The first line contains a positive integer n (1 ≤ n ≤ 100), then follow n lines containing three integers each: the xi coordinate, the yi coordinate and the zi coordinate of the force vector, applied to the body ( - 100 ≤ xi, yi, zi ≤ 100).

# Output
# Print the word "YES" if the body is in equilibrium, or the word "NO" if it is not.

# Examples
# InputCopy
# 3
# 4 1 7
# -2 4 -1
# 1 -5 -3
# OutputCopy
# NO
# InputCopy
# 3
# 3 -1 7
# -5 2 -4
# 2 -1 -3
# OutputCopy
# YES

n = int(input())
l = []
l2 = []
for _ in range(n):
    l.append(input().split())

for _ in range(n):
    x = 0
    idx = 0
    for j in l:
        if idx < 3:
            x += int(j[idx])
    idx += 1
    l2.append(x)


print("YES" if sum(l2)==0 else "NO")

# better ver:
n = int(input())

l = []
l2 = []

for _ in range(n):
    l.append(input().split())

for i in range(3):
    x = 0
    for j in l:
        x += int(j[i])
    l2.append(x)

print("YES" if sum(l2) == 0 else "NO")

# how to solve a matrix acc to this question:
# x1 y1 z1
# x2 y2 z2
# x3 y3 z3

# x = x1 + x2 + x3
# y = y1 + y2 + y3
# z = z1 + z2 + z3

# if x == y == z == 0

# its true else False


