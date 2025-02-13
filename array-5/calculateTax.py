#Time: O(n)
#Space: O(1)
#Program ran on leetcode successfully

class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:

        tax = 0
        prev_limit = 0

        for b in brackets:
            limit = b[0]
            rate = b[1]
            tax += (min(limit, income) - prev_limit) * (rate / 100)
            prev_limit = limit

            if limit >= income:
                return tax
        
        return 0

