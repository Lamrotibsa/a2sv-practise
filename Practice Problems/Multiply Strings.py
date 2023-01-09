class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        intnum1 = 0
        intnum2 = 0

        for i in range(len(num1)):
            val = ord(num1[i]) - 48
            intnum1 = 10 * intnum1 + val

        for i in range(len(num2)):
            val = ord(num2[i]) - 48
            intnum2 = 10 * intnum2 + val

        return str(intnum1 * intnum2)

        



