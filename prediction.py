import numpy as np

def predict_price(model, input_data):
    """
    Realiza la predicción del precio de la casa.
    
    Parámetros:
        model: Modelo de Machine Learning cargado con joblib.
        input_data: Lista o array con los valores de entrada.

    Retorna:
        float: Predicción del precio.
    """
    input_array = np.array([input_data])  # Convertir a formato compatible
    prediction = model.predict(input_array)
    return prediction[0]  # Retorna el valor predicho