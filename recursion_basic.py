# https://www.codingninjas.com/studio/problems/print-1-to-n_628290?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=0
from typing import List

def printNos(x: int) -> List[int]:
    # Write your code here
    if x == 1: return [1]
    return printNos(x-1) + [x]


def printNtimes(n: int):

    if n == 1: return 'Coding Ninjas'

    return printNtimes(n - 1) + ' Coding Ninjas'

# https://www.codingninjas.com/studio/problems/-print-n-times_8380707?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=1
def printNtimes(n: int):
    if n == 0: return
    print('Coding Ninjas ', end="")
    printNtimes(n-1)

# https://www.codingninjas.com/studio/problems/n-to-1-without-loop_8357243?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=1
from typing import List

def printNos(x: int) -> List[int]:
    # Write your code here
    if x == 1: return [1]
    return [x] + printNos(x-1) 

# https://www.codingninjas.com/studio/problems/reverse-an-array_8365444?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=1
from typing import *

def reverseArray(n: int, nums: List[int]) -> List[int]:
    # Write your code here
    # def worker(n, idx):
    #     if idx == n-1:
    #         return [nums[-1]]
    #     return worker(n, idx+1) + [nums[idx]]

    def worker(n, idx):

        if idx == n-1:
            return [nums[-1]]

        out = worker(n, idx+1)

        out.append(nums[idx])

        return out

    return worker(n, 0)

# https://www.codingninjas.com/studio/problems/check-palindrome-recursive_624386?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=1
def isPalindrome(string: str) -> bool:
    
    # def reverse_string(x):

    #     if x == "": return ""

    #     return reverse_string(x[1:]) + x[0]
    
    # return reverse_string(string) == string

    ### compare 0 and n-1 

    size = len(string)

    ##if even then size can be 0 if odd size will be 1 
    if size <= 1: return True 
    
    if string[0] != string[-1]: return False

    return isPalindrome(string[1:-1])

def get_fibonacci(n, dp):
    
    if n in dp: return dp[n]

    if n <= 0:
        return 0

    if n == 1:
        print('--',1)
        return 1

    if n == 2:
        return 1

    c =  get_fibonacci(n-1,dp) + get_fibonacci(n-2,dp)

    print(c)
    # out.append(c)
    dp[n] = c

    return c 

# https://www.codingninjas.com/studio/problems/print-fibonacci-series_7421617?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=1
from typing import List

def generateFibonacciNumbers(n: int) -> List[int]: 
    # Write your code here
    out = [0, 1]

    if n == 1:
        return [0]
    
    if n == 2:
        return [0, 1]
    
    if n == 3:
        return [0, 1, 1]


    def get_fibonacci(n, dp):
        
        if n in dp: return dp[n]

        if n <= 0:
            return 0

        if n == 1:
            # print('--',1)
            out.append(1)
            return 1

        if n == 2:
            # out.append(1)
            return 1

        c =  get_fibonacci(n-1,dp) + get_fibonacci(n-2,dp)

        out.append(c)
        dp[n] = c

        return c 


    get_fibonacci(n-1, {})

    # print(out)

    return out



if __name__ == '__main__':

    # print(printNtimes(n=3))
    # print(get_fibonacci(3))
    print(get_fibonacci(2,{}))