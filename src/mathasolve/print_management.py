"""Printing management"""
import operator

from typing import List

def str_operator(_operator: callable) -> str:
    """Returns a string describing the operation"""
    switch = {
        operator.add : "+",
        operator.sub : "-",
        operator.mul : "×",
        operator.truediv : "÷"
    }
    return switch.get(_operator)

def str_operators(operators: List[callable]) -> str:
    """Return a string describing a series of operations"""
    _str_operators = []
    for _operator in operators:
        _str_operators.append(str_operator(_operator))
    return str(list(_str_operators))

def list_str_operators(operators):
    """Return a string describing a series of operations"""
    _str_operators = []
    for _operator in operators:
        _str_operators.append(str_operator(_operator))
    return list(_str_operators)

def print_rpn(numbers, operators):
    return "" + str(numbers) + " " + str_operators(operators)
