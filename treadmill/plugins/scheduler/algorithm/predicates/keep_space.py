from ...predicates import PredicateConfig
import numpy as np

import operator


def _all(oper, left, right):
    """Short circuit all for ndarray."""
    return all(oper(ai, bi) for ai, bi in zip(left, right))

def _all_lt(left, right):
    """Short circuit all lt for ndarray."""
    return _all(operator.lt, left, right)


def _all_le(left, right):
    """Short circuit all le for ndarray."""
    return _all(operator.le, left, right)


def _all_gt(left, right):
    """Short circuit all gt for ndarray."""
    return _all(operator.gt, left, right)

def _all_ge(left, right):
    """Short circuit all ge for ndarray."""
    return _all(operator.ge, left, right)


class KeepSpace(PredicateConfig):
    def predicate(self, app, node):
        if app.demand[0] / node.init_capacity[0] > 0.5 and app.demand[0] / node.init_capacity[0] < 0.8:
            return False
        return True


def keep_space():
    return KeepSpace()
