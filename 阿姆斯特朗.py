def check(num):
    i=len(str(num))-1
    res=0
    origin=num
    while i!=-1:
        a=num//(10**i)
        num%=(10**i)
        res+=a**3
        i-=1
    if res==origin:
        return True

def xiaoyu(N):
     for i in range(1, N+1):
         if check(i):
             print(i)

print(xiaoyu(10000000))