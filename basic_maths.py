# https://www.codingninjas.com/studio/problems/count-digits_8416387?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=0
def countDigits(n: int) -> int:
    
    counter = 0
    m = n

    while n > 0:
        
        digit = n % 10
        
        if digit != 0 and m % digit == 0: counter += 1
        
        n = n // 10
    
    return counter 

# https://www.codingninjas.com/studio/problems/reverse-bits_2181102?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=0

def reverseBits(n):
    # Write your code here.
    s1 = bin(n)[2:]
    s1 = '0' * (32-len(s1)) + s1 
    return int(s1[::-1],2)

"""
    Time Complexity: O(1)
    Space Complexity: O(1)
"""

def reverseBits(n):
    # 'bits' array to store the bits representation of 'n'.
    bits = [0]*32

    # Preparing the bits array.
    for i in range(32):
        # If the ith bit is set.
        if (n & (1 << i)) > 0:
            bits[i] = 1

    for i in range(16):
        # Swapping the left and rightmost bits.
        bits[i], bits[31-i] = bits[31-i], bits[i]

    # 'ans' will store the value for the reversed bits representation.
    ans = 0

    for i in range(32):
        # If the i'th bit is set.
        if bits[i] == 1:
            ans += (1 << i)

    return ans


# https://www.codingninjas.com/studio/problems/palindrome-number_624662?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=0
n=int(input())  
# taking n as a input 
## write your code !!
m = n
rev = 0
while n > 0:

    d = n % 10 
    rev = rev * 10 + d
    n = n // 10

if rev == m:
    print('true')
else:
    print('false')


# https://www.codingninjas.com/studio/problems/hcf-and-lcm_840448?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=0

# Write your code here
n, m = list(map(int, input().split()))

def gcd(n, m):

    x = min(n, m)
    
    ans = 1

    for i in range(2, x+1):

        if n % i == 0 and m % i == 0:
            ans = i
    
    return ans 

print(gcd(n,m))

# https://www.codingninjas.com/studio/problems/check-armstrong_589?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *

n = int(input())

m = n 
res = 0
count = 0

while n > 0:
    count += 1
    n = n // 10

n = m 

while n > 0:

    d = n % 10 

    res += pow(d, count)

    n = n // 10 

if res == m:
    print('true')
else:
    print('false')

# https://www.codingninjas.com/studio/problems/sum-of-all-divisors_8360720?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=2
## TC: O(N)
def sumOfAllDivisors(n: int) -> int:
    # Write your code here
    
    def get_divisors(x):

        if x == 1: return 1 
        
        res = x + 1 #the 1 and number x are divisior of x

        for i in range(2, x):
            if x % i == 0:
                res += i
        
        return res
    

    out = 0
    for i in range(1, n+1):
        out += get_divisors(i)

    return out


##TC: Sqrt(N) using harmonic lemma

### if a divisor divides a number then its quotient also divides the number. hence we dont need to go from 1 till we can stop sqrt(N)

from math import *
def sumOfAllDivisors(n: int) -> int:
    # Write your code here
    
    def get_divisors(x):

        # if x == 1: return 1 
        
        # res = x + 1 #the 1 and number x are divisior of x

        # for i in range(2, x):
        #     if x % i == 0:
        #         res += i
        
        # return res
        res = 0
        for i in range(1, int(sqrt(x))+1):
            
            if x % i == 0:
                ##perfect square
                if x//i == i:
                    res += i
                else:
                    ###add the quotient as its a divisor 
                    ###it comes after the sqroot.
                    res += i + x // i

        return res

    out = 0
    for i in range(1, n+1):
        out += get_divisors(i)

    return out


# https://www.codingninjas.com/studio/problems/check-prime_624934?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=1

from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())

flag = -1

for i in range(2, int(sqrt(n))+1):

    if n % i == 0:
        flag = 1
        break 

if flag == 1 or n == 1:
    print('NO')
else:
    print('YES')


