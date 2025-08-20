# An agricultural research institute monitors the daily yield of maize from various farms. Each farm submits the number of bags harvested each day, and the central database stores them in chronological order. However, due to weather changes, they want to identify the lowest yield day for analysis. The function must return the minimum value in the dataset along with the day index it ocurred. The institute plans to run this calculation every month, so the solution must adapt to any dataset size.
# Input: [45, 60, 38, 55, 70, 42, 39, 48 ]
# Output: 'Lowest yield: 38 bags on day 2'

def agric_research_yield(yields):
    if len(yields) == 0:
        return "Empty Dataset"
    
    min_yield = yields[0]
    min_index = 0
    
    for i in range(1, len(yields)):
        if yields[i] < min_yield:
            min_yield = yields[i]
            min_index = i
            
    return f'Lowest yield: {min_yield} bags on day {min_index}'

# Example usage:
input_data = [45, 60, 38, 55, 70, 42, 39, 48]
result = agric_research_yield(input_data)
print(result)  # Output: 'Lowest yield: 38 bags on day 2'