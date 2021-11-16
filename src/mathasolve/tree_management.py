"""Builds a tree"""
from itertools import combinations_with_replacement, permutations, product
from typing import Callable, Iterable, Tuple

def set_of_permutations(_list: Iterable) -> list[Tuple]:
    """Return all permutations of a list"""
    _set = list(permutations(_list))
    # Get rid of duplicates via set-hack
    _set = list(set(_set))
    return _set

def set_of_combinations(_list: Iterable) -> list[Tuple]:
    """Return all combinations of a list"""
    _set = list(product(_list, repeat=len(_list)))
    # Get rid of duplicates via set-hack
    _set = list(set(_set))
    return _set

def rpn(operands: list, operators: list[Callable]):
    """Does a series of operations on the operands"""
    if not len(operands) == len(operators) + 1:
        raise IndexError
    while operators:
        first_operand = operands.pop(0)
        operands[0] = operators.pop(0)(first_operand, operands[0])
        if operands[0] < 0 or not isinstance(operands[0], int):
            raise ValueError
    return operands[0]

def inject_list(injected, injector):
    """Weave together 2 lists: (a[0], b[0], a[1], b[1]…) injected MUST be
    1 longer than injector"""
    if not len(injected) == len(injector) + 1:
        raise IndexError
    weave = []
    for index in range(len(injector)):
        weave.append(injected[index])
        weave.append(injector[index])
    weave.append(injected[-1])
    return tuple(weave)
