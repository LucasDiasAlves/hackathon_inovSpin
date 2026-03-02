import requests
from django.conf import settings

def processar_manutencao_preditiva(dados_sensor):
    temp_ar_c = dados_sensor['temp_ar_k'] - 273.15
    temp_proc_c = dados_sensor['temp_processo_k'] - 273.15
    delta_temp = temp_proc_c - temp_ar_c

    status_matematico = "Operação Normal"
    if delta_temp > 10:
        status_matematico = "Alerta: Dissipação Térmica Deficiente (Crítico)"
    if dados_sensor['torque_nm'] > 60:
        status_matematico = "Alerta: Sobrecarga de Torque"

    url_ia = "http://127.0.0.1:8001/predict"
    
    payload = {
        "temp_ar": dados_sensor['temp_ar_k'],
        "temp_processo": dados_sensor['temp_processo_k'],
        "rpm": dados_sensor['rotacao_rpm'],
        "torque": dados_sensor['torque_nm'],
        "desgaste": dados_sensor['desgaste_ferramenta_min']
    }

    try:
        response = requests.post(url_ia, json=payload, timeout=5)
        response.raise_for_status()
        resultado_ia = response.json()
    except requests.exceptions.RequestException as e:
        resultado_ia = {
            "falha_prevista": False,
            "risco": 0.0,
            "mensagem": f"Erro ao contatar serviço de IA: {str(e)}"
        }

    return {
        "temp_ar_c": round(temp_ar_c, 2),
        "temp_proc_c": round(temp_proc_c, 2),
        "delta_temp": round(delta_temp, 2),
        "status_matematico": status_matematico,
        "ia_falha_prevista": resultado_ia['falha_prevista'],
        "ia_risco_porcentagem": resultado_ia['risco'],
        "ia_mensagem": resultado_ia['mensagem'],
        "critico": (status_matematico != "Operação Normal") or resultado_ia['falha_prevista']
    }