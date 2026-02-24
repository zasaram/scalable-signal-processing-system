from config import DATA_SIZE
from src.data_generator import create_dataset
from src.feature_engineering import build_feature_matrix
from src.model import train_model
from src.utils import ensure_dirs

def main():
    print("Initializing scalable signal processing system...")
    ensure_dirs()

    print("Generating dataset...")
    signals, labels = create_dataset(DATA_SIZE)

    print("Extracting features...")
    X = build_feature_matrix(signals)

    print("Training model...")
    acc = train_model(X, labels)

    print(f"Training completed. Accuracy: {acc:.3f}")

if __name__ == "__main__":
    main()