class Solution:
    def isPalindrome(slef, x: int) ->bool:
        myString = str(x)
        for i in range(len(myString)//2):
            if myString[i]==myString[~i]:
                continue
            else: return False
        return True