#Time: O(n^2)
#Space: O(n)
#Program ran on leetcode successfully

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        board.reverse()

        def helperPos(square):
            r = (square - 1) // n
            c = (square - 1) % n
            if r % 2:
                c = n - 1 - c
            return [r, c]
        
        q = deque()
        q.append([1,0])
        visited = set()
        while q:
            square, num_moves = q.popleft()
            for i in range(1, 7):
                nextSq = square + 1
                r, c = helperPos(nextSq)
                if board[r][c] != -1:
                    nextSq = board[r][c]
                
                if nextSq == n * n:
                    return num_moves
                if nextSq not in visited:
                    visited.add(nextSq)
                    q.append([nextSq, num_moves+1])
        
        return -1
