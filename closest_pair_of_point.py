from practical import * 
import math 
def dist(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
point = [0]*2
point1 = [0]*2
def bruteForce(P,n):
    mini = math.inf
    for i in range(n):
        for j in range(i+1,n):
            if dist(P[i],P[j])<mini:
                mini = dist(P[i],P[j]) 
                point[0] = P[i]
                point[1] = P[j] 
    return mini

def stripClosest(strip,size,d):
    mini = d
    divide1(strip,0,len(strip)-1)
    for i in range(size):
        for j in range(i+1,size):
            if strip[j][1] - strip[i][1] < mini:
                if dist(strip[i],strip[j])<mini:
                    mini = dist(strip[i],strip[j]) 
                    point1[0] = strip[i]
                    point1[1] = strip[j] 
    return mini 
def closest(P,n):
    if n<=3:
        return bruteForce(P,n)
    mid = n//2
    midPoint = P[mid]
    l = closest(P[:mid],mid) 
    rr = closest(P[mid:],n-mid)
    d = min(l,rr) 
    strip= [] 
    for i in range(n):
        if abs(P[i][0]-midPoint[0])<d:
            strip.append(P[i])  
    return min(d,stripClosest(strip,len(strip),d))

def func(arr,n):
    divide(arr,0,n-1)
    return closest(arr,n)

arr1=[[95,89],[12,83],[58,56],[34,7],[8,47],[51,15],[33,61],[18,1],[11,9],[56,37],[60,26],[52,66],[86,2],[99,30],[22,50],[30,34],[27,65],[5,42],[63,35],
[28,11],[82,67],[7,46],[10,97],[14,12],[90,41],[31,54],[20,38],[42,18],[87,22],[47,39]]
print(func(arr1,len(arr1)-1))
# print(point,point1)