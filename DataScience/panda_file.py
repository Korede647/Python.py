import pandas as pd

data = {
    "Name": ["John", "Korede", "Daniel", "Sarah"],
    "Age":  [23, 25, 22, 24],
    "City": ["Lagos", "Abuja", "Kano", "Port Harcourt"]
    }

df = pd.DataFrame(data)
# print(df)

examData = {
    "Name": ["Mike", "David", "Daniel", "Korede", "Stephanie", "Frank"],
    "Study Hours": [5, 3, 8, 2, 7, 4],
    "Sleep Hours": [7, 6, 6, 5, 8, 7],
    "Score": [80, 60, 92, 55, 88, 72]
}

viewData = pd.DataFrame(examData)
# print("====Data======")
# print(viewData)
# print("====Info======")
# print(viewData.info())
# print("====Describe======")
# print(viewData.describe())

titanic_data = pd.read_csv("DataScience/titanic.csv")
print(titanic_data.head())
# print(titanic_data.tail())  