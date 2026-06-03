### Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Custom Judge:

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

################################################################################

Intuition
We just need to keep track of two numbers: the lowest price We’ve seen so far (to buy at) and the highest profit we could get by selling at the current price. That way, we only look at each price once.

Approach
Let minimum start at the first day's price.

Let max_profit start at 0.

Loop through each day's cost:

If today’s cost is lower than minimum, update minimum.

Otherwise, see if selling today gives me a bigger profit than I’ve seen so far—if yes, update max_profit.

At the end, return max_profit (it’s already non-negative)

Complexity
Time complexity: O(n)
Space complexity: O(1)