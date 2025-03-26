# https://www.codingninjas.com/studio/problems/next-greater-permutation_6929564?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=0
from typing import *
def nextGreaterPermutation(A : List[int]) -> List[int]:
    # Write your code here.

    # def permute(idx, ls=[1,2,3]):
     
    #         if idx == len(ls):
    #             print(ls)
    #             return
     
    #         for i in range(idx, len(ls)):
    #             #print(i, idx)
    #             ls[i], ls[idx] = ls[idx], ls[i]
    #             #print(ls)
    #             permute(idx+1, ls)
    #             ls[i], ls[idx] = ls[idx], ls[i]
    
    ## Solution using breaking point.
    n = len(A)

    ##find the breaking point where i < i + 1 
    ###starting from reverse cuz need to stop at the first break point.
    ###from n-2 -> 0
    break_point = -1
    for i in range(n-2, -1, -1):
        if A[i] < A[i+1]:
            break_point = i 
            break 

    if break_point != -1:

        ###swap the break point idx with the smalles index from break_point_idx to N
        for i in range(n-1, break_point, -1):
            if A[i] > A[break_point]:
                A[i], A[break_point] = A[break_point], A[i]
                break
        
        ###reverse or sort the array from breaking_point+1 to N 

        start = break_point+1
        end = n - 1

    else:
        start = 0
        end = n - 1

    while start < end:

        ##swap 
        A[start], A[end] = A[end], A[start]

        start += 1
        end -= 1
    
    return A 

# https://www.codingninjas.com/studio/problems/superior-elements_6783446?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=1
from typing import *

def superiorElements(a : List[int]) -> List[int]:
    # Write your code here.
    '''
    1. Using two for loops. 
    2. sort the answer 
    '''

    ### Brute Force Approach 
    ## TC: O(N^2) + O(NlogN) + o(N) for creating the set
    ## SC: O(N)
    # out = []
    # n = len(a)

    ### O(N^2)
    # for i in range(n): # O(N)
    #     is_superior = True
    #     ###find if idx i is a superior element. 
    #     for j in range(i+1, n): # O(n-1)
    #         if a[i] < a[j]:
    #             is_superior = False 
    #             break  
        
    #     if is_superior:
    #         out.append(a[i])
    
    # out.append(a[n-1])

    # return sorted(set(out)) #nlog(n) + o(n)

    '''
    Starting from the last index to n 
    Keep storing, greatest element from the right 
    If the current element is greater then greatest_right_element add it to out.
    In this case sorting was not needed. As the greatest elements will be at the start.
    '''

    n = len(a)
    out = []
    greatest_right = a[n-1]
    out.append(greatest_right)

    for i in range(n-2, -1, -1):

        if a[i] > greatest_right:
            greatest_right = a[i]
            out.append(a[i])
    
    return out

# https://www.codingninjas.com/studio/problems/longest-successive-elements_6811740?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=1

from typing import *

def longestSuccessiveElements(a : List[int]) -> int:
    # Write your code here.
    ### Brute Force Approach.
    ### TC: O(NlogN) + O(N) 
    ### SC: O(1)

    # length = 1
    # n = len(a)
    # a.sort() ##(NlogN)
    # prev = a[0]
    # ans = 1 

    
    # ###duplicates are ignored. 
    # for i in range(1, n): ## O(N)

    #     if a[i] == prev + 1:
    #         length += 1
    #     ###to discontinue a sequence and start a new one
    #     elif a[i] != prev: ###if duplicate do nothing. 
    #         length = 1
        
    #     prev = a[i]
    #     ### can have multiple answers.
    #     ans = max(ans, length)


    # return ans 

    ###can use set to remove duplicates and remove sorting.
    ###if we store in set the look up is O(1) hence no need to maintain the order.
    ###to calcualte length just need to check if item + 1 in set else stop. 
    ###now to find the best/correct item need to check if item - 1 should not be in set.
    ###if item - 1 is present in set then you should start counting from item - 1 and not item
    ###if you count from item your length will be less than one. 

    #### create a sec 
    hashmap = set(a)
    length = 1
    ans = 0

    for i in a:
        if i - 1 not in hashmap: ###meaning i is the first one (start of sequence.)
           ### now start counting till i + 1 is in set
            length = 0
            num = i

            while num in hashmap:
               length += 1
               num += 1

            ans = max(length, ans)
    
    return ans 


# https://www.codingninjas.com/studio/problems/zero-matrix_1171153?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=0
from os import *
from sys import *
from collections import *
from math import *

