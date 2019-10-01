import time
li=[]
with open('sorted3.txt','r') as f:
    for line in f.readlines():
        temp = line[:len(line)-1]
        li.append(int(temp))

#li = li[::-1]
def insertion_sort(li):
    n = len(li)
    for i in range(1,n):
        temp = li[i]
        j = i-1
        for j in range(i-1,-1,-1):
            if(temp<li[j]):
                li[j+1] = li[j]
            else:
                j+=1
                break
        li[j] = temp
    return li
li = li[::-1]
start  = time.time()
li = insertion_sort(li)
end = time.time()
#print(li)
print(end-start)

with open('ans.txt','a') as f1:
    f1.write("F2.txt,"+" insertion sort, "+ "sorted_time,"+" time = "+str(end-start)+"\n")
