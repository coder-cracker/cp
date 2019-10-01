def zeroPadding(arr,zeroPad):
    for i in range(zeroPad):
        arr = '0'+arr
    return arr


def zeroPad1(arr,zeroPad):
    for i in range(zeroPad):
        arr+='0'
    return arr

def add(a,b):
    carry = 0
    if(len(a)>len(b)):
        b = zeroPadding(b,len(a)-len(b))
    else:
        a = zeroPadding(a,len(b)-len(a))
    sum1 =['0']*(len(a)+1)
    # print(sum1)
    for i in range(len(a)-1,-1,-1):
        mul = str(int(a[i])+int(b[i])+int(carry))
        if len(mul)>1:
            sum1[i+1] = mul[1]
            carry =int(mul[0])
        else:
            sum1[i+1] = mul[0]
            carry = 0
    if(carry>0):
        sum1[0] = str(carry)
    return str(int(''.join(sum1)))

def sub(a,b):
    if(len(a)>len(b)):
        b = zeroPadding(b,len(a)-len(b))
    else:
        a = zeroPadding(a,len(b)-len(a))
    temp = ''
    for i in b:
        temp+=str(9-int(i))
    temp1 = add(temp,'1')
    string = add(temp1,a)
    return string[1:]    


def karatsuba(x,y):
    if(len(x)==1 and len(y)==1):
        # print(f'x = {x} y = {y}')
        return str(int(x)*int(y))
    elif len(x)>len(y):
        y = zeroPadding(y,len(y)-len(x))
    elif len(x)<len(y):
        x = zeroPadding(x,len(y)-len(x))
    
    j = len(x)//2 # floor division

    # if len(x) is odd then ++j
    if len(x)%2!=0:
        j+=1 
    
    aZeroPad = len(x)-j
    bZeroPad = 2*aZeroPad

    a = x[:j]
    b = x[j:]
    c = y[:j]
    d = y[j:]
    # print(f'a={a},b={b},c={c},d={d}')
    first_part = karatsuba(a,c)
    second_part = karatsuba(b,d)
    # print(f'a+b={add(a,b)} c+d={add(c,d)}')
    temp_part = karatsuba(add(a,b),add(c,d))
    x = add(first_part,second_part)
    # print(type(temp_part),type(x))
    # print(f'sum= {sub(temp_part,x)}')
    third_part = sub(temp_part,(add(first_part,second_part)))
    # print(first_part,second_part,third_part,temp_part)
    first_part = zeroPad1(first_part,aZeroPad)
    third_part = zeroPad1(third_part,bZeroPad)
    
    return add(first_part,add(second_part,third_part))



import time
a  = '91372500513292095738230726216073236119250659105365038431646586678624302231043626009743762390473684358557741680979274057218663306504114228795391557340347023589289341900277811194973758501148406376218675700891776902217398381845643069125879338575936333345290327619235433306926799834196707125823286128011280455205417793619777248285242738813246124157776739644523523305653757182349250121931599331690359327457264331594049445485583768096141216722237292002021169289300731448943042275144353241039870539829408873'
b = '83151718945881250065896839571039083576934301438296750825203270414630062922577411639048889343933984983475443164207571068724496741632978786465589054596270963267509065163799835475712261914594117124296634416902280527180980083462503669341163272691781501844521015858787883877160700741363909908403790996720576653575218590910175874766788993760165761308837320884138984942275902135298812763384184658939741412619401263574658485602326475783169938729818116115114130806340407816563030156207480047849420029335323372'
start = time.process_time_ns()
temp = karatsuba(a,b)
end = time.process_time_ns()
print(end-start)
# print("The multiplication via algorithm = "+str(karatsuba(a,b)))
# a  = 1675372438
# b  = 2824371162
# print("Manually multiplication of 2 numbers is "+str(a*b))
