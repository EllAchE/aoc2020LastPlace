# --- Day 23: Crab queue ---
# The small crab challenges you to a game! The crab is going to mix up some queue, and you have to predict where they'll end up.

# The queue will be arranged in a circle and labeled clockwise (your puzzle input). For example, if your labeling were 32415, there would be five queue in the circle; going clockwise around the circle from the first cup, the queue would be labeled 3, 2, 4, 1, 5, and then back to 3 again.

# Before the crab starts, it will designate the first cup in your list as the current cup. The crab is then going to do 100 moves.

# Each move, the crab does the following actions:

# The crab picks up the three queue that are immediately clockwise of the current cup. They are removed from the circle; cup spacing is adjusted as necessary to maintain the circle.
# The crab selects a destination cup: the cup with a label equal to the current cup's label minus one. If this would select one of the queue that was just picked up, the crab will keep subtracting one until it finds a cup that wasn't just picked up. If at any point in this process the value goes below the lowest value on any cup's label, it wraps around to the highest value on any cup's label instead.
# The crab places the queue it just picked up so that they are immediately clockwise of the destination cup. They keep the same order as when they were picked up.
# The crab selects a new current cup: the cup which is immediately clockwise of the current cup.
# For example, suppose your cup labeling were 389125467. If the crab were to do merely 10 moves, the following changes would occur:

# -- move 1 --
# queue: (3) 8  9  1  2  5  4  6  7 
# pick up: 8, 9, 1
# destination: 2

# -- move 2 --
# queue:  3 (2) 8  9  1  5  4  6  7 
# pick up: 8, 9, 1
# destination: 7

# -- move 3 --
# queue:  3  2 (5) 4  6  7  8  9  1 
# pick up: 4, 6, 7
# destination: 3

# -- move 4 --
# queue:  7  2  5 (8) 9  1  3  4  6 
# pick up: 9, 1, 3
# destination: 7

# -- move 5 --
# queue:  3  2  5  8 (4) 6  7  9  1 
# pick up: 6, 7, 9
# destination: 3

# -- move 6 --
# queue:  9  2  5  8  4 (1) 3  6  7 
# pick up: 3, 6, 7
# destination: 9

# -- move 7 --
# queue:  7  2  5  8  4  1 (9) 3  6 
# pick up: 3, 6, 7
# destination: 8

# -- move 8 --
# queue:  8  3  6  7  4  1  9 (2) 5 
# pick up: 5, 8, 3
# destination: 1

# -- move 9 --
# queue:  7  4  1  5  8  3  9  2 (6)
# pick up: 7, 4, 1
# destination: 5

# -- move 10 --
# queue: (5) 7  4  1  8  3  9  2  6 
# pick up: 7, 4, 1
# destination: 3

# -- final --
# queue:  5 (8) 3  7  4  1  9  2  6 
# In the above example, the queue' values are the labels as they appear moving clockwise around the circle; the current cup is marked with ( ).

# After the crab is done, what order will the queue be in? Starting after the cup labeled 1, collect the other queue' labels clockwise into a single string with no extra characters; each number except 1 should appear exactly once. In the above example, after 10 moves, the queue clockwise from 1 are labeled 9, 2, 6, 5, and so on, producing 92658374. If the crab were to complete all 100 moves, the order after cup 1 would be 67384529.

# Using your labeling, simulate 100 moves. What are the labels on the queue after cup 1?

# Your puzzle input is 362981754.
from collections import deque

data = [int(i) for i in "362981754"]

queue = deque(data)

for _ in range(100):
    cup = queue[0]
    dest = queue[0] - 1
    if dest < 1:
        dest += 9
    queue.rotate(-1)

    values = (queue.popleft(), queue.popleft(), queue.popleft())

    while dest in values:
        dest = dest - 1 if dest > 1 else dest + 8

    while queue[0] != dest:
        queue.rotate(-1)
    queue.rotate(-1)

    queue.append(values[0])
    queue.append(values[1])
    queue.append(values[2])

    while queue[0] != cup:
        queue.rotate(-1)
    queue.rotate(-1)

while queue[0] != 1:
    queue.rotate(-1)
queue.popleft()

ans = ''.join([str(i) for i in queue])

print("Part 1:", ans)


# --- Part Two ---
# Due to what you can only assume is a mistranslation (you're not exactly fluent in Crab), you are quite surprised when the crab starts arranging many cups in a circle on your raft - one million (1000000) in total.

# Your labeling is still correct for the first few cups; after that, the remaining cups are just numbered in an increasing fashion starting from the number after the highest number in your list and proceeding one by one until one million is reached. (For example, if your labeling were 54321, the cups would be numbered 5, 4, 3, 2, 1, and then start counting up from 6 until one million is reached.) In this way, every number from one through one million is used exactly once.

# After discovering where you made the mistake in translating Crab Numbers, you realize the small crab isn't going to do merely 100 moves; the crab is going to do ten million (10000000) moves!

# The crab is going to hide your stars - one each - under the two cups that will end up immediately clockwise of cup 1. You can have them if you predict what the labels on those cups will be when the crab is finished.

# In the above example (389125467), this would be 934001 and then 159792; multiplying these together produces 149245887792.

# Determine which two cups will end up immediately clockwise of cup 1. What do you get if you multiply their labels together?



ONE_MILLON = 1000000
TEN_MILLON = 10000000

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

nodes = {}
prev = None
for i in data:
    node = Node(i)
    nodes[i] = node
    if prev is not None:
        prev.right = node
        node.left = prev
    prev = node

for i in range(len(data)+1, ONE_MILLON+1):
    node = Node(i)
    nodes[i] = node
    if prev is not None:
        prev.right = node
        node.left = prev
    prev = node

pointer = nodes[data[0]]
prev.right = pointer
pointer.left = prev
for i in range(TEN_MILLON):
    cup = pointer.val

    c1 = pointer.right
    c2 = c1.right
    c3 = c2.right

    pointer.right, pointer.right.left = c3.right, pointer

    dest = cup - 1 or ONE_MILLON
    while dest in (c1.val, c2.val, c3.val):
        dest = dest - 1 or ONE_MILLON

    dest_node = nodes[dest]

    c3.right, c3.right.left = dest_node.right, c3
    dest_node.right, c1.left = c1, dest_node

    pointer = pointer.right

while pointer.val != 1:
    pointer = pointer.right
ans =pointer.right.val * pointer.right.right.val

print("Part 2:", ans)



