class Solution:
    def __init__(self) -> None:
        self.chrs = ('I', 'V', 'X', 'L', 'C', 'D', 'M')
        self.vals = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' :500, 'M' : 1000}
    def romanToInt(self, input: str):
        val = 0
        for i, chr in enumerate(input):
            for x in range(i, len(input)):
                if(self.vals[input[x]]>self.vals[chr]):
                    val -= self.vals[chr]
                    break
                if(x == len(input)-1):
                    val += self.vals[chr]
        return val
    
roman_calc = Solution()
print(roman_calc.romanToInt("MCMXCIV"))
