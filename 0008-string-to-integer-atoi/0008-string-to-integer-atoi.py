class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)

        # 1. Skip leading spaces

        while i < n and s[i] == ' ':
            i += 1

        # 2. Check the sign

        sign = 1
        if i < n and s[i] == '-':
            sign = -1
            i+=1
        elif i < n and s[i] == '+':
            i += 1

        # 3. Build the number digit by digit
        num = 0
        while i < n and s[i].isdigit():
            num = num * 10 + (ord(s[i]) - ord('0'))
            i += 1
        

        # 4. Apply the sign and clamp to 32-bit range
        num *= sign
        num = max(-2**31, min(num, 2**31 - 1))

        return num