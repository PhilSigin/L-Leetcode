"""
121. Best Time to Buy and Sell Stock

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


Runtime          Memory
700 ms           27.43MB
Beats 80.02%     Beats 23.87%

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        size = len (prices)
        max_price = 0
        max_profit = 0

        for _ in range (size):
            current = prices[size-_-1]
            if current > max_price:
                max_price = current
            if max_price - current > max_profit:
                max_profit = max_price - current
            
        return max_profit
        

        """
        Версия 2, тоже медленная, доходит до 201
        maxim = 0
        size = len (prices)
        for _ in range (size):
            # print("(max ==)", maxim, "--", prices[_], end = " -- ")
            if _ < size-2:
                if prices[_+1]<prices [_] and prices[_+1]>prices[_+2]:
                    prices.pop(_+1)
                    size -=1
                elif prices[_+1]>prices [_] and prices[_+1]<prices[_+2]:
                    prices.pop(_+1)
                    size -=1


        maxim = 0
        size = len (prices)
        for _ in range (size):
            # print("(max ==)", maxim, "--", prices[_], end = " -- ")
            if _ < size-1:
                sliced_array = prices[_+1:]
                # print (sliced_array, end = "")
                biggest_price = max(sliced_array)

                temp2max = biggest_price - prices[_]
                if biggest_price < prices[_]:
                    # print ("  biggest_price > prices[_]:")
                    continue
                    # return maxim
                elif temp2max > maxim:
                    maxim = temp2max




        # print (max) 
        return maxim

        """

        """
        Версия 1, слищком медленная

        maxim = 0
        size = len (prices)
        for _ in range (size):
            # print("(max ==)", maxim, "--", prices[_], end = " -- ")
            if _ < size-1:
                sliced_array = prices[_+1:]
                # print (sliced_array, end = "")
                biggest_price = max(sliced_array)

                temp2max = biggest_price - prices[_]
                if biggest_price < prices[_]:
                    # print ("  biggest_price > prices[_]:")
                    continue
                    # return maxim
                elif temp2max > maxim:
                    maxim = temp2max

        # print (max) 
        return maxim
        """


