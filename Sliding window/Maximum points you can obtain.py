class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)  
        wsize=n-k
        wsum = sum(cardPoints[:wsize])
        mins = wsum
        if k==n:
            return sum(cardPoints)
        for i in range(wsize, n):
            wsum += cardPoints[i] - cardPoints[i - wsize]
            mins = min(mins, wsum)    
        return sum(cardPoints) - mins
        
