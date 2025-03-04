import joblib

def load_model():
    """
    Carga el modelo de Machine Learning entrenado.
    
    Retorna:
        model: Modelo cargado desde el archivo .pkl
    """
    model = joblib.load("data/model.pkl")
    return model
