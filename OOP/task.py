class Laptop():
    def __init__(self, id, year, brand, color, RAM, ROM, operatingSystem, size ):
        self.id = id
        self.year = year
        self.brand = brand
        self.color = color
        self.RAM = RAM
        self.ROM = ROM
        self.operatingSystem = operatingSystem
        self.size = size

    def __str__(self):
        return f"{self.id}, Year: {self.year}, Brand: {self.brand}, Color: {self.color}, RAM: {self.RAM}, ROM: {self.ROM}, Operating System: {self.operatingSystem}, Size: {self.size}"
        

Laptops = {
       "1": f"{Laptop("1", "2024", "HP", "Black", "32GB", "520GB", "corei7", "15 inches")}",
       "2": f"{Laptop("2", "2023", "HP",  "Grey", "32GB", "256GB", "corei5", "17 inches")}",
       "3": f"{Laptop("3", "2025", "MacBook", "Black", "32GB", "520GB", "M1 Chip", "14 inches")}",
       "4": f"{Laptop("4", "2020", "HP", "Black", "32GB", "520GB", "corei6", "18 inches")}",
       "5": f"{Laptop("5", "2023", "HP", "Dark blue", "32GB", "1TB", "corei7", "13 inches")}"
}

for values in Laptops.values():
    print(values)

# print(Laptops)