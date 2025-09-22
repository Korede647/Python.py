import pandas as pd

data = {
    "Name": ["John", "Korede", "Daniel", "Sarah"],
    "Age":  [23, 25, 22, 24],
    "City": ["Lagos", "Abuja", "Kano", "Port Harcourt"]
    }

df = pd.DataFrame(data)
print(df)