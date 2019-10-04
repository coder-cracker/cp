def mergeSkyline(skylineList_lower,skylineList_higher):
    h1 = h2 = 0
    skyline_merged = []
    while(True):
        if len(skylineList_lower)==0 or len(skylineList_higher)==0:
            break 
        stripe1 = skylineList_lower[0]
        stripe2 = skylineList_higher[0] 
        merged_stripe = [0]*2 
        if stripe2[0]>stripe1[0]:
            merged_stripe[0] = stripe1[0] 
            merged_stripe[1] = stripe1[1] 
            h1 = stripe1[1] 
            if h2>stripe1[1]:
                merged_stripe[1] = h2 
            skylineList_lower.pop(0) 
        elif stripe2[0]<stripe1[0]:
            merged_stripe[0] = stripe2[0] 
            merged_stripe[1] = stripe2[1] 
            h2 = stripe2[1] 
            if h1>stripe2[1]:
                merged_stripe[1] = h1   
            skylineList_higher.pop(0) 
        else:
            merged_stripe[0] = stripe2[0] 
            merged_stripe[1] = max(stripe2[1],stripe1[1]) 
            h2 = stripe2[1] 
            h1 = stripe1[1] 
            skylineList_higher.pop(0)
            skylineList_lower.pop(0) 

        skyline_merged.append(merged_stripe) 

        while(len(skylineList_lower)!=0):
            skyline_merged.append(skylineList_lower.pop(0))
        while(len(skylineList_higher)!=0):
            skyline_merged.append(skylineList_higher.pop(0))
        return skyline_merged 
def getSkyline(low,high,buildings):
    skylineList = [] 
    if low>high:
        return skylineList 
    elif low==high:
        x1 = buildings[low][0] 
        x2 = buildings[low][1] 
        h =  buildings[low][2] 

        element1 = [x1,h] 
        element2 = [x2,0] 

        skylineList.append(element1) 
        skylineList.append(element2)
        
        
        return skylineList 
    else:
        mid = (low+high)//2 
        skylineList_lower = getSkyline(low,mid,buildings)
        skylineList_higher = getSkyline(mid+1,high,buildings) 

        return mergeSkyline(skylineList_lower,skylineList_higher) 

def reductant(skyline_merged):
    current = 0 
    while(current<len(skyline_merged)):
        dupeFound = True 
        i = current+1 
        while((i<len(skyline_merged)) and dupeFound):
            if skyline_merged[current][1] == skyline_merged[i][1]:
                dupeFound = True 
                skyline_merged.pop(i) 
            else:
                dupeFound = False
        current+=1 
    return skyline_merged  
buildings = [[2,9,10],[3,6,15],[5,12,12],[13,16,10],[15,17,5]]
print(reductant(getSkyline(0,len(buildings)-1,buildings)))