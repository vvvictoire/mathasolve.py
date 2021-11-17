"""Testing module"""

import operator

from mathasolve.tree_management import rpn, set_of_combinations, set_of_permutations
from mathasolve.print_management import str_operator, str_operators, print_rpn

# Permutation of 1 element
_list = [1]
_set = set(set_of_permutations(_list))
# Don’t remove the comma. Don’t.
expected = set([(1,)])
assert _set == expected

# Permutations of 2 elements
_list = [1,2]
_set = set(set_of_permutations(_list))
expected = set([(1,2), (2,1)])
assert _set == expected

# Permutations of 2 same elements
_list = [1,1]
_set = set(set_of_permutations(_list))
expected = set([(1,1)])
assert _set == expected

# Permutations of 3 elements
_list = [1,2,3]
_set = set(set_of_permutations(_list))
expected = set([(1,2,3), (1,3,2), (2,1,3), (2,3,1), (3,1,2), (3,2,1)])
assert _set == expected

# Permutations of 3 element with a repeat
_list = [1,1,2]
_set = set(set_of_permutations(_list))
expected = set([(1,2,1), (1,1,2), (2,1,1)])
assert _set == expected

# rpn with 2 elements (1+2)
operands = [1,2]
operators = [operator.add]
RESULT = rpn(operands, operators)
assert RESULT == 3

# rpn with 3 elements (1+2+3)
operands = [1,2,3]
operators = [operator.add, operator.add]
RESULT = rpn(operands, operators)
assert RESULT == 6

# rpn should fail because it’s negative(1-2)
operands = [1,2]
operators = [operator.sub]
try:
    rpn(operands, operators)
except ValueError:
    pass
else:
    assert False

# rpn should fail because it’s not an int (1/2)
operands = [1,2]
operators = [operator.truediv]
try:
    rpn(operands, operators)
except ValueError:
    pass
else:
    assert False

# rpn should fail because of division by 0 (1/0)
operands = [1,0]
operators = [operator.truediv]
try:
    rpn(operands, operators)
except ZeroDivisionError:
    pass
else:
    assert False

# set of combinations with 1 element
_list = [1]
_set = set(set_of_combinations(_list))
# Don’t remove the comma. Don’t
expected = set([(1,)])
assert _set == expected

# set of combinations with 2 elements
_list = [1, 2]
_set = set(set_of_combinations(_list))
# Don’t remove the comma. Don’t
expected = set([(1,1), (1,2), (2,1), (2,2)])
assert _set == expected

# set of combinations with 3 elements
_list = [1, 2, 3]
_set = set(set_of_combinations(_list))
# Don’t remove the comma. Don’t
expected = set([(1,1,1), (1,1,2), (1,1,3), (1,2,1), (1,2,2), (1,2,3),
                (1,3,1), (1,3,2), (1,3,3), (2,1,1), (2,1,2), (2,1,3),
                (2,2,1), (2,2,2), (2,2,3), (2,3,1), (2,3,2), (2,3,3),
                (3,1,1), (3,1,2), (3,1,3), (3,2,1), (3,2,2), (3,2,3),
                (3,3,1), (3,3,2), (3,3,3)])
assert _set == expected

# Print the operators
assert str_operator(operator.add) == "+"
assert str_operator(operator.sub) == "-"
assert str_operator(operator.mul) == "×"
assert str_operator(operator.truediv) == "÷"

PLUS = operator.add
MINUS = operator.sub
TIMES = operator.mul
DIV = operator.truediv

# Print a list of operators
assert str_operators([PLUS, MINUS, TIMES, DIV]) == "['+', '-', '×', '÷']"

# Print a rpn
numbers = [1,2]
operators = [PLUS]
assert print_rpn(numbers, operators) == "[1, 2] ['+']"

# Print a rpn with 2 operations
numbers = [1,2,3]
operators = [PLUS, MINUS]
assert print_rpn(numbers, operators) == "[1, 2, 3] ['+', '-']"

print("All good!")
