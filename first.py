from builtins import len
arr = [2,5,4,8,6,9,4,7]

x = 9



def find(arr, x):
    n = len(arr)

    if n== 0:
        return False
    if arr[n-1] == x:
        flag = True
        return flag
    else:

        j =find(arr[:n-1], x)

    return j





print(find(arr, x))