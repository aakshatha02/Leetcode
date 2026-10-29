class Solution:
    def isPalindrome(self, x: int) -> bool:
        res = 0
        temp = x
        while temp > 0:
            res = res * 10 + (temp%10)
            temp//=10
        return res == x