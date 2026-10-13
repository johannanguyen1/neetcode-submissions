class Solution:
    def countBits(self, n: int) -> List[int]:
        l = []
        for k in range(n):
            l.append(k)
        l.append(n)
        print(l)
        total = 0 
        output = []
        for i in l: 
            b = bin(i)
            for j in range(len(b)):
                if b[j: j+1] == "1": 
                    total = total + 1
            output.append(total)
            total = 0
        return output