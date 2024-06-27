import joblib

def load_model():
    model = joblib.load('your_trained_model.pkl')  # Load your trained model
    return model
