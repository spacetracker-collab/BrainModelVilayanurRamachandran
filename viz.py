
import matplotlib.pyplot as plt

def plot(history):
    data = history.detach().numpy()
    plt.plot(data)
    plt.title("Cortical Dynamics")
    plt.xlabel("Time")
    plt.ylabel("Activation")
    plt.show()
