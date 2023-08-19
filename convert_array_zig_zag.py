def zigZag(arr, n):
    
    print(arr, n)

    ans = []

    """
    < sign is going to be 1
    > sign is going to be 0
    """

    def check(i, sign, out):

        if sign == False and out[-1] < i: return True 

        if sign == True and out[-1] > i: return True 

        return False 

    # def worker(idx, sign, out):
    #     nonlocal ans 
    #     if idx == n - 1:
    #         print(idx, n, out)
    #         if len(out) == n:

    #             ans.append(out)
    #         return 
        
    #     ##not taking 
    #     worker(idx+1, sign,out)

    #     if not out or check(idx, sign):
    #         worker(idx+1, not sign, out + [arr[idx]])

    def worker(idx, sign, out):

        nonlocal ans 

        if len(out) == n:
            print('added : ', out)
            ans.append(out.copy())
            return True

        if arr == []: return False

        for i in arr:

            # if idx == i: continue 
            print(arr,i,sign,out)
            if out == [] or check(i, sign, out):
                idx = arr.index(i)
                arr.remove(i)
                if worker(arr, not sign, out + [i]):
                    return True
                arr.insert(idx, i)
                
    worker(arr, True, [])

    return ans[0]


if __name__ == '__main__':

    # arr = [4, 3, 7, 8, 6, 2, 1]

    # print(zigZag(arr, len(arr)))

    arr = [1, 4, 3, 2]

    print(zigZag(arr, len(arr)))