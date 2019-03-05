n=int(input("N:"))
a=[[0 for i in range(1,n+1)]for j in range(1,n+1)]
y,i,j=0,0,0
while a[i][j]==0:
    y+=1
    a[i][j]=y
    if j<n-1 and a[i][j+1]==0 and (i==0 or a[i-1][j]!=0):
        j+=1
    elif  i<n-1 and a[i+1][j]==0:

        i+=1
    elif  j>0 and a[i][j-1]==0:
        j-=1
    elif  i>0 and a[i-1][j]==0:
        i-=1
    

print(a)
