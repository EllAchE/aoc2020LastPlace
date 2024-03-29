# --- Part Two ---
# Now that you've identified which tickets contain invalid values, discard those tickets entirely. Use the remaining valid tickets to determine which field is which.

# Using the valid ranges for each field, determine what order the fields appear on the tickets. The order is consistent between all tickets: if seat is the third field, it is the third field on every ticket, including your ticket.

# For example, suppose you have the following notes:

# class: 0-1 or 4-19
# row: 0-5 or 8-19
# seat: 0-13 or 16-19

# your ticket:
# 11,12,13

# nearby tickets:
# 3,9,18
# 15,1,5
# 5,14,9
# Based on the nearby tickets in the above example, the first position must be row, the second position must be class, and the third position must be seat; you can conclude that in your ticket, class is 12, row is 11, and seat is 13.

# Once you work out which field is which, look for the six fields on your ticket that start with the word departure. What do you get if you multiply those six values together?

class Field:
    def __init__(self, name, range_set, lower_mid, upper_mid):
        self.name = name
        self.range_set = range_set
        self.max = max(range_set)
        self.min = min(range_set)
        self.lower_mid = lower_mid
        self.upper_mid = upper_mid


data = open("input.txt").readlines()

tickets = []
fieldDefinitions = []
fieldNames = list()
range_set = set()

for line in data:
    if "ticket" in line:
        continue
    elif ":" in line:
        temp_range_set = set()
        name, ranges = line.split(": ")
        a, b = ranges.split(" or ")
        x1, y1 = [int(z) for z in a.split("-")]
        x2, y2 = [int(z) for z in b.split("-")]
        range_set |= set(range(x1, y1 + 1)).union(set(range(x2, y2 + 1)))
        temp_range_set |= set(range(x1, y1 + 1)).union(set(range(x2, y2 + 1)))
        fieldDefinitions.append(Field(name, temp_range_set, y1, x2))
    elif "," in line:
        validTicket = True
        ticket = [int(l) for l in line.split(",")]
        for field in ticket:
            if field not in range_set:
                validTicket = False
        if validTicket:
            tickets.append(ticket)

i = 0
while i < 20:
    invalid_field_names = list(list())
    temp_set = set()
    for tick in tickets:
        temp_set.add(tick[i])
    #print ('temp_set_max', max(temp_set), 'temp_set_min', min(temp_set))
    for field in fieldDefinitions:
        #print sorted(temp_set)
        #print ('max field range', field.max, 'min', field.min, 'lower mid', field.lower_mid, 'upper mid', field.upper_mid)
        for val in temp_set:
           if ((val > field.min and val < field.lower_mid) or (val < field.max and val > field.upper_mid)):
               pass
           else:
               #print ('out of range', val)
               invalid_field_names = invalid_field_names.__add__([field.name])
    invalid_field_names = list(set(invalid_field_names))
    #print invalid_field_names
    #print len(invalid_field_names)
    fieldNames.append(invalid_field_names)
    i = i + 1

fieldNames.sort(key=len, reverse=True)
all_field_names = list()

#FROM HERE WE JUST NEED THE SYMMETRIC DIFFERENCE THEN TO ELIMINATE OPTIONS

for f in fieldDefinitions:
    all_field_names.append(f.name)
print all_field_names
#for fieldSet in fieldNames:
 #   print fieldSet



