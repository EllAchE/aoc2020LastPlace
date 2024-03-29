# --- Day 16: Ticket Translation ---
# As you're walking to yet another connecting flight, you realize that one of the legs of your re-routed trip coming up is on a high-speed train. However, the train ticket you were given is in a language you don't understand. You should probably figure out what it says before you get to the train station after the next flight.

# Unfortunately, you can't actually read the words on the ticket. You can, however, read the numbers, and so you figure out the fields these tickets must have and the valid ranges for values in those fields.

# You collect the rules for ticket fields, the numbers on your ticket, and the numbers on other nearby tickets for the same train service (via the airport security cameras) together into a single document you can reference (your puzzle input).

# The rules for ticket fields specify a list of fields that exist somewhere on the ticket and the valid ranges of values for each field. For example, a rule like class: 1-3 or 5-7 means that one of the fields in every ticket is named class and can be any value in the ranges 1-3 or 5-7 (inclusive, such that 3 and 5 are both valid in this field, but 4 is not).

# Each ticket is represented by a single line of comma-separated values. The values are the numbers on the ticket in the order they appear; every ticket has the same format. For example, consider this ticket:

# .--------------------------------------------------------.
# | ????: 101    ?????: 102   ??????????: 103     ???: 104 |
# |                                                        |
# | ??: 301  ??: 302             ???????: 303      ??????? |
# | ??: 401  ??: 402           ???? ????: 403    ????????? |
# '--------------------------------------------------------'
# Here, ? represents text in a language you don't understand. This ticket might be represented as 101,102,103,104,301,302,303,401,402,403; of course, the actual train tickets you're looking at are much more complicated. In any case, you've extracted just the numbers in such a way that the first number is always the same specific field, the second number is always a different specific field, and so on - you just don't know what each position actually means!

# Start by determining which tickets are completely invalid; these are tickets that contain values which aren't valid for any field. Ignore your ticket for now.

# For example, suppose you have the following notes:

# class: 1-3 or 5-7
# row: 6-11 or 33-44
# seat: 13-40 or 45-50

# your ticket:
# 7,1,14

# nearby tickets:
# 7,3,47
# 40,4,50
# 55,2,20
# 38,6,12
# It doesn't matter which position corresponds to which field; you can identify invalid nearby tickets by considering only whether tickets contain values that are not valid for any field. In this example, the values on the first nearby ticket are all valid for at least one field. This is not true of the other three nearby tickets: the values 4, 55, and 12 are are not valid for any field. Adding together all of the invalid values produces your ticket scanning error rate: 4 + 55 + 12 = 71.

# Consider the validity of the nearby tickets you scanned. What is your ticket scanning error rate?

data = open("input.txt").readlines()
clean_data = data[:]

tickets = list()
set_range = set()
total = 0

for line in data:
    if "ticket" in line:
        continue
    elif ":" in line:
        name, ranges = line.split(": ")
        a, b = ranges.split(" or ")
        x1, y1 = [int(z) for z in a.split("-")]
        x2, y2 = [int(z) for z in b.split("-")]
        set_range |= set(range(x1, y1 + 1)).union(set(range(x2, y2 + 1)))
    elif "," in line:
        invalid = False
        ticket = [int(l) for l in line.split(",")]
        for field in ticket:
            if field not in set_range:
                total += field
                invalid = True
        if invalid:
            clean_data.remove(line)

print("Part 1: ", total)

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

new_range = {}

for line in clean_data:
    if ":" in line:
        name, ranges = line.split(": ")
        a, b = ranges.split(" or ")
        x1, y1 = [int(z) for z in a.split("-")]
        x2, y2 = [int(z) for z in b.split("-")]
        new_range[name] = [[x1, y1], [x2, y2]]
    else:
        break

possibilities = []

for i in range(0, len(new_range.keys())):
    possibilities.append(new_range.keys()[:])

for line in clean_data:
    if "," in line:
        ticket = [int(l) for l in line.split(",")]
        for field in range(0, len(ticket)):
            temp = possibilities[field][:]
            for p in possibilities[field]:
                bounds = new_range[p]
                if bounds[0][1] < ticket[field] < bounds[1][0] or ticket[field] < bounds[0][0] or ticket[field] > bounds[1][1]:
                    temp.remove(p)
            possibilities[field] = temp
    else:
        continue

fin = False
i = 0
while not fin:
    if len(possibilities[i]) == 1:
        for p in range(0, len(possibilities)):
            if p != i and possibilities[i][0] in possibilities[p]:
                possibilities[p].remove(possibilities[i][0])
    i += 1
    i = i % len(possibilities)
    fin = True
    for p in possibilities:
        if len(p) != 1:
            fin = False

print(possibilities)

myticket = [137,149,139,127,83,61,89,53,73,67,131,113,109,101,71,59,103,97,107,79]
ans = 1
for p in range(0, len(possibilities)):
    if "departure " in possibilities[p][0]:
        ans *= myticket[p]

print(ans)
