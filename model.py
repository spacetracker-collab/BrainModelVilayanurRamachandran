
import torch
import torch.nn as nn
import torch.nn.functional as F

class CorticalGNN(nn.Module):
    def __init__(self, n_nodes=6, dim=8):
        super().__init__()
        self.W = nn.Linear(dim, dim)

    def forward(self, x, adj):
        # graph propagation
        agg = torch.matmul(adj, x)
        return F.relu(self.W(agg))
