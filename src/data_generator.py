import numpy as np
from config import FS

def generate_signal(length=5000):
    t = np.linspace(0, length/FS, length)
    freq = np.random.choice([1, 3, 5, 7])
    signal = np.sin(2 * np.pi * freq * t)
    noise = np.random.normal(0, 0.5, length)
    return signal + noise, freq

def create_dataset(n_samples):
    X = []
    y = []
    for _ in range(n_samples):
        s, label = generate_signal()
        X.append(s)
        y.append(label)
    return X, y