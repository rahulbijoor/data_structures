class Solution:
    #Understand
    #Space/ Time ?
    #Empty Grid?
    #Negative numbers?
    #Do all the customers have same number of bank accounts?
    #Match
    #Array
    #Without Array

    #Plan
    #Approach 1
    # create an array of size number of rows in the grid
    # find the sum of each row and append it to the array
    # find the max value in the array

    #Approach two
    # variable max_sum
    # calculate sum of each row
    # if the sum is greater than max_sum then max_sum=sum
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(acc) for acc in accounts])