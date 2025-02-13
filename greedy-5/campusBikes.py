#Time: O(mn)
#Space: O(n)
#Program ran on leetcode successfully

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        
        results = [None for i in range(len(workers))]
        
        distances = defaultdict(list)
        
        for worker_index, worker in enumerate(workers):            
            for bike_index, bike in enumerate(bikes):                
                distance = self.get_distance(worker, bike)                
                distances[distance].append([worker_index, bike_index])
                        
        assigned_workers = set()
        assigned_bikes = set()
        
        for key in sorted(distances.keys()):            
            for pair in distances[key]:
                if pair[0] not in assigned_workers and pair[1] not in assigned_bikes:
                    results[pair[0]] = pair[1]

                    assigned_workers.add(pair[0])
                    assigned_bikes.add(pair[1])

                
        return results
        
        
    def get_distance(self, worker, bike):
        return abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])