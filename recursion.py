from builtins import len
"""
                                         FIND ELEMENT PRESENT OR NOT



arr = [1,2,5,4,8,6,9]
x = 2


def find(arr, x):
    n = len(arr)
    if n == 0:
        return False
    if arr[0] ==x:
        return True
    else:
        j = find(arr[1:], x)
    return j


print(find(arr, x))





                                        FIND THE INDEX

from builtins import len
arr = [1,2,2,2,2,2,2,2,4,5,4,7]
x = 99


def first_index(arr, x):
    n = len(arr)
    if n == 0:
        return -1
    if arr[0] ==x:
        return 0
    else:
        j =first_index(arr[1:], x)
        if j == -1:
            return -1
        k = 1+j
    return k


print(first_index(arr, x))

                                FIND INDEX USING START INDEX

from builtins import len
arr = [1,2,2,2,2,2,2,2,4,5,4,7]
x = 2
SI = 0


def Last_occur(arr, x, SI):
    n = len(arr)
    if SI == n:
        return -1

    if SI< n and arr[SI] == x:
        return 0

    else:
        j = Last_occur(arr, x, SI+ 1)
        if j == -1:
            return -1
        k = 1 + j
    return k


print(Last_occur(arr, x, SI))



                                    FIND LAST OCCURANCE


from builtins import len
arr = [1,2,4,5,4]
x = 4

def Last_index(arr, x):
    n = len(arr)
    if n == 0:
        return -1
    if arr[0] == x :
        k = Last_index(arr[1:], x)
        if k == -1:
            return 0
        else:
            return k + 1
    else:
        j = Last_index(arr[1:], x)
        if j == -1:
            return -1
        else:
            return j + 1






print(Last_index(arr, x))
"""
string = "pisndfdsupppijpifnisdnjpi"
def replace_pi(string):
    n = len( string)
    if n == 0 or n == 1:
        return string

    if string[:2] == "pi":
        small_op = replace_pi(string[2:])
        if string[:2] == "pi":
            return "3.14" + small_op
        else:
            return string[0] + small_op
    else:
        small_op = replace_pi(string[1:])
        if string[:2] == "pi":
            return "3.14" + small_op
        else:
            return string[0] + small_op

print(replace_pi(string))
