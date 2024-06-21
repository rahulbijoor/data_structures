class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        
        # Calculate base satisfaction (when grumpy[i] == 0)
        base_satisfaction = 0
        for i in range(n):
            if grumpy[i] == 0:
                base_satisfaction += customers[i]
        
        # Calculate the additional satisfaction by using the secret technique
        additional_satisfaction = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                additional_satisfaction += customers[i]
        
        max_additional_satisfaction = additional_satisfaction
        
        # Sliding window to calculate the maximum additional satisfaction
        for i in range(minutes, n):
            if grumpy[i] == 1:
                additional_satisfaction += customers[i]
            if grumpy[i - minutes] == 1:
                additional_satisfaction -= customers[i - minutes]
            max_additional_satisfaction = max(max_additional_satisfaction, additional_satisfaction)
        
        # The maximum number of satisfied customers is the sum of base and max additional satisfaction
        return base_satisfaction + max_additional_satisfaction