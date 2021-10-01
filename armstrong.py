
def armstrong (num):
    count = 0
    sum = 0
    temp = num
    qw = num
    while temp>0:
        count +=1
        temp=int(temp/10)
        #print(temp)
    while qw>0 :
        remain = qw % 10
        sum = sum + (remain**count)
        qw = int(qw/10)    
    #print(sum)    
    if num == sum : 
        print(str(num) + " is an armstrong number .\n")
    else :
        print(str(num) + " is not an armstrong number .\n")


a=int(input("enter a number =  "))
armstrong(a)                

