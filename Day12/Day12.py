# --- Day 12: Rain Risk ---
# Your ferry made decent progress toward the island, but the storm came in faster than anyone expected. The ferry needs to take evasive actions!
#
# Unfortunately, the ship's navigation computer seems to be malfunctioning; rather than giving a route directly to safety, it produced extremely circuitous instructions. When the captain uses the PA system to ask if anyone can help, you quickly volunteer.
#
# The navigation instructions (your puzzle input) consists of a sequence of single-character actions paired with integer input values. After staring at them for a few minutes, you work out what they probably mean:
#
# Action N means to move north by the given value.
# Action S means to move south by the given value.
# Action E means to move east by the given value.
# Action W means to move west by the given value.
# Action L means to turn left the given number of degrees.
# Action R means to turn right the given number of degrees.
# Action F means to move forward by the given value in the direction the ship is currently facing.
# The ship starts by facing east. Only the L and R actions change the direction the ship is facing. (That is, if the ship is facing east and the next instruction is N10, the ship would move north 10 units, but would still move east if the following action were F.)
#
# For example:
#
# F10
# N3
# F7
# R90
# F11
# These instructions would be handled as follows:
#
# F10 would move the ship 10 units east (because the ship starts by facing east) to east 10, north 0.
# N3 would move the ship 3 units north to east 10, north 3.
# F7 would move the ship another 7 units east (because the ship is still facing east) to east 17, north 3.
# R90 would cause the ship to turn right by 90 degrees and face south; it remains at east 17, north 3.
# F11 would move the ship 11 units south to east 17, south 8.
# At the end of these instructions, the ship's Manhattan distance (sum of the absolute values of its east/west position and its north/south position) from its starting position is 17 + 8 = 25.
#
# Figure out where the navigation instructions lead. What is the Manhattan distance between that location and the ship's starting position?
#

data = open("input.txt", "r")
# copy the data to a list
lst = data.read().split("\n")[:-1]

# lst = ["F10", "N3", "F7", "L270", "L90", "R90", "F11"]

dir = []
amt = []

for i in range(0, len(lst)):
    dir.append(lst[i][0])
    amt.append(int(lst[i][1:]))


def move(direction, amount, orientation, coordinates):
    orient_list = ['N', 'E', 'S', 'W']
    if direction == 'N':
        coordinates[0] += amount
    elif direction == 'E':
        coordinates[1] += amount
    elif direction == 'S':
        coordinates[0] -= amount
    elif direction == 'W':
        coordinates[1] -= amount
    elif direction == 'L':
        orientation = (orientation - (amount / 90)) % 4
    elif direction == 'R':
        orientation = (orientation + (amount / 90)) % 4
    elif direction == 'F':
        move(orient_list[orientation], amount, orientation, coordinates)
    return orientation, coordinates


orient = 1
coord = [0, 0]
for i in range(0, len(lst)):
    orient, coord = move(dir[i], amt[i], orient, coord)
    # print(dir[i], amt[i], orient, coord)
print("Part 1: ", abs(coord[0]) + abs(coord[1]))

# Your puzzle answer was 1687.
#
# --- Part Two ---
# Before you can give the destination to the captain, you realize that the actual action meanings were printed on the back of the instructions the whole time.
#
# Almost all of the actions indicate how to move a waypoint which is relative to the ship's position:
#
# Action N means to move the waypoint north by the given value.
# Action S means to move the waypoint south by the given value.
# Action E means to move the waypoint east by the given value.
# Action W means to move the waypoint west by the given value.
# Action L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
# Action R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.
# Action F means to move forward to the waypoint a number of times equal to the given value.
# The waypoint starts 10 units east and 1 unit north relative to the ship. The waypoint is relative to the ship; that is, if the ship moves, the waypoint moves with it.
#
# For example, using the same instructions as above:
#
# F10 moves the ship to the waypoint 10 times (a total of 100 units east and 10 units north), leaving the ship at east 100, north 10. The waypoint stays 10 units east and 1 unit north of the ship.
# N3 moves the waypoint 3 units north to 10 units east and 4 units north of the ship. The ship remains at east 100, north 10.
# F7 moves the ship to the waypoint 7 times (a total of 70 units east and 28 units north), leaving the ship at east 170, north 38. The waypoint stays 10 units east and 4 units north of the ship.
# R90 rotates the waypoint around the ship clockwise 90 degrees, moving it to 4 units east and 10 units south of the ship. The ship remains at east 170, north 38.
# F11 moves the ship to the waypoint 11 times (a total of 44 units east and 110 units south), leaving the ship at east 214, south 72. The waypoint stays 4 units east and 10 units south of the ship.
# After these operations, the ship's Manhattan distance from its starting position is 214 + 72 = 286.
#
# Figure out where the navigation instructions actually lead. What is the Manhattan distance between that location and the ship's starting position?

#Screwed up the first time on part 2 because I forgot to account for multiple rotations when you had 270 vs. 90 degrees.
# Fixed and got it 2nd time though

data = open("input.txt", "r")
lst = data.read().split("\n")
print lst

eWaypointOffset = 10
nWaypointOffset = 1
eBoatDistance = 0
nBoatDistance = 0

for move in lst:
    print move
    if(move[0] == 'E'):
        eWaypointOffset += int(move[1:])
    elif(move[0] == 'W'):
        eWaypointOffset -= int(move[1:])
    elif(move[0] == 'N'):
        nWaypointOffset += int(move[1:])
    elif(move[0] == 'S'):
        nWaypointOffset -= int(move[1:])
    elif(move[0] == 'L'):
        numTimes = int(move[1:])
        while (numTimes > 1):
            numTimes -= 90
            temp = eWaypointOffset;
            eWaypointOffset = -1 * nWaypointOffset
            nWaypointOffset = temp
    elif(move[0] == 'R'):
        numTimes = int(move[1:])
        while(numTimes > 1):
            numTimes -= 90
            temp = eWaypointOffset;
            eWaypointOffset = nWaypointOffset
            nWaypointOffset = temp * -1
    elif(move[0] == 'F'):
        eBoatDistance += (int(move[1:]) * eWaypointOffset)
        nBoatDistance += (int(move[1:]) * nWaypointOffset)
    else:
        print "error"
    print ("eboatdis ", eBoatDistance)
    print ("nboatdis ", nBoatDistance)
    print ("nwaypoint ", nWaypointOffset)
    print ("ewaypoint ", eWaypointOffset)

print abs(nBoatDistance) + abs(eBoatDistance)
