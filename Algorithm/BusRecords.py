# A city bus company records the daily number of passengers for each bus route for each bus route. Due to complaints about overcrowding , management wants to know which routes exceed 100 passengers per day on average. The input data contains each route's daily passenger counts. Your function should return a list of route averages that meet or exceed 100, rounded to the nearest whole number 
# Input [[80, 90, 120,], [105, 110, 115], [70, 85, 95], [130, 140, 125]]
# Output [119, 113, 132]


def bus_route_averages(routes):
    averages = []
    for route in routes:
        average = sum(route) / len(route)
        if average >= 100:
            averages.append(round(average))
    return averages

# Example usage:

input_data = [[80, 90, 120], [105, 110, 115], [70, 85, 95], [130, 140, 125]]
result = bus_route_averages(input_data)
print(result)  # Output: [119, 113, 132]