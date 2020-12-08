# The boot code is represented as a text file with one instruction per line of text. Each instruction consists of an operation (acc, jmp, or nop) and an argument (a signed number like +4 or -20).
#
# acc increases or decreases a single global value called the accumulator by the value given in the argument. For example, acc +7 would increase the accumulator by 7. The accumulator starts at 0. After an acc instruction, the instruction immediately below it is executed next.
# jmp jumps to a new instruction relative to itself. The next instruction to execute is found using the argument as an offset from the jmp instruction; for example, jmp +2 would skip the next instruction, jmp +1 would continue to the instruction immediately below it, and jmp -20 would cause the instruction 20 lines above to be executed next.
# nop stands for No OPeration - it does nothing. The instruction immediately below it is executed next.
# For example, consider the following program:
#
# nop +0
# acc +1
# jmp +4
# acc +3
# jmp -3
# acc -99
# acc +1
# jmp -4
# acc +6
# These instructions are visited in this order:
#
# nop +0  | 1
# acc +1  | 2, 8(!)
# jmp +4  | 3
# acc +3  | 6
# jmp -3  | 7
# acc -99 |
# acc +1  | 4
# jmp -4  | 5
# acc +6  |
# First, the nop +0 does nothing. Then, the accumulator is increased from 0 to 1 (acc +1) and jmp +4 sets the next instruction to the other acc +1 near the bottom. After it increases the accumulator from 1 to 2, jmp -4 executes, setting the next instruction to the only acc +3. It sets the accumulator to 5, and jmp -3 causes the program to continue back at the first acc +1.
#
# This is an infinite loop: with this sequence of jumps, the program will run forever. The moment the program tries to run any instruction a second time, you know it will never terminate.
#
# Immediately before the program would run an instruction a second time, the value in the accumulator is 5.
#
# Run your copy of the boot code. Immediately before any instruction is executed a second time, what value is in the accumulator?
#

# --- Part Two ---
# After some careful analysis, you believe that exactly one instruction is corrupted.
#
# Somewhere in the program, either a jmp is supposed to be a nop, or a nop is supposed to be a jmp. (No acc instructions were harmed in the corruption of this boot code.)
#
# The program is supposed to terminate by attempting to execute an instruction immediately after the last instruction in the file. By changing exactly one jmp or nop, you can repair the boot code and make it terminate correctly.
#
# For example, consider the same program from above:
#
# nop +0
# acc +1
# jmp +4
# acc +3
# jmp -3
# acc -99
# acc +1
# jmp -4
# acc +6
# If you change the first instruction from nop +0 to jmp +0, it would create a single-instruction infinite loop, never leaving that instruction. If you change almost any of the jmp instructions, the program will still eventually find another jmp instruction and loop forever.
#
# However, if you change the second-to-last instruction (from jmp -4 to nop -4), the program terminates! The instructions are visited in this order:
#
# nop +0  | 1
# acc +1  | 2
# jmp +4  | 3
# acc +3  |
# jmp -3  |
# acc -99 |
# acc +1  | 4
# nop -4  | 5
# acc +6  | 6
# After the last instruction (acc +6), the program terminates by attempting to run the instruction below the last instruction in the file. With this change, after the program terminates, the accumulator contains the value 8 (acc +1, acc +1, acc +6).
#
# Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp). What is the value of the accumulator after the program terminates?

data = open("input.txt", "r")
# copy the data to a list
lst = data.read().split("\n")

def run(list):
    loop = True
    accum = 0
    line = 0
    visited = [0]
    # jmpnop = []
    while loop:
        cmd = lst[line].split(' ')[0]
        val = int(lst[line].split(' ')[1])
        if cmd == "nop":
            # jmpnop.append(line)
            line += 1
        elif cmd == "acc":
            line += 1
            accum += val
        elif cmd == "jmp":
            # jmpnop.append(line)
            line += val

        if line in visited or line >= len(lst):
            loop = False
            # print("Infinite", accum, visited)
            # print(jmpnop)
            return False
        else:
            visited.append(line)

        if line == len(lst) -1:
            loop = False
            print(accum)
            return True


jmpnop = [4, 306, 309, 155, 156, 30, 514, 515, 41, 203, 19, 331, 74, 337, 579, 231, 609, 59, 51, 209, 375, 377, 593, 62,
          621, 622, 434, 367, 518, 520, 196, 186, 250, 251, 85, 455, 457, 459, 91, 161, 242, 396, 132, 566, 548, 549,
          551, 399, 400, 420, 421, 422, 569, 599, 601, 443, 429, 430, 224, 225, 556, 151, 268, 364, 315, 382, 541, 11,
          324, 34, 44, 47, 235, 236, 465, 466, 468, 611, 507, 277, 278, 103, 272, 406, 66, 67, 139, 141, 534, 447, 448,
          450, 257]


def swap(lst, idx):
    if idx > 0:
        lst[jmpnop[idx - 1]] = flipjmpnop(lst[jmpnop[idx - 1]])
    lst[jmpnop[idx]] = flipjmpnop(lst[jmpnop[idx]])
    return lst


def flipjmpnop(line):
    cmd = line.split(' ')[0]
    if cmd == "jmp":
        line = "nop " + line.split(' ')[1]
    elif cmd == "nop":
        line = "jmp " + line.split(' ')[1]
    return line
    # print(line)


loop = False
i = 0
while not loop:
    loop = run(lst)
    lst = swap(lst, i)
    i += 1
