import pickle
import numpy as np

def predict(preprocessed_input):
    property_type = preprocessed_input[0]
    property_values = preprocessed_input[1]
    print(property_type)
    if(property_type == "HOUSE"):
        with open("model/house/house_scaler.pkl", "rb") as scaler_file:
            scaler = pickle.load(scaler_file)
        
        with open("model/house/house_polyfeatures.pkl", "rb") as poly_features_file:
            poly_features = pickle.load(poly_features_file)
        
        with open("model/house/house_model.pkl", "rb") as model_file:
            model = pickle.load(model_file)

    elif(property_type == "APARTMENT"):
        with open("model/apartment/apartment_scaler.pkl", "rb") as scaler_file:
            scaler = pickle.load(scaler_file)
        
        with open("model/apartment/apartment_polyfeatures.pkl", "rb") as poly_features_file:
            poly_features = pickle.load(poly_features_file)
        
        with open("model/apartment/apartment_model.pkl", "rb") as model_file:
            model = pickle.load(model_file)
    
    array_input = np.array([property_values])
    X_scaled_input = scaler.transform(array_input)
    price_prediction = model.predict(poly_features.fit_transform(X_scaled_input))
    return round(float(price_prediction), 2)