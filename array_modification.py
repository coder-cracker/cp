for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    state1=[]
    state2=[]
    state3=[]
    pre=[]

    if(k<n):

        for i in range(k):
            a[i]=a[i]^a[n-1-i]
        for i in range(n):
            print(a[i],end=" ")
        print()        
    else:        

        for i in range(n):
            a[i]=a[i]^a[n-1-i]
            state1.append(a[i])

        for i in range(n):
            a[i]=a[i]^a[n-1-i]
            state2.append(a[i])   
        for i in range(n):
            a[i]=a[i]^a[n-1-i]
            state3.append(a[i])
        remain=k%n
        
        l=k//n
        p=l%3 
        if(p==0):
            pre=state3
        elif(p==1):
            pre=state1
        elif(p==2):
            pre=state2
        if(remain==0):
            for i in range(n):
                print(pre[i],end=" ")
            print()    
        else:            
            for i in range(remain):
                pre[i]=pre[i]^pre[n-1-i]
            for i in range(n):
                print(pre[i],end=" ")
            print()       
