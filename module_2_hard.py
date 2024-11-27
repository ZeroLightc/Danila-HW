def password(n):
    result = str()
    for i in range(1,n):
        for j in range(2,n):
            if n % ( i + j ) == 0 and i != j and i<j:
                result = result +str(i)+str(j)
    print(result)
for i in range(3,21):
    print (i,password(i))