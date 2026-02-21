t=(1,2,2,3,2,2,1)
def palind(r):
    end=len(r)-1
    start=0
    while (start>end):
        if r[start]!=r[end]:
            return False
    end=end-1
    start=start+1
    return True


if palind(t):
    print("palindrome is present")
else:
    print("pallindrome is not present")