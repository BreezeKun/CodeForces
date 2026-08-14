# A. Nearly Lucky Number
# time limit per test2 seconds
# memory limit per test256 megabytes
# Petya loves lucky numbers. We all know that lucky numbers are the positive integers whose decimal representations contain only the lucky digits 4 and 7. For example, numbers 47, 744, 4 are lucky and 5, 17, 467 are not.

# Unfortunately, not all numbers are lucky. Petya calls a number nearly lucky if the number of lucky digits in it is a lucky number. He wonders whether number n is a nearly lucky number.

# Input
# The only line contains an integer n (1 ≤ n ≤ 1018).

# Please do not use the %lld specificator to read or write 64-bit numbers in С++. It is preferred to use the cin, cout streams or the %I64d specificator.

# Output
# Print on the single line "YES" if n is a nearly lucky number. Otherwise, print "NO" (without the quotes).

# Examples
# InputCopy
# 40047
# OutputCopy
# NO
# InputCopy
# 7747774
# OutputCopy
# YES
# InputCopy
# 1000000000000000000
# OutputCopy
# NO

n = input()
lucky = ["7", "4"]
x = 0
for i in n:
    if i in lucky:
        x += 1
print("YES" if str(x) in lucky else "NO")