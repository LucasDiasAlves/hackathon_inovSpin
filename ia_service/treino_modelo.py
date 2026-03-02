import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

def train():
    csv_path = os.path.join('..', 'data', 'predictive_maintenance.csv')
    df = pd.read_csv(csv_path)

    features = [
        'Air temperature [K]', 
        'Process temperature [K]', 
        'Rotational speed [rpm]', 
        'Torque [Nm]', 
        'Tool wear [min]'
    ]
    X = df[features]
    y = df['Machine failure']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    joblib.dump(model, 'modelo_manutencao.pkl')
    print("Modelo treinado e salvo como 'modelo_manutencao.pkl'")

if __name__ == "__main__":
    train()