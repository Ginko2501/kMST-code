import math
import numpy as np
from Graph import Graph

class Tree(Graph):
    def __init__(self, mat):
        super().__init__(mat)
        self.cut = []