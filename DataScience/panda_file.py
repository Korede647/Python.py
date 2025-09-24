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
# print(titanic_data.head())
# print(titanic_data.tail())
# print(titanic_data.isnull().sum())

# breastCancerData = pd.read_csv("DataScience/breastCancer.csv")
# print(breastCancerData.head())
# print(breastCancerData.isnull().sum())

# df["Age"].fillna(df["Age"].median(), inplace = True) #replace missing age with average values

print(df.drop("Cabin", axis = 1, inplace= True))

# df["Embarked"].fillna(titanic_data["embarked"].mode()[0], inplace= True) #replace missing values with most common value

# df["Sex"] = titanic_data["Sex"].map({
#     "male": 0,
#     "female": 1
# })

# df.drop(["passengerId", "Ticket", "Name"], axis= 1, inplace= True)