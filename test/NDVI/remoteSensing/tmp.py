k = " "
d = "*"
n = 10
for i in range(n,0,-1):
    for j in range(i):
        print (k * j )+ (k + d) * (i-j)
    break
