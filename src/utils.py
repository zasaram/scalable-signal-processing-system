import os

def ensure_dirs():
    if not os.path.exists("models"):
        os.makedirs("models")