import numpy as np
import joblib

# Load trained model
model = joblib.load('Trained_4_degree_Polynomial_Regressor.pkl')

# Normalization (min-max) functions
def normalize_linear(value, vmin, vmax):
    return (value - vmin) / (vmax - vmin)

# Input values [Replace x_val (%), Tabs_val (μ), Nabs_val (cm^{-3}), and Netl_val (cm^{-3}) with desired values]
x_val = 77.5
Tabs_val = 0.5375
Nabs_val = 3e14
Netl_val = 1.75e17

# Normalize input using min-max scaling based on feature bounds
x_norm = normalize_linear(x_val, 60, 75)
Nabs_norm = normalize_linear(Nabs_val, 1e14, 9e14)
Tabs_norm = normalize_linear(Tabs_val, 0.25, 0.5)
Netl_norm = normalize_linear(Netl_val, 6e16, 1.8e17)

# Combine into input array
X_input_norm = np.array([[x_norm, Nabs_norm, Tabs_norm, Netl_norm]])

# Predict (output is still normalized)
y_pred_scaled = model.predict(X_input_norm)

# Given: eta (η) min-max and degradation (Δ) min-max
eta_min, eta_max = 10.2210864, 16.7010432
deg_min, deg_max = 0.033853813, 1.551581245

# Inverse min-max scaling to recover original target values
eta_pred = y_pred_scaled[0, 0] * (eta_max - eta_min) + eta_min
deg_pred = y_pred_scaled[0, 1] * (deg_max - deg_min) + deg_min

# Show result
print(f"Predicted η: {eta_pred:.2f}%")
print(f"Predicted Δ: {deg_pred:.2f}%")