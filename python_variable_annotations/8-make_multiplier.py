#!/usr/bin/env python3
"""
Complex types - functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    type-annotated function make_multiplier that
    takes a float multiplieras argument and returns a function
    that multiplies a float by multiplier.
    """
    def multiply_function(number: float) -> float:
        return number * multiplier
    return multiply_function
