
import torch

class Plasticity:
    def __init__(self, adj):
        self.adj = adj

    def remap(self, source, target, strength=0.2):
        self.adj[target, source] += strength
        self.adj[source, target] += strength
