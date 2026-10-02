class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0

        c1 = 0
        c2 = 1
        if len(prices) == 1:
            return 0
        cur_p = prices[c2] - prices[c1]
        while c2 < len(prices):
            print(c1, c2, cur_p)

            if prices[c2] < prices[c1]:
                cur_p = 0 
                c1 = c2 
            else:
                cur_p = prices[c2] - prices[c1]
            
            if cur_p > max_p:
                max_p = cur_p
                
            c2 += 1
        
        return max_p