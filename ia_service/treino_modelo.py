import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import joblib
import os

def train():
    csv_path = os.path.join('..', 'data', 'predictive_maintenance.csv')
    df = pd.read_csv(csv_path)
    df['delta_t'] = df['Process temperature [K]'] - df['Air temperature [K]']
    df['relacao'] = df['Rotational speed [rpm]'] / (df['delta_t'] + 1)

    features = [
        'Air temperature [K]', 
        'Process temperature [K]', 
        'Rotational speed [rpm]', 
        'Torque [Nm]', 
        'Tool wear [min]',
        'relacao'
    ]
    X = df[features]
    y = df['Machine failure']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    joblib.dump(model, 'modelo_manutencao.pkl')
    print("Modelo treinado e salvo como 'modelo_manutencao.pkl'")
    importances = model.feature_importances_
    feat_importances = pd.Series(importances, index=features)
    feat_importances.nlargest(10).plot(kind='barh', color='#0ea5e9')
    plt.title('Padrões Identificados: Importância dos Sensores')
    plt.xlabel('Nível de Influência na Falha')
    plt.savefig('padroes_ia.png')

if __name__ == "__main__":
    train()