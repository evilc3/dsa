def minJumps(arr, n):
    #code here
    ans = 0
    i = 0
    while i < n:
        print(ans,i, arr[i+1:i+1+arr[i]])
        next_step = max(arr[i+1:i+1+arr[i]])
        
        ans += 1

        i += next_step
    
    return ans 

if __name__ == '__main__':

    arr = [1,4,3,2,6,7]
    arr = [1,2,1,3,4,6,7]
    arr = [2,3,1,1,2,4,2,0,1,1]
    print(minJumps(arr, len(arr)))