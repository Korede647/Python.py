

def hospitalDataset(list):
    for i in range (len(list)):
        for j in range(i + 1, len(list)):
            if list[i] and list[j] == 0:
                return list
    return "None"


print(hospitalDataset([[5, 0, 0, 4, 6, 5, 4], [3, 1, 0, 2, 0, 1, 2], [0, 0, 0, 0, 0, 0, 0]])) # [[5, 0, 0, 4, 6, 5, 4], [0, 0, 0, 0, 0, 0, 0]]