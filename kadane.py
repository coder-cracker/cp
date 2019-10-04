def kadane(arr,n):
    temp_sum = 0 
    max_sum = 0 
    start_ind,end_ind=[],[] 
    for i in range(n):
        if temp_sum==0:
            start_ind.append(i)
        temp_sum  = max(0,arr[i]+temp_sum)

        max_sum = max(max_sum,temp_sum)
        if max_sum==temp_sum:
            end_ind.append([i,start_ind[-1],max_sum]) 

    return max_sum,end_ind   

r = [2,3,-1,-2,-3,4,5,7]
print(kadane(r,len(r))) 
