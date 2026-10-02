n = int(input())
t = [100, 20, 10, 5]
w = 0
for i in t:
    w += n//i
    n %= i
w += n

print(w)