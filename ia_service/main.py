from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

model = joblib.load('modelo_manutencao.pkl')

class DadosSensor(BaseModel):
    temp_ar: float
    temp_processo: float
    rpm: float
    torque: float
    desgaste: int

@app.post("/predict")
def predict(dados: DadosSensor):
    delta_t = dados.temp_processo - dados.temp_ar
    relacao = dados.rpm / (delta_t + 1)
    input_data = np.array([[
        dados.temp_ar, 
        dados.temp_processo, 
        dados.rpm, 
        dados.torque, 
        dados.desgaste,
        relacao
    ]])
    
    predicao = model.predict(input_data)[0]
    probabilidade = model.predict_proba(input_data)[0][1]
    return {
        "falha_prevista": bool(predicao),
        "risco": round(float(probabilidade) * 100, 2),
        "mensagem": "Alerta de Falha Iminente!" if predicao else "Sistema Estável"
    }