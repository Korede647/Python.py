def speedFine(speed, birthday):
     if speed >= 61 and speed < 80 and not birthday or speed > 80 and birthday:
        return "Small Fine"
     if speed > 80 and not birthday:
        return "Big Fine"
     return "No Fine"
        
print(speedFine(60, False))
print(speedFine(77, False))
print(speedFine(77, True))
print(speedFine(85, False))
print(speedFine(85, True))
