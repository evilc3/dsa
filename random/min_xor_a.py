'''
Given two integers A and B, the task is to find an integer X such that (X XOR A)
is minimum possible and the count of set bit in X is equal to the count of set bits in B.

Input: 
A = 3, B = 5
Output: 3
Explanation:
Binary(A) = Binary(3) = 011
Binary(B) = Binary(5) = 101
The XOR will be minimum when x = 3
i.e. (3 XOR 3) = 0 and the number
of set bits in 3 is equal
to the number of set bits in 5.
'''

### incorrect assumption. x can be > b 

# def count_bits(x):

#     count = 0

#     while x:
#         count += x & 1
#         x = x >> 1 
    
#     return  count 


# a = 3
# b = 5
# ans = None
# b_set = count_bits(b)
# print(b_set)

# for x in range(b + 1):
    
#     x_ = a ^ x
    

#     print(x,x_,count_bits(x))
#     if count_bits(x) == b_set:
        
#         if not ans or ans > x_:
#             ans = x 


# print(ans)
        
'''
if set_bit(a) == set_bit(b) => return a 

if set_bit(a) > set_bit(b):
    unset bits of a lowest bits 
else
    unset bits of b set the lowest bits. 


'''

def count(x):

    count = 0

    while x:
        count += x & 1
        x = x >> 1 
    
    return  count 

def minval(a,b):

    c1 = count(a)
    c2 = count(b)

    if c1 == c2: return a 
    
    if c1 > c2:
        diff = c1 - c2
        while(diff > 0):
            a = a & (a - 1)
            diff -= 1
        return a 
    else:
        diff = c2 - c1 
        while(diff > 0):
            a = a | (a + 1)
            diff -= 1
        return a 

print(minval(3,5))
print(minval(5,3))
print(minval(7,12))
print(minval(12,7))











    


