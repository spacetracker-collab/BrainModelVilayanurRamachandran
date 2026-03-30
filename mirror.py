
import torch
import torch.nn as nn
import torch.nn.functional as F

class MirrorNeuronSystem(nn.Module):
    def __init__(self, dim=8):
        super().__init__()
        self.shared = nn.Linear(dim, dim)

    def forward(self, action, observation):
        a = self.shared(action)
        o = self.shared(observation)
        return F.cosine_similarity(a, o, dim=-1)
