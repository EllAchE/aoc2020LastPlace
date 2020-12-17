# ######### PROBLEM
# --- Day 17: Conway Cubes ---
# As your flight slowly drifts through the sky, the Elves at the Mythical Information Bureau at the North Pole contact you. They'd like some help debugging a malfunctioning experimental energy source aboard one of their super-secret imaging satellites.
#
# The experimental energy source is based on cutting-edge technology: a set of Conway Cubes contained in a pocket dimension! When you hear it's having problems, you can't help but agree to take a look.
#
# The pocket dimension contains an infinite 3-dimensional grid. At every integer 3-dimensional coordinate (x,y,z), there exists a single cube which is either active or inactive.
#
# In the initial state of the pocket dimension, almost all cubes start inactive. The only exception to this is a small flat region of cubes (your puzzle input); the cubes in this region start in the specified active (#) or inactive (.) state.
#
# The energy source then proceeds to boot up by executing six cycles.
#
# Each cube only ever considers its neighbors: any of the 26 other cubes where any of their coordinates differ by at most 1. For example, given the cube at x=1,y=2,z=3, its neighbors include the cube at x=2,y=2,z=2, the cube at x=0,y=2,z=3, and so on.
#
# During a cycle, all cubes simultaneously change their state according to the following rules:
#
# If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise, the cube becomes inactive.
# If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.
# The engineers responsible for this experimental energy source would like you to simulate the pocket dimension and determine what the configuration of cubes should be at the end of the six-cycle boot process.
#
# For example, consider the following initial state:
#
# .#.
# ..#
# ###
# Even though the pocket dimension is 3-dimensional, this initial state represents a small 2-dimensional slice of it. (In particular, this initial state defines a 3x3x1 region of the 3-dimensional space.)
#
# Simulating a few cycles from this initial state produces the following configurations, where the result of each cycle is shown layer-by-layer at each given z coordinate:
#
# After the full six-cycle boot process completes, 112 cubes are left in the active state.
#
# Starting with your given initial configuration, simulate six cycles. How many cubes are left in the active state after the sixth cycle?

###INPUT###
# ...#...#
# ..##.#.#
# ###..#..
# ........
# ...##.#.
# .#.####.
# ...####.
# ..##...#
# Define Top Left as 0,0,0. Top right would be 8,0,0. Bottom right is 8,8,0.

class Cube:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.active = False

    def set_Active(self, state):
        self.active = state

cube_list = list()
i = -7
j = -7
k = -7
while i < 15:
    j = -7
    while j < 15:
        k = -7
        while k < 7:
            cube_list.append(Cube(i, j, k))
            k += 1
        j += 1
    i += 1

cube_list.sort(key=lambda a: a.z)
cube_list.sort(key=lambda a: a.y)
cube_list.sort(key=lambda a: a.x)

data = open("input.txt").readlines()
initial_active_list = list()

xval = 0
for line in data:
    yval = 0
    while(yval < 7)
        if (line[yval] == '#'):
            initial_active_list.append([xval, yval, 0])
        else:
            pass



print cube_list


