def getMinDiff(arr, n, k):
    # code here
    """
    Ans needs to be minimum different.
    After sorting need to find two adjacent elements. 
    as difference between them will be smallest. Hence all
    min values can be +k ed and max value can be -k ed. 
    hence i is -k and i - 1 +ked.
    
    """
    arr.sort()
    
    maxi = arr[-1]
    mini = arr[0]
    ans = maxi - mini 
    
    possiable_mini = arr[0] + k
    possiable_maxi = arr[-1] - k
    
    #### need to find two adjcent elements who will be new mini and maxi 
    #### after sorting i - mini , i + 1 maxi
    #### OR i - 1 (new maxi) and i is new mini
    for i in range(n):
        
        if arr[i] - k < 0: continue 
    
        maxi = max(possiable_maxi, arr[i-1] + k)
        mini = min(possiable_mini, arr[i] - k)
        
        ans = min(ans, maxi - mini)
    
    return ans