"""
Matthew Sabo
Network
Copywrite 2018
"""

import random

class Network(object):
    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        init_biases(sizes)
        init_weights(sizes)

    def init_biases(self, sizes):
        return