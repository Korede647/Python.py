# A health NGO collects daily blood pressure readings from volunteers in rural commmunities. The readings are recorded as pairs of systolic and diastolic values in sequence. However, they want to find all readings where systolic pressure exceeds 140 (indicating hypertension). Your function should scan through the dataset and return only those readings that meet the condition. The NGO also insists that the function works even if hundreds of readings are added later without any modification. The results will be used to schedule follow-up medical visits.
# Input: [[120, 80], [150, 95], [138, 85], [145, 92], [160, 100]]
# Output: [(150, 95], [145, 92], [160, 100]]

def health_ngo_hypertension(readings):
    if len(readings) == 0:
        return "Empty Dataset"
    
    hypertensive_readings = []
    
    for reading in readings:
        systolic, diastolic = reading
        if systolic > 140:
            hypertensive_readings.append((systolic, diastolic))
    
    return hypertensive_readings

# Example usage:
input_data = [[120, 80], [150, 95], [138, 85], [145, 92], [160, 100]]
result = health_ngo_hypertension(input_data)
print(result)  # Output: [(150, 95), (145, 92), (160, 100)]