def zeroMatrix(matrix, n, m):
    # Write your code here.

    ###Brute force will be find the zero and set the corrosponding row and column to zero. 
    ### TC: N*M*(M+N) + N*M
    ### SC: O(1)
    # for i in range(n):
    #     for j in range(m):

    #         if matrix[i][j] == 0:
    #             ###make the row zero
    #             for col in range(m):
    #                 if matrix[i][col] == 0: continue
    #                 matrix[i][col] = None
                
    #             ###make the col zero 
    #             for row in range(n):
    #                 if matrix[row][j] == 0: continue
    #                 matrix[row][j] = None
    
    # for i in range(n):
    #     for j in range(m):

    #         if not matrix[i][j]:
    #             matrix[i][j] = 0

    # return matrix

    ### Better Approach 
    ### Use a row and column vector to store when col and row needs to be zero
    ### TC: O(2(N*M)) ~ O(N*M)
    ### SC: O(N) + O(M)

    # row = [0] * n  
    # col = [0] * m 

    # for i in range(n):
    #     for j in range(m):
    #         if matrix[i][j] == 0:
    #             row[i] = 1
    #             col[j] = 1 
    
    # # print(row)
    # # print(col)

    # for i in range(n):
    #     for j in range(m):
    #         if row[i] == 1 or col[j] == 1:
    #             matrix[i][j] = 0
    
    # return matrix

    ###optimal approach use the matrix to store the row and col values where i,j is zeros.
    ###Why does this work?
    ###For any i,j which is zero say 2,1 or 2,2 or 3,4 the 0th row and col will always be zeros 
    ### eg for 2,1 (2,0) and (0,2) will be set to zero 
    ### Hence we can use the 0th row and col to store the values instead of using an extra row and col matrix.

    ### Algorithem 
    ### 1. If matrix[i][j] == 0 then
        ### if set matrix[0][j] == 0 and matrix[i][0] == 0
    ### special case since 0,0 is used to set 0th row and 0th col
    ### need a extra variable col_0 to set when col_0 needs to be 0

    ###TC: O(N*M)
    ###SC: O(1)
    col_0 = 0

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                ###set the 0th col to 0
                if j == 0:
                    col_0 = 1
                else:
                    matrix[0][j] = 0
                
                ###set the 0th row to 0 
                matrix[i][0] = 0
    
    ###mark the remaining rows/cols to zero 
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j] != 0 and (matrix[0][j]==0 or matrix[i][0] == 0):
                matrix[i][j] = 0
    
    ###if matrix[0][0] is 0 then set the entire row to zero
    if matrix[0][0] == 0:
        for i in range(m):
            matrix[0][i] = 0

    ###if col_0 == 1 set the 0th row to 0
    if col_0==1:
        for i in range(n):
            matrix[i][0] = 0
    


    return matrix

# https://takeuforward.org/data-structure/rotate-image-by-90-degree/                
### For Brute force: create a new array for size nxn and replace every i th row with n-i column
from typing import *

