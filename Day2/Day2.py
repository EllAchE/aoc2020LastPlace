# Suppose you have the following list:
#
# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc
#
# Each line gives the password policy and then the password. The password policy indicates the lowest and highest
# number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password
# must contain a at least 1 time and at most 3 times.
#
# In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b,
# but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits
# of their respective policies.
#
# How many passwords are valid according to their policies?
# --- Part Two ---
# While it appears you validated the passwords correctly, they don't seem to be what
# the Official Toboggan Corporate Authentication System is expecting.
#
# password policy rules from his old job at the sled rental place down the street! The Official Toboggan Corporate
# Policy actually works a little differently.
#
# Each policy actually describes two positions in the password, where 1 means the first character,
# 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!)
# Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.
#
# Given the same example list from above:
#
# 1-3 a: abcde is valid: position 1 contains a and position 3 does not.
# 1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
# 2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
# How many passwords are valid according to the new interpretation of the policies?

import re

data = open("input.txt", "r")
# copy the data to a list
lst = [d for d in data]

def process(value):
    value = re.split("[:, ,-]", value[0:-1])
    character = value[2]
    password = value[4]
    firstIndex = password[int(value[0])-1]
    secondIndex = password[int(value[1])-1]
    #print(firstIndex, secondIndex, character, password, value[0], value[1])

    if(firstIndex == character):
        if(secondIndex == character):
            #print(0)
            return 0
        #print(1)
        return 1
    if(secondIndex == character):
        #print(1)
        return 1
    #print(0)
    return 0

count = 0
for line in lst:
    count += process(line)
print(count)

##Part 1##
# import re
#
# data = open("input.txt", "r")
# # copy the data to a list
# lst = [d for d in data]
#
#
# def process(value):
#     value = re.split("[:, ,-]", value[0:-1])
#     minimum = int(value[0])
#     maximum = int(value[1])
#     character = value[2]
#     password = value[4]
#     # print(minimum, maximum, character, password)
#
#     matchcount = 0
#     for c in password:
#         if c == character:
#             matchcount += 1
#     # print(character, matchcount, password)
#     if minimum <= matchcount <= maximum:
#         return 1
#     return 0
#
#
# count = 0
# for line in lst:
#     count += process(line)
# print(count)
