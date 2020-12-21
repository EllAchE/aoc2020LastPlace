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
# To check that you've assembled the image correctly, multiply the IDs of the four corner tiles together. If you do
# this with the assembled tiles from the example above, you get 1951 * 3079 * 2971 * 1171 = 20899048083289.
#
# Assemble the tiles into an image. What do you get if you multiply together the IDs of the four corner tiles?

import re


def reverse_string(string):
    new_str_list = list()
    for char in string:
        new_str_list.append(char)
    new_str_list = new_str_list.reverse()
    new_str = ""
    for char in new_str_list:
        new_str += char
    return new_str


def get_left(image):
    left_list = list()
    for line in image:
        left_list.append(line[0])
    return left_list


def get_right(image):
    left_list = list()
    for line in image:
        left_list.append(line[-1])
    return left_list


def get_bottom(image):
    bottom_list = list()
    for char in image[-1]:
        bottom_list.append(char)
    return bottom_list


def get_top(image):
    bottom_list = list()
    for char in image[0]:
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


def match_bottoms_and_tops(obj_list):
    return None

def match_left_and_right(obj_list):
    return None


class Tile:
    def __init__(self, id, image):
        self.id = id
        self.left_side = get_left(image)
        self.right_side = get_right(image)
        self.bottom_side = get_bottom(image)
        self.top_side = get_top(image)
        self.left_side_flipped = [e for e in self.left_side]
        self.right_side_flipped = [e for e in self.right_side]
        self.bottom_side_flipped = [e for e in self.bottom_side]
        self.top_side_reversed = [e for e in self.top_side]
        self.left_side.reverse()
        self.right_side.reverse()
        self.bottom_side.reverse()
        self.top_side.reverse()
        self.side_match_count = 0

    def add_match(self):
        self.side_match_count += 1


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

obj_lst = list()

for lst in lst_of_lst:
    obj_lst.append(Tile(lst[0], lst[1:]))

print obj_lst

# All that you need to solved this problem now is to find whichever Tile it is that only has matches on 2 sides (I believe,
# this assumes that you don;t have to jigsaw the Tiles to solve the problem

i = 0
lits_len = len(obj_lst)
while i < lits_len - 1:
    temp_r = obj_lst[i].right_side
    temp_r_r = obj_lst[i].right_side_flipped
    temp_l = obj_lst[i].left_side
    temp_l_r = obj_lst[i].left_side_flipped
    temp_t = obj_lst[i].top_side
    temp_t_r = obj_lst[i].top_side_reversed
    temp_b = obj_lst[i].bottom_side
    temp_b_r = obj_lst[i].bottom_side_flipped

    base_lst = [temp_r, temp_l, temp_r_r, temp_l_r, temp_t, temp_b, temp_t_r, temp_b_r]

    for obj in obj_lst[i+1:]:
        comp_lst = [obj.right_side, obj.left_side, obj.top_side, obj.bottom_side]
        for side in comp_lst:
            if side in base_lst:
                obj_lst[i].add_match()
                obj.add_match()
        if obj_lst[i].side_match_count > 3:
            break

    i += 1

for item in obj_lst:
    if item.side_match_count == 2:
        print item.id

print obj_lst


