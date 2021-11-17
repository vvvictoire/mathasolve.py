"""Main mathasolve.py module"""

import operator
from mathasolve.print_management import print_rpn

from mathasolve.tree_management import set_of_combinations, set_of_permutations, rpn

PLUS = operator.add
MINUS = operator.sub
TIMES = operator.mul
DIV = operator.truediv

numbers = [1,2,3,4,5]
operands = [PLUS, MINUS, TIMES, DIV]
target = 24

# Generate all permutations possibles for the 5 numbers
permutation_numbers = set_of_permutations(numbers)

# Generate all combinations possibles for the 4 operands
combination_operands = set_of_combinations(operands)

for number in permutation_numbers:
    for operand in combination_operands:
        try:
            RESULT = rpn(number, operand)
            if RESULT == target:

                print(print_rpn(number, operand))
        except Exception:
            pass
