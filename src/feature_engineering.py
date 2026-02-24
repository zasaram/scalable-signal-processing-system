import numpy as np
from scipy import signal

def extract_features(sig, fs=100):
    features = []

    # Time domain
    features.append(np.mean(sig))
    features.append(np.std(sig))
    features.append(np.max(sig))
    features.append(np.min(sig))

    # Frequency domain
    freqs, psd = signal.welch(sig, fs)
    features.append(np.mean(psd))
    features.append(np.max(psd))

    return np.array(features)

def build_feature_matrix(signals):
    return np.array([extract_features(s) for s in signals])