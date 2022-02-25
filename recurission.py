print("wipro coding question")
"""
print the total number of positive numbers in a space sepreted list

Include 0 too


"""
from builtins import len


n = int(input())
arr = [int(x) for x in input().split()]
def right(arr):
    ans = 0
    if len(arr) == 0:
        return 0
    else:
        for x in arr:
            if x >= 0:
                ans = ans + 1
    return ans


result = right(arr)
print(result)
