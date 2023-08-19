'''
Problem Statement: Given an array containing integers [1,2,3] denoting jobs, and k painters you task is to split the jobs among the k painters 
such that each painter is assigned at least one job, split the jobs such that the partation has the min time required to complete the job.

Example3

arr = [1, 2, 3, 4]  k = 2

Different Partitions:
k1 = [1], k2 = [2,3,4]    ans = k1 = 1, k2 = 9 max time 9
k1 = [1, 2] , k2 = [3, 4] ans = k1 = 3, k2 = 7 max time 7
k1 = [1, 2, 3], k2 = [4]  ans = k1 = 6, k2 = 4 max time 6

ans = 6, partition k1 = [1, 2, 3], k2 = [4]

-------
Example 2

arr = [1, 2, 3, 4]  k = 3

Different Partitions:
k1 = [1], k2 = [2], k3 = [3,4]  ans = k1=1, k2=2, k3=7 max time 7
k1 = [1], k2 = [2,3], k3 = [4]  ans = k1=1, k2=5, k3=4 max time 5
k1 = [1,2], k2 = [3], k3 = [4]  ans = k1=3, k2=3, k3=4 max time 4

ans = 4, partition k1 = [1,2], k2 = [3], k3 = [4]

Solving Using DP

Draw the recursive tree.

            [1, 2, 3, 4], k =3
         k=3[1]         [1, 2]

    k=2[2]     [2,3]      [3]

    k=1[3,4]    [4]       [4]

base case: if k == 1: sum(arr[i:N])
Need to make sure that each painter gets at least 1 job, so inner loop needs to run for i=0 -> i<=N+1-K

k1 = 1 2      0, [4-3=1]
k2 = 2        2, [4-2=2]


[1,2,3,4,5,6,7] k = 3

k=3[1 3 6]
k=2[0 2 5 9]
NxK




'''

def worker(arr, k, start, n):
    if k == 1:
        return sum(arr[start:n])
    if n == 1: return arr[0]
    ans = 10000
    for i in range(start, n-k+1):
        ans = min(ans, max(sum(arr[start:i+1]), worker(arr, k-1, i+1, n)))

    return ans

def worker_dp(arr, k, start, n, dp):
    if k == 1:
        return sum(arr[start:n])
    if n == 1: return arr[0]
    if dp[start][k] != 0:
        return dp[start][k]

    ans = 10000
    for i in range(start, n-k+1):
        ans = min(ans, max(sum(arr[start:i+1]), worker_dp(arr, k-1, i+1, n, dp)))
    dp[start][k] = ans
    return dp[start][k]

def partition_painters(arr, k):
    dp = [[0 for _ in range(k+1)] for _ in range(len(arr)+1)]
    # print(dp)
    return worker_dp(arr, k, 0, len(arr), dp)

if __name__ == '__main__':

    # print(partition_painters(arr=[1,2,3,4], k=2))
    # print(partition_painters(arr=[1,2,3,4], k=3))

    print(partition_painters(arr=[5,5,5,5], k=2))
    print(partition_painters(arr=[10,20,30,40], k=2))

    print(partition_painters(arr=[48,90], k = 2))