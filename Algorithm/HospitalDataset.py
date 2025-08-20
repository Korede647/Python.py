# A Hospital Pharmacy monitors daily drug consumption for several medicines. Each medicine's consumption is recorded for a week. The hospital wants to detect if any medicine had zero consumptions for two consecutive days, which might indicate stock shortage or reporting error. Your function should scan the dataset and flag all such medicines.
# Input [[5, 0, 0, 4, 6, 5, 4], [3, 1, 0, 2, 0, 1, 2], [0, 0, 0, 0, 0, 0, 0]] 
# Output [[5, 0, 0, 4, 6, 5, 4], [0, 0, 0, 0, 0, 0, 0]]

def hospitalDataset(medicines):
    if len(medicines) == 0:
        return "Empty Dataset"
    
    flagged_medicines = []
    
    for medicine in medicines:
        for i in range(len(medicine) - 1):
            if medicine[i] == 0 and medicine[i + 1] == 0:
                flagged_medicines.append(medicine)
                break
    
    return flagged_medicines

# Example usage:

print(hospitalDataset([[5, 0, 0, 4, 6, 5, 4], [3, 1, 0, 2, 0, 1, 2], [0, 0, 0, 0, 0, 0, 0]])) # [[5, 0, 0, 4, 6, 5, 4], [0, 0, 0, 0, 0, 0, 0]]