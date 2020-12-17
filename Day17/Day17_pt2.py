data = open("input.txt").readlines()
# data = ['.#.\n', '..#\n', '###\n']
# top left 0,0,0, bottom right 3,3,0 or sth
x = 0
y = 0
z = 0
w = 0
current = {}
for line in data:
    # cut trailing \n
    line = line.strip('\n')
    for cube in line:
        if cube == '#':
            current[x, y, z, w] = cube
        x += 1
    x = 0
    y += 1

cycles = 6
neighbor = [[1, 0, 0, 0], [0, 1, 0, 0], [1, 1, 0, 0], [-1, 0, 0, 0], [0, -1, 0, 0], [-1, -1, 0, 0], [1, -1, 0, 0], [-1, 1, 0, 0],
            [0, 0, 1, 0], [1, 0, 1, 0], [0, 1, 1, 0], [1, 1, 1, 0], [-1, 0, 1, 0], [0, -1, 1, 0], [-1, -1, 1, 0], [1, -1, 1, 0], [-1, 1, 1, 0],
            [0, 0, -1, 0], [1, 0, -1, 0], [0, 1, -1, 0], [1, 1, -1, 0], [-1, 0, -1, 0], [0, -1, -1, 0], [-1, -1, -1, 0], [1, -1, -1, 0],
            [-1, 1, -1, 0],
            [1, 0, 0, 1], [0, 1, 0, 1], [1, 1, 0, 1], [-1, 0, 0, 1], [0, -1, 0, 1], [-1, -1, 0, 1], [1, -1, 0, 1], [-1, 1, 0, 1],
            [0, 0, 1, 1], [1, 0, 1, 1], [0, 1, 1, 1], [1, 1, 1, 1], [-1, 0, 1, 1], [0, -1, 1, 1], [-1, -1, 1, 1], [1, -1, 1, 1], [-1, 1, 1, 1],
            [0, 0, -1, 1], [1, 0, -1, 1], [0, 1, -1, 1], [1, 1, -1, 1], [-1, 0, -1, 1], [0, -1, -1, 1], [-1, -1, -1, 1], [1, -1, -1, 1],
            [-1, 1, -1, 1],
            [1, 0, 0, -1], [0, 1, 0, -1], [1, 1, 0, -1], [-1, 0, 0, -1], [0, -1, 0, -1], [-1, -1, 0, -1], [1, -1, 0, -1], [-1, 1, 0, -1],
            [0, 0, 1, -1], [1, 0, 1, -1], [0, 1, 1, -1], [1, 1, 1, -1], [-1, 0, 1, -1], [0, -1, 1, -1], [-1, -1, 1, -1], [1, -1, 1, -1], [-1, 1, 1, -1],
            [0, 0, -1, -1], [1, 0, -1, -1], [0, 1, -1, -1], [1, 1, -1, -1], [-1, 0, -1, -1], [0, -1, -1, -1], [-1, -1, -1, -1], [1, -1, -1, -1],
            [-1, 1, -1, -1],
            [0, 0, 0, -1], [0, 0, 0, 1]
            ]
for i in range(0, cycles):
    nxt = current.keys()
    for key in current.keys():
        for n in neighbor:
            neighbor_key = (key[0] + n[0], key[1] + n[1], key[2] + n[2], key[3] + n[3])
            if neighbor_key not in nxt:
                nxt.append(neighbor_key)

    active = []
    for key in nxt:
        # print(key)
        active_neighbors = 0
        for n in neighbor:
            neighbor_key = (key[0] + n[0], key[1] + n[1], key[2] + n[2], key[3] + n[3])
            if neighbor_key in current.keys():
                active_neighbors += 1
        # active
        if key in current.keys() and current[key] == '#':
            if active_neighbors == 3 or active_neighbors == 2:
                active.append(key)
        # inactive
        else:
            if active_neighbors == 3:
                active.append(key)
    current = {}
    for key in active:
        current[key] = '#'

    print(i)

print(len(current.keys()))
