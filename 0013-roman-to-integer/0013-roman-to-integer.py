class Solution:
    def romanToInt(self,roman_n):
        total = 0
        d = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
    
        for i in range(len(roman_n)-1):
            current = roman_n[i]
            nxt  = roman_n[i+1]
            if d[current] < d[nxt]:
                total = total - d[current]
            else:
                total = total + d[current]
                
        total = total + d[roman_n[-1]]
        return total