

def geo_drill_max(list):
    if len(list) == 0:
        return "Empty Dataset"
    first = list[0]
    for i in list[1:]:
        if i > first:
            first = i
        elif first > i:
            i = first      
    return f'Highest discovery: {first} barrels at position {list.index(first)}'


# Example

print(geo_drill_max([300, 450, 120, 800, 540, 760, 310, 900, 500, 620]))