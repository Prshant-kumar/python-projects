"""input n = 4

* * * * 1
* * * 3 2
* *6  5 4
*10 9 8 7"""
n = int(input())
i = 1

m = 0
while i <= n:
    j = 0
    while j < n-i+1:
        print("*", end=" ")
        j = j +1
    m =m+i
    l = m
    k=i
    while k>0:
        print(l, end=" ")
        l = l-1
        k= k-1
    print()
    i = i +1




