Approach
just traverse the string :
condition if s[firstindex]<s[secondindex] then c-=d[s[firstindex]]
else add the c+=d[s[firstindex]]

Complexity
Time complexity:
Space complexity:
Code
class Solution:
    def romanToInt(self, s: str) -> int:
        d={'I':1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        c=0
        for i in range(len(s)-1):
            if d[s[i+1]]>d[s[i]]:
                c-=d[s[i]]
            else:
                c+=d[s[i]]
        c+=d[s[-1]]
        return c
