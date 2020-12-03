# You start on the open square (.) in the top-left corner and need to reach the bottom (below the bottom-most row on
# your map).
#
# The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational numbers);
# start by counting all the trees you would encounter for the slope right 3, down 1:
#
# From your starting position at the top-left, check the position that is right 3 and down 1. Then, check the
# position that is right 3 and down 1 from there, and so on until you go past the bottom of the map.
#
# The locations you'd check in the above example are marked here with O where there was an open square and X where
# there was a tree:
#
# ..##.........##.........##.........##.........##.........##.......  --->
# #..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
# .#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
# ..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
# .#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
# ..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
# .#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
# .#........#.#........X.#........#.#........#.#........#.#........#
# #.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
# #...##....##...##....##...#X....##...##....##...##....##...##....#
# .#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
# In this example, traversing the map using this slope would cause you to encounter 7 trees.
#
# Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you
# encounter?


data = open("input.txt", "r")
# copy the data to a list
lst = [d for d in data]

def genericSlope(horizontal, vertical):
    col = 0
    trees = 0
    vertLoop = vertical
    for line in lst:
        if(vertLoop == 1):
            vertLoop = vertical
        else:
            vertLoop-=1
            continue
        line = line[0:-1]
        if line[col] == "#":
            trees += 1
        #print(line, col, trees)
        col = (col + horizontal) % len(line)
    print(trees)
    return trees

print(genericSlope(1,1) * genericSlope(3,1) * genericSlope(5,1) * genericSlope(7,1) * genericSlope(1,2))