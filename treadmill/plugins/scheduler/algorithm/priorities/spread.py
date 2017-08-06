import logging
import sys

import numpy

from treadmill.plugins.scheduler import priorities

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
_LOGGER = logging.getLogger(__name__)


class Spread(priorities.PriorityConfig):
    def map(self, app, node):
        if numpy.array_equal(node.free_capacity, node.init_capacity):
            _LOGGER.debug("The node is free.")
            return priorities.ServerWithPriority(1, node)
        else:
            return priorities.ServerWithPriority(100000, node)

    def reduce(self, app, nodes, result):
        pass


def spread(weight):
    return Spread(weight)
