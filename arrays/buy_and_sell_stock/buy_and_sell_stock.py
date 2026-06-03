class Solution:
    def max_profit(self, prices: list[int]) -> int:
        buy = prices[0]
        max_profit = 0
        for price in prices:
            if price < buy:
                buy = price
            profit= price-buy
            if profit> max_profit:
                max_profit= profit


        return max_profit if max_profit > 0 else 0

    # two pointer technique
    def find_max_profit(self, prices: list[int])-> int:
        buy=0
        sell=1
        max_profit=0
        while sell < len(prices):
            if prices[sell]> prices[buy]:
                profit= prices[sell]- prices[buy]
                max_profit= max(max_profit,profit)
            else:
                # move buy pointer to right
                buy= sell
            sell+=1
        return max_profit if max_profit>0 else 0



p=[7,6,4,3,1]
obj= Solution()
print(obj.find_max_profit(p))