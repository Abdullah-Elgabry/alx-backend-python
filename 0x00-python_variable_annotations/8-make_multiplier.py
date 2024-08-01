#!/usr/bin/env python3
'''multiplier functions
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''this function makes multiplier ()
    '''
    return lambda x: x * multiplier
