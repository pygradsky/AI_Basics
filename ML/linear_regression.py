import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.datasets import fetch_california_housing


# Задание 1. Примеры и синтетические данные

# Линейная регрессия поможет предсказать:
# 1) Погоду на завтра (температуру)
# 2) Численность людей в мире
# 3) Цену на жилье

X_synth = np.linspace(0, 10, 50).reshape(-1, 1)
y_synth = 3 * X_synth + 5 + np.random.randn(50, 1) * 2

X_train, X_test, y_train, y_test = train_test_split(X_synth, y_synth, test_size=0.33, random_state=42)
model_synth = LinearRegression()
model_synth.fit(X_train, y_train)


# Задание 2. Анализ одного признака (California Housing)

housing = fetch_california_housing()

X_single = housing.data[:, [0]] 
y_single = housing.target

X_train_s, X_test_s, y_train_s, y_test_s = train_test_split(X_single, y_single, test_size=0.33, random_state=42)

model_single = LinearRegression()
model_single.fit(X_train_s, y_train_s)
y_pred_s = model_single.predict(X_test_s)

print("--- Задание 2: Одномерная регрессия (California) ---")
print(f"MAE: {mean_absolute_error(y_test_s, y_pred_s):.4f}")
print(f"MSE: {mean_squared_error(y_test_s, y_pred_s):.4f}")
print(f"R^2 Score: {r2_score(y_test_s, y_pred_s):.4f}\n")


# Задание 3. Множественная регрессия (2-3 признака)

data_multi = fetch_california_housing(as_frame=True)
X_multi = data_multi.frame[['MedInc', 'HouseAge', 'AveRooms']]
y_multi = data_multi.target

X_train_m, X_test_m, y_train_m, y_test_m = train_test_split(X_multi, y_multi, test_size=0.2, random_state=42)

model_multi = LinearRegression()
model_multi.fit(X_train_m, y_train_m)
y_pred_m = model_multi.predict(X_test_m)

print("--- Задание 3: Множественная регрессия ---")
print(f"Coef: {model_multi.coef_}")
print(f"R^2 Score: {r2_score(y_test_m, y_pred_m):.4f}\n")


# Задание 4. Модель для выбранного датасета (EV vs ICE)

df_ev = pd.read_csv('EV_vs_ICE_Vehicle_Specs_2015_2026.csv')
df_ev = df_ev.drop(columns=['Model'], errors='ignore')
df_ev = pd.get_dummies(df_ev)

X_ev = df_ev.drop(columns=['CO2_Emissions_g_per_mile'])
y_ev = df_ev['CO2_Emissions_g_per_mile']

X_train_ev, X_test_ev, y_train_ev, y_test_ev = train_test_split(X_ev, y_ev, test_size=0.2, random_state=42)
model_ev = LinearRegression()
model_ev.fit(X_train_ev, y_train_ev)
print("--- Задание 4: EV vs ICE ---")
print(f"R^2 Score: {model_ev.score(X_test_ev, y_test_ev):.4f}\n")


# Задание 5. Метод наименьших квадратов (МНК) вручную

print("--- Задание 5: Ручной МНК (одномерный) ---")
X_5 = np.array([1, 2, 3, 4, 5])
y_5 = np.array([2.1, 3.9, 6.2, 8.1, 10.2])

n = len(X_5)
w1 = (n * np.sum(X_5 * y_5) - np.sum(X_5) * np.sum(y_5)) / (n * np.sum(X_5**2) - (np.sum(X_5))**2)
w0 = np.mean(y_5) - w1 * np.mean(X_5)

print(f"Ручной расчет: w0 = {w0:.4f}, w1 = {w1:.4f}")
model_sk5 = LinearRegression().fit(X_5.reshape(-1, 1), y_5)
print(f"Sklearn расчет: w0 = {model_sk5.intercept_:.4f}, w1 = {model_sk5.coef_[0]:.4f}\n")


# Задание 6. МНК для многомерного случая 

print("--- Задание 6: Нормальное уравнение (многомерный) ---")
X_6 = data_multi.frame[['MedInc', 'HouseAge']].values
y_6 = data_multi.target.values


X_b = np.c_[np.ones((len(X_6), 1)), X_6] 
# Формула: w = (X^T * X)^-1 * X^T * y
w_normal = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y_6)

print(f"Веса (Нормальное уравнение): {w_normal}")
model_sk6 = LinearRegression().fit(X_6, y_6)
print(f"Веса (Sklearn): {model_sk6.intercept_}, {model_sk6.coef_}\n")


# Задание 7

print("--- Задание 7: Градиентный спуск ---")
def gradient_descent(X, y, lr=0.1, epochs=1000):
    m, n = X.shape
    w = np.zeros(n)
    for _ in range(epochs):
        prediction = X.dot(w)
        gradient = (2/m) * X.T.dot(prediction - y)
        w = w - lr * gradient
    return w

# Масштабирование данных для стабильности GD
X_6_scaled = (X_6 - X_6.mean(axis=0)) / X_6.std(axis=0)
X_6_scaled_b = np.c_[np.ones((len(X_6_scaled), 1)), X_6_scaled]

w_gd = gradient_descent(X_6_scaled_b, y_6)
print(f"Коэффициенты после GD: {w_gd}")
