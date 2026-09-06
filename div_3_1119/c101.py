# 

t = int(input())
o = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    c = ""

    for i in a:
        if i == -1:
            c += "0"
        else:
            c += str(i)

    parts = c.split("1")

    best = 0
    left = -1
    right = -1

    pos = [i for i in range(n) if c[i] == "1"]

    if len(pos) >= 2:
        for i in range(len(pos) - 1):
            l = pos[i]
            r = pos[i + 1]

            if r - l + 1 > best:
                best = r - l + 1
                left = l
                right = r

        p = pos[0]
        l = -1

        for i in range(p - 1, -1, -1):
            if a[i] == -1:
                l = i

        if l != -1 and p - l + 1 > best:
            best = p - l + 1
            left = l
            right = p

        p = pos[-1]
        r = -1

        for i in range(p + 1, n):
            if a[i] == -1:
                r = i

        if r != -1 and r - p + 1 > best:
            best = r - p + 1
            left = p
            right = r

    elif len(pos) == 1:
        p = pos[0]

        l = -1
        for i in range(p - 1, -1, -1):
            if a[i] == -1:
                l = i

        if l != -1 and p - l + 1 > best:
            best = p - l + 1
            left = l
            right = p

        r = -1
        for i in range(p + 1, n):
            if a[i] == -1:
                r = i

        if r != -1 and r - p + 1 > best:
            best = r - p + 1
            left = p
            right = r

        if left == -1:
            left = p
            right = p

    else:
        neg = []

        for i in range(n):
            if a[i] == -1:
                neg.append(i)

        if len(neg) >= 2:
            left = neg[0]
            right = neg[-1]
        elif len(neg) == 1:
            left = neg[0]
            right = neg[0]

    if left != -1:
        for i in range(left, right + 1):
            if i == left or i == right:
                a[i] = 1
            else:
                a[i] = 0

    for i in range(n):
        if a[i] == -1:
            a[i] = 0

    o.append(a)

for a in o:
    print(*a)