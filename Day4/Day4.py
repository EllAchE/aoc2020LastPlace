# --- Day 4: Passport Processing ---
# You arrive at the airport only to realize that you grabbed your North Pole Credentials instead of your passport. While these documents are extremely similar, North Pole Credentials aren't issued by a country and therefore aren't actually valid documentation for travel in most of the world.

# It seems like you're not the only one having problems, though; a very long line has formed for the automatic passport scanners, and the delay could upset your travel itinerary.

# Due to some questionable network security, you realize you might be able to solve both of these problems at the same time.

# The automatic passport scanners are slow because they're having trouble detecting which passports have all required fields. The expected fields are as follows:

# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)
# Passport data is validated in batch files (your puzzle input). Each passport is represented as a sequence of key:value pairs separated by spaces or newlines. Passports are separated by blank lines.

# Here is an example batch file containing four passports:

# ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
# byr:1937 iyr:2017 cid:147 hgt:183cm

# iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
# hcl:#cfa07d byr:1929

# hcl:#ae17e1 iyr:2013
# eyr:2024
# ecl:brn pid:760753108 byr:1931
# hgt:179cm

# hcl:#cfa07d eyr:2025 pid:166559648
# iyr:2011 ecl:brn hgt:59in
# The first passport is valid - all eight fields are present. The second passport is invalid - it is missing hgt (the Height field).

# The third passport is interesting; the only missing field is cid, so it looks like data from North Pole Credentials, not a passport at all! Surely, nobody would mind if you made the system temporarily ignore missing cid fields. Treat this "passport" as valid.

# The fourth passport is missing two fields, cid and byr. Missing cid is fine, but missing any other field is not, so this passport is invalid.

# According to the above rules, your improved system would report 2 valid passports.

# Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch file, how many passports are valid?


### Part 1 ###

data = open("input.txt", "r")
# copy the data to a list
lst = [d for d in data]

result = []
passport = set()
for line in lst:
    pairs = line.strip()
    if not pairs:
        result.append(passport)
        passport = set()
    else:
        for pair in pairs.split(" "):
            key = pair.split(":")[0]
            if key != 'cid':
                passport.add(key)

valid = 0
for port in result:
    if len(port) == 7:
        valid += 1


print("Part 1: ", valid)



### Part 2 ###

def validated(key, value):
    if key == 'byr':
        return 1920 <= int(value) <= 2002
    elif key == 'iyr':
        return 2010 <= int(value) <= 2020
    elif key == 'eyr':
        return 2020 <= int(value) <= 2030
    elif key == 'hgt':
        if value.endswith('cm'):
            return 150 <= int(value.strip('cm')) <= 193
        elif value.endswith('in'):
            return 59 <= int(value.strip('in')) <= 76
    elif key == 'hcl':
        if value.startswith('#'):
            value = value.lstrip('#')
            return len(''.join([c for c in value if c in '0123456789abcdef'])) == 6
    elif key == 'ecl':
        return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    elif key == 'pid':
        return len(value) == 9
    return False

data = open("input.txt", "r")
# copy the data to a list
lst = [d for d in data]

result = []
passport = set()
for line in lst:
    pairs = line.strip()
    if not pairs:
        result.append(passport)
        passport = set()
    else:
        for pair in pairs.split(" "):
            key = pair.split(":")[0]
            value = pair.split(":")[1]
            if key != 'cid' and validated(key, value):
                passport.add(key)

valid = 0
for port in result:
    if len(port) == 7:
        valid += 1


print("Part 2: ", valid)
