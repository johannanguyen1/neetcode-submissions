class Solution:
    def hammingWeight(self, n: int) -> int:
        b = bin(n)
        num = 0
        print(b)

        for i in range(len(b)): 
            if b[i:i+1] == "1":
                num = num + 1

        return num