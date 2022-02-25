"""Each letter in a sentence is worth its position in the alphabet (i.e. a = 1, b = 2, c = 3, etc...).
However, if a word is all in UPPERCASE, the value of that word is doubled.

Create a function which returns the value of a sentence.

getSentenceValue("abc ABC Abc") ➞ 24
// a = 1, b = 2, c = 3

// abc = 1 + 2 + 3 = 6
// ABC = (1+2+3) * 2 = 12 (ALL letters are in uppercase)
// Abc = 1 + 2 + 3 = 6 (NOT ALL letters are in uppercase)
// 6 + 12 + 6 = 24"""



s = "Abc abc ABC"
from builtins import len
def getSentenceValue(s):
    li = s.split(" ")
    ans = 0
    i = 0
    for x in li:
        sum = 0
        arr = x
        j = 0
        if arr.islower():
            while j < len(x):
                sum += (ord(arr[j])-ord("a")+1)
                j = j+1
            ans = ans+sum

        elif arr.isupper():
            print()
            while j < len(x):
                sum = sum + (ord(arr[j])-ord("A")+1)
                j = j +1
            ans = ans+ (sum *2)
        else:
            while j <len(x):
                l= arr[j].lower()

                sum = sum + (ord(l)-ord("a")+1)

                j = j +1
            ans = ans +sum
    return ans


print(getSentenceValue("HELLO world ?"))
