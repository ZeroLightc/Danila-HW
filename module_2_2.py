a= int(input())
b = int(input())
c = int(input())


if a == b:
    if b == c:
        d = 3
    else:
        d = 2
elif b == c:
    d = 2
elif a == c:
    d = 2
else:
    d = 0

print(d)