# --- Day 18: Operation Order ---
# As you look out the window and notice a heavily-forested continent slowly appear over the horizon, you are interrupted by the child sitting next to you. They're curious if you could help them with their math homework.
#
# Unfortunately, it seems like this "math" follows different rules than you remember.
#
# The homework (your puzzle input) consists of a series of expressions that consist of addition (+), multiplication (*), and parentheses ((...)). Just like normal math, parentheses indicate that the expression inside must be evaluated before it can be used by the surrounding expression. Addition still finds the sum of the numbers on both sides of the operator, and multiplication still finds the product.
#
# However, the rules of operator precedence have changed. Rather than evaluating multiplication before addition, the operators have the same precedence, and are evaluated left-to-right regardless of the order in which they appear.
#
# For example, the steps to evaluate the expression 1 + 2 * 3 + 4 * 5 + 6 are as follows:
#
# 1 + 2 * 3 + 4 * 5 + 6
#   3   * 3 + 4 * 5 + 6
#       9   + 4 * 5 + 6
#          13   * 5 + 6
#              65   + 6
#                  71
# Parentheses can override this order; for example, here is what happens if parentheses are added to form 1 + (2 * 3) + (4 * (5 + 6)):
#
# 1 + (2 * 3) + (4 * (5 + 6))
# 1 +    6    + (4 * (5 + 6))
#      7      + (4 * (5 + 6))
#      7      + (4 *   11   )
#      7      +     44
#             51
# Here are a few more examples:
#
# 2 * 3 + (4 * 5) becomes 26.
# 5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 437.
# 5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 12240.
# ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 13632.
# Before you can help with the homework, you need to understand it yourself. Evaluate the expression on each line of the homework; what is the sum of the resulting values?

import re

data = open("input.txt", "r")
# copy the data to a list
lst = data.read().split("\n")[:-1]

def eval_left_to_right(expression):
    expression = convert_lr_expression_to_list(expression)
    while len(expression) > 2:
        first_val = int(expression[0])
        second_val = int(expression[2])
        if re.match('\+', expression[1]):
            new_val = first_val + second_val
        elif re.match('\*', expression[1]):
            new_val = first_val * second_val
        else:
            new_val = 'error'
        expression.pop(0)
        expression.pop(0)
        expression.pop(0)
        expression.insert(0,new_val)
    if len(expression) > 1:
        if(expression[0] != '*' and expression[0] != '+'):
            expression = expression[0] + " " + expression[1] + " "
        else:
            expression = " " + expression[1] + " " + expression[0]
    return expression

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

def no_whitespace_list(list_in):
    i = 0
    iterate = len(list_in)
    while i < iterate:
        try:
            list_in.remove(' ')
            i += 1
        except:
            break
    return list_in

def convert_lr_expression_to_list(expression):
    expression_list = re.split(' ', expression)
    expression_list = no_empty_list(expression_list)
    expression_list = no_whitespace_list(expression_list)
    return expression_list

def convert_to_list(line):
    i = 0
    paranthesis_list = list()
    for char in line:
        if (char == '('):
            if (i != 0):
                paranthesis_list.append(line[:i])
                paranthesis_list.append('(')
                line = line[i + 1:]
            else:
                paranthesis_list.append('(')
                line = line[i + 1:]
            i = -1
        elif (char == ')'):
            if (re.match('[^\)]*', line)):
                if (i != 0):
                    paranthesis_list.append(line[:i])
                    paranthesis_list.append(')')
                    line = line[i + 1:]
                else:
                    paranthesis_list.append(')')
                    line = line[i + 1:]
            else:
                break
            i = -1
        i += 1
    if len(line) > 0:
        paranthesis_list.append(line)
    return paranthesis_list

def eval_paranthesis(paranthesis_list):
    try:
        paranthesis_list.index('(')
    except:
        return paranthesis_list

    while paranthesis_list.index('(') != -1:
        right_brace_index = -1
        left_brace_index = paranthesis_list.index('(')
        i = left_brace_index + 1

        while right_brace_index == -1:
            if(paranthesis_list[i] == '('):
                left_brace_index = i
            if(paranthesis_list[i] == ')'):
                right_brace_index = i
            i += 1

        eval = ""
        popit = False
        for elem in paranthesis_list[(left_brace_index + 1):right_brace_index]:
            eval += elem
            if popit:
                paranthesis_list.pop(left_brace_index+1)
            popit = True
        eval = eval_left_to_right(eval)

        paranthesis_list[left_brace_index + 1] = str(eval[0])
        paranthesis_list.pop(left_brace_index)
        paranthesis_list.pop(left_brace_index+1)

        if '(' not in paranthesis_list:
            break
    return paranthesis_list

count = 1
total = 0
for line in lst:
    paranthesis_list = convert_to_list(line)
    no_paranthesis_list = eval_paranthesis(paranthesis_list)

    final_ex = ""
    for val in no_paranthesis_list:
        final_ex += str(val)

    result = eval_left_to_right(final_ex)
    print (count, result[0])

    count += 1
    total = total + result[0]
print total
