class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_a = {}
        counter_b = {}
        for alp in s:
            if alp not in counter_a:
                counter_a[alp] = 0
            counter_a[alp] += 1
        
        for alp in t:
            if alp not in counter_b:
                counter_b[alp] = 0
            counter_b[alp] += 1

        return counter_a == counter_b