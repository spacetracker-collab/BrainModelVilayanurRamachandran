
import torch
from model import CorticalGNN
from mirror import MirrorNeuronSystem
from plasticity import Plasticity
from therapy import mirror_therapy
from viz import plot

# adjacency (cortical topology)
adj = torch.tensor([
 [1,0,1,0,0,0],
 [0,1,1,0,0,0],
 [1,1,1,1,0,0],
 [0,0,1,1,0,0],
 [0,0,0,0,1,1],
 [0,0,0,0,1,1]
], dtype=torch.float32)

gnn = CorticalGNN()
mirror = MirrorNeuronSystem()
plastic = Plasticity(adj)

state = torch.randn(6,8)
history = []

for t in range(50):
    # simulate phantom (remove left hand input)
    state[0] *= 0.9

    # mirror therapy
    left, right = mirror_therapy(state[0], state[1], enable=True)
    state[0], state[1] = left, right

    # cortical remapping (face -> hand)
    plastic.remap(2,0,0.01)

    # GNN propagation
    state = gnn(state, adj)

    history.append(state.mean(dim=1))

history = torch.stack(history)
plot(history)
