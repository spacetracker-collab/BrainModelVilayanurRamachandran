
# Ramachandran Brain GNN

This project implements a neuroscience-inspired model based on Vilayanur Ramachandran’s ideas:

- Mirror neurons
- Phantom limb representation
- Mirror therapy (left-right inversion)
- Cortical remapping (face-hand interaction)
- Graph Neural Network with cortical topology

## Features
- True graph structure of brain regions
- Temporal dynamics
- Plasticity (remapping)
- Visualization

## Brain Regions (Graph Nodes)
0: Left Hand
1: Right Hand
2: Face
3: Arm
4: Visual Cortex
5: Motor Cortex

Edges represent cortical adjacency.

## Install

pip install torch matplotlib networkx

## Run Locally

python main.py

## Run in Google Colab

```python
!pip install torch matplotlib networkx
!unzip ramachandran_gnn.zip
%cd ramachandran_gnn
!python main.py
```