def rotateMatrix(mat : List[List[int]]):
    # Write your code here.
    ### take transpose and reverse the rows 
    ## TC: N^2 + N^2 
    ## SC: O(1)
    n = len(mat)

    # print(mat)

    for i in range(n):
        for j in range(i+1, n):
            if i == j: continue
            # print(mat[i][j], mat[j][i])
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    
    # for i in mat:
        # print(i)

    ###reverse each row 
    for i in range(n):
        ### 0-th -> n col 
        for j in range(n//2):
            mat[i][j], mat[i][n-1-j] = mat[i][n-1-j], mat[i][j]
    
    return mat


# https://takeuforward.org/data-structure/spiral-traversal-of-matrix/

##***very important.
#https://www.codingninjas.com/studio/problems/print-pascal-s-triangle_6917910?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=1
'''
Main formula from strivers 

>>> O(N) formular for getting a single element 

1. nCr = n!/(n-r)! * r! => n * n(n-1).. * (n-r+1)/r * (r-1) .. * 1
   -> both (n-r)! terms cancel output.

   In code we can make it even simplerer, by rewriting the formula as (reverse the denominator)
   
   nCr => (n / 1) * (n / 2) ... (n-(r-1)) / r
    
    
>>> O(N) formula to generate the whole row. 

1. current_element = previous_element * (row - col_idx) / col_idx, where col_idx goes from 1, n

'''

def nCr(n, r):
    ### TC: O(r)
    ### SC: O(1)
    ans = 1
    for i in range(r):
        ans = ans * (n - i) // (i + 1)
    return ans 

def pascal_nth_row(n):
    ### TC: O(N)
    ### SC: O(1)
    
    out = [1]
    
    prev = 1 
    for i in range(1, n):
        curr = prev * (n - i) // i
        out.append(curr)
        prev = curr
    return out


###strivers generate pascalls triangle is 

def pascalTriangle(n):
    
    ans = []
    
    for i in range(1, n+1):
        
        ans.append(pascal_nth_row(i))
    
    return ans 


from typing import *
def pascalTriangle(n : int) -> List[List[int]]:
    # Write your code here.
    ###TC: O(N^2) optimal solution
    ###SC: O(1)

    ans = [[1], [1,1]]

    if n == 1: [ans[0]]

    if n == 2: ans


    # for i in range(n-2):
    #     tmp = []
    #     prev = 0
    #     for i in ans[-1]:
    #         tmp.append(prev+i)
    #         prev = i
    #     tmp.append(1)
    #     ans.append(tmp)
    
    
    ##To remove n
    for i in range(n-2):
        ans.append([])
        prev = 0
        for i in ans[-2]:
            ans[-1].append(i + prev)
            prev = i
        
        ans[-1].append(1)

    return ans

# https://takeuforward.org/data-structure/merge-two-sorted-arrays-without-extra-space/

from typing import *

def mergeTwoSortedArraysWithoutExtraSpace(a : List[int], b : List[int]):
    # Write your code here.
    
    ###Brute Force 
    ### TC: O(M+N)
    ### SC: O(M+N)
    # ans = []

    len_a = len(a)
    len_b = len(b)

    # p1 = 0
    # p2 = 0

    # while p1 < len_a and p2 < len_b:

    #     if a[p1] == b[p2]:
    #         ans.append(a[p1])
    #         ans.append(b[p2])
    #         p1 += 1
    #         p2 += 1
    #     elif a[p1] < b[p2]:
    #         # print('->', a[p1])
    #         ans.append(a[p1])
    #         p1 += 1
    #     else:
    #         # print('---', b[p2])
    #         ans.append(b[p2])
    #         p2 += 1 

    # # print(ans)

    # ####if elements are remaining insert them 
    # while p1 < len_a:
    #     # print('-----', a[p1])/
    #     ans.append(a[p1]) 
    #     p1 += 1

    # ###if  elements are remaining in b insert them.  
    # while p2 < len_b:
    #     # print('-----', b[p2])
    #     ans.append(b[p2])
    #     p2 += 1
     
    # # print(ans)
    # a = ans[:len_a]
    # b = ans[len_a:]

    # return ans

    ## Solutions from striver.

    ##A better approach is to move all bigger elements to array b
    ##in going this all elements in array a will be smaller 
    ##we then sort both the arrays.

    ###TC: O(N+M) + Nlog(N) + Mlog(M)
    ###SC: O(1)

    left = len_a - 1
    right = 0 

    ###O(N+M)
    while left >= 0 and right < len_b:

        if a[left] > b[right]:
            a[left], b[right] = b[right], a[left]
            left -= 1
            right += 1
        elif a[left] <= b[right]:
            # left -= 1
            # right += 1
            break 
    
    a.sort() ##Nlog(N)
    b.sort() ##Mlog(M)
    
# https://www.codingninjas.com/studio/problems/three-sum_6922132?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=1
###Time Complexity : O(n^2)  
# Space Complexity : O(3*k)  // k is the no.of triplets. 
def triplet(n: int, arr: [int]) -> [[int]]:
    # Write your code here.
    
    ###brute force approach N^3 
    # s = set()
    # out = []
    # for i in range(n):
    #     for j in range(i+1, n):
    #         for k in range(j+1, n):

    #             if arr[i] + arr[j] + arr[k] == 0:
    #                 item = [arr[i], arr[j], arr[k]]
    #                 if tuple(sorted(item)) not in s: 
    #                     out.append(item)
    #                     s.add(tuple(sorted(item)))
    # return out

    ### Using three pointer approach 
    ### j and k will be the moving pointers 
    ### where i stays fixed and j and k perform 2 sum for n times
    ### TC: O(N^2) + Nlog(N), 2 pointer approach requires sorted array.
    ### SC: O(1)

    out = []

    arr.sort() ##Nlog(N)

    for i in range(n):

        if i > 0 and arr[i] == arr[i-1]: continue

        j = i + 1
        k = n - 1 ###this will say the same. 

        while j < k:

            s = arr[i] + arr[j] + arr[k]

            if s == 0:
                out.append([arr[i], arr[j], arr[k]])

                while j < k and arr[j] == arr[j+1]: j += 1 

                while j < k and arr[k] == arr[k-1]: k -= 1

                k -= 1
                j += 1

            elif s > 0:
                k -= 1
            else:
                j += 1
    
    return out
            

