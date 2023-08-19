'''CORRECT: https://practice.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1'''
def maxSubArraySum(arr,N):
    ##Your code here
    
    maxi = float('-inf')
    sum = 0
    for i in arr:
        
        sum += i
        
        maxi = max(maxi, sum)
        
        if sum < 0:
            sum = 0
        
    return maxi 

if __name__ == '__main__':

    arr = [-2,-1, 3,-4,-5, 10, -15, 70]
    print(maxSubArraySum(arr, len(arr)))