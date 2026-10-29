class Solution:
    def isPalindrome(self, x: int) -> bool:
        res = 0
        temp = x
        if x <= -1:
            return False
        while x:
            res = res * 10 + (x%10)
            x//=10
        return True if (res == temp) else False