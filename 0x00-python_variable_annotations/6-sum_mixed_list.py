#!/usr/bin/env python3
'''RET sum as a float.
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''takes int+ float[] returns their sum as a float.
    '''
    return float(sum(mxd_lst))
