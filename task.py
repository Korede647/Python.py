
def speedFine(speed, birthday):
     
     if birthday:
        if speed < 80:
           return "No Fine"
        elif speed <= 85:
            return "Small Fine"
        else:
            return "Big Fine"
     else:
        if speed <= 60:
           return "No Fine"
        elif speed <= 80:
            return "Small Fine"
        else:
            return "Big Fine"

        
print(speedFine(60, False))
print(speedFine(77, False))
print(speedFine(77, True))
print(speedFine(85, False))
print(speedFine(85, True))
