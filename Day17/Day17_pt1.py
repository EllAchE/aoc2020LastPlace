data = open("input.txt").readlines()
# data = ['.#.\n', '..#\n', '###\n']
# top left 0,0,0, bottom right 3,3,0 or sth
x = 0
y = 0
z = 0
current = {}
for line in data:
    # cut trailing \n
    line = line.strip('\n')
    for cube in line:
        current[x, y, z] = cube
        x += 1
    x = 0
    y += 1

cycles = 6
neighbor = [[1, 0, 0], [0, 1, 0], [1, 1, 0], [-1, 0, 0], [0, -1, 0], [-1, -1, 0], [1, -1, 0], [-1, 1, 0],
            [0, 0, 1], [1, 0, 1], [0, 1, 1], [1, 1, 1], [-1, 0, 1], [0, -1, 1], [-1, -1, 1], [1, -1, 1], [-1, 1, 1],
            [0, 0, -1], [1, 0, -1], [0, 1, -1], [1, 1, -1], [-1, 0, -1], [0, -1, -1], [-1, -1, -1], [1, -1, -1],
            [-1, 1, -1], ]
for i in range(0, cycles):
    nxt = dict(current)
    for key in current.keys():
        for n in neighbor:
            neighbor_key = (key[0] + n[0], key[1] + n[1], key[2] + n[2])
            if neighbor_key not in nxt.keys():
                nxt[neighbor_key] = '.'

    for key in nxt.keys():
        # print(key)
        active_neighbors = 0
        for n in neighbor:
            neighbor_key = (key[0] + n[0], key[1] + n[1], key[2] + n[2])
            if neighbor_key in current.keys():
                if current[neighbor_key] == '#':
                    active_neighbors += 1
        # active
        if key in current.keys() and current[key] == '#':
            if active_neighbors == 3 or active_neighbors == 2:
                nxt[key] = '#'
            else:
                nxt[key] = '.'
        # inactive
        else:
            if active_neighbors == 3:
                nxt[key] = '#'
            else:
                nxt[key] = '.'
    current = nxt

# print(current)

active = 0
for key in current.keys():
    if current[key] == '#':
        active += 1
print(active)