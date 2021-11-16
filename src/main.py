"""Main mathasolve.py module"""

import operator

from mathasolve.tree_management import inject_list, set_of_permutations

PLUS = operator.add
MINUS = operator.sub
TIMES = operator.mul
DIV = operator.truediv

numbers = [1,2,3]
operands = [PLUS, MINUS, TIMES, DIV]

# Generate all permutations possibles for the 5 numbers
permutation_numbers = set_of_permutations(numbers)

# Generate all permutations possibles for
weave = inject_list(a, b)
print(weave)
