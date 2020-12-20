# --- Day 20: Jurassic Jigsaw ---
# The high-speed train leaves the forest and quickly carries you south. You can even see a desert in the distance!
# Since you have some spare time, you might as well see if there was anything interesting in the image the Mythical
# Information Bureau satellite captured.
#
# After decoding the satellite messages, you discover that the data actually contains many small images created by
# the satellite's camera array. The camera array consists of many cameras; rather than produce a single square image,
# they produce many smaller square image tiles that need to be reassembled back into a single image.
#
# Each camera in the camera array returns a single monochrome image tile with a random unique ID number. The tiles
# (your puzzle input) arrived in a random order.
#
# Worse yet, the camera array appears to be malfunctioning: each image tile has been rotated and flipped to a random
# orientation. Your first task is to reassemble the original image by orienting the tiles so they fit together.
#
# To show how the tiles should be reassembled, each tile's image data includes a border that should line up exactly with
# its adjacent tiles. All tiles have this border, and the border lines up exactly when the tiles are both oriented
# correctly. Tiles at the edge of the image also have this border, but the outermost edges won't line up with any other tiles.
#
# For example, suppose you have the following nine tiles:
#
# Tile 2311:
# ..##.#..#.
# ##..#.....
# #...##..#.
# ####.#...#
# ##.##.###.
# ##...#.###
# .#.#.#..##
# ..#....#..
# ###...#.#.
# ..###..###
#
# Tile 1951:
# #.##...##.
# #.####...#
# .....#..##
# #...######
# .##.#....#
# .###.#####
# ###.##.##.
# .###....#.
# ..#.#..#.#
# #...##.#..
#
# Tile 1171:
# ####...##.
# #..##.#..#
# ##.#..#.#.
# .###.####.
# ..###.####
# .##....##.
# .#...####.
# #.##.####.
# ####..#...
# .....##...
#
# Tile 1427:
# ###.##.#..
# .#..#.##..
# .#.##.#..#
# #.#.#.##.#
# ....#...##
# ...##..##.
# ...#.#####
# .#.####.#.
# ..#..###.#
# ..##.#..#.
#
# Tile 1489:
# ##.#.#....
# ..##...#..
# .##..##...
# ..#...#...
# #####...#.
# #..#.#.#.#
# ...#.#.#..
# ##.#...##.
# ..##.##.##
# ###.##.#..
#
# Tile 2473:
# #....####.
# #..#.##...
# #.##..#...
# ######.#.#
# .#...#.#.#
# .#########
# .###.#..#.
# ########.#
# ##...##.#.
# ..###.#.#.
#
# Tile 2971:
# ..#.#....#
# #...###...
# #.#.###...
# ##.##..#..
# .#####..##
# .#..####.#
# #..#.#..#.
# ..####.###
# ..#.#.###.
# ...#.#.#.#
#
# Tile 2729:
# ...#.#.#.#
# ####.#....
# ..#.#.....
# ....#..#.#
# .##..##.#.
# .#.####...
# ####.#.#..
# ##.####...
# ##..#.##..
# #.##...##.
#
# Tile 3079:
# #.#.#####.
# .#..######
# ..#.......
# ######....
# ####.#..#.
# .#...#.##.
# #.#####.##
# ..#.###...
# ..#.......
# ..#.###...
# By rotating, flipping, and rearranging them, you can find a square arrangement that causes all adjacent borders to line up:
#
# #...##.#.. ..###..### #.#.#####.
# ..#.#..#.# ###...#.#. .#..######
# .###....#. ..#....#.. ..#.......
# ###.##.##. .#.#.#..## ######....
# .###.##### ##...#.### ####.#..#.
# .##.#....# ##.##.###. .#...#.##.
# #...###### ####.#...# #.#####.##
# .....#..## #...##..#. ..#.###...
# #.####...# ##..#..... ..#.......
# #.##...##. ..##.#..#. ..#.###...
#
# #.##...##. ..##.#..#. ..#.###...
# ##..#.##.. ..#..###.# ##.##....#
# ##.####... .#.####.#. ..#.###..#
# ####.#.#.. ...#.##### ###.#..###
# .#.####... ...##..##. .######.##
# .##..##.#. ....#...## #.#.#.#...
# ....#..#.# #.#.#.##.# #.###.###.
# ..#.#..... .#.##.#..# #.###.##..
# ####.#.... .#..#.##.. .######...
# ...#.#.#.# ###.##.#.. .##...####
#
# ...#.#.#.# ###.##.#.. .##...####
# ..#.#.###. ..##.##.## #..#.##..#
# ..####.### ##.#...##. .#.#..#.##
# #..#.#..#. ...#.#.#.. .####.###.
# .#..####.# #..#.#.#.# ####.###..
# .#####..## #####...#. .##....##.
# ##.##..#.. ..#...#... .####...#.
# #.#.###... .##..##... .####.##.#
# #...###... ..##...#.. ...#..####
# ..#.#....# ##.#.#.... ...##.....
# For reference, the IDs of the above tiles are:
#
# 1951    2311    3079
# 2729    1427    2473
# 2971    1489    1171
# To check that you've assembled the image correctly, multiply the IDs of the four corner tiles together. If you do this with the assembled tiles from the example above, you get 1951 * 3079 * 2971 * 1171 = 20899048083289.
#
# Assemble the tiles into an image. What do you get if you multiply together the IDs of the four corner tiles?

def get_left(image):
    lst = image.split()
    left_list = list()
    for char in lst[0]:
        left_list.append(char)
    return left_list


def get_right(image):
    lst = image.split()
    left_list = list()
    for char in lst[-1]:
        left_list.append(char)
    return left_list


def get_bottom(image):
    lst = image.split()
    bottom = lst[-1]
    bottom_list = list()
    for char in bottom:
        bottom_list.append(char)
    return bottom_list


def get_top(image):
    lst = image.split()
    bottom = lst[0]
    bottom_list = list()
    for char in bottom:
        bottom_list.append(char)
    return bottom_list

def no_empty_list(list_in):
    i = 0
    iterate = len(list_in)
    while i < iterate:
        try:
            list_in.remove('')
            i += 1
        except:
            break
    return list_in

def no_newline_list(list_in):
    i = 0
    iterate = len(list_in)
    while i < iterate:
        try:
            list_in.pop(1 + i)
            i += 1
        except:
            break
    return list_in

class tile:
    def __init__(self, id, image):
        self.id = id
        self.left_side = get_left(image)
        self.right_side = get_right(image)
        self.bottom_side = get_bottom(image)
        self.top_side = get_top(image)
        self.left_side_flipped = reversed(self.left_side)
        self.right_side_flipped = reversed(self.right_side)
        self.bottom_side_flipped = reversed(self.bottom_side)
        self.top_side = reversed(self.top_side)


import re
data = open("input.txt", "r").read()
data_str = data
lst = re.split('Tile ', data_str)
lst = no_empty_list(lst)

lst_of_lst = list()

for str in lst:
    str = re.split('(\\n)', str)
    str = no_newline_list(str)
    str = no_empty_list(str)
    lst_of_lst.append(str)
    print str
