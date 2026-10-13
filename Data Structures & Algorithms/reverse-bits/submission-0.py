class Solution:
    def reverseBits(self, n: int) -> int:
        b = bin(n)
        r = str(b)[::-1]
        for i in range(len(r)):
            if r[i:i+1] == "b": 
                z = 32 - i
                copies = z * "0"
                r = r[0:i] + copies
        b = int(r, 2)

        return b 