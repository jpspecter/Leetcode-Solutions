#Time: O(logn)
#Space: O(1)
#Program ran on leetcode successfully

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        if not weights:
            return 1
        
        min_cap = max(weights)
        max_cap = sum(weights)
        
        while min_cap < max_cap:
            curr_cap = min_cap + (max_cap - min_cap) // 2
            
            current_load = 0
            num_days = 1
            
            for i in range(len(weights)):
                if weights[i] + current_load > curr_cap:
                    current_load = weights[i]
                    num_days += 1
                else:
                    current_load += weights[i]
                    
            if num_days <= days:
                max_cap = curr_cap
            else:
                min_cap = curr_cap + 1
                
        return min_cap