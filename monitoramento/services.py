import math
import requests

def processar_manutencao_preditiva(dados_sensor):
    temp_ar_k = dados_sensor['temp_ar_k']
    temp_proc_k = dados_sensor['temp_processo_k']
    rpm = dados_sensor['rotacao_rpm']
    torque = dados_sensor['torque_nm']
    desgaste = dados_sensor['desgaste_ferramenta_min']

    potencia_w = (torque * 2 * math.pi * rpm) / 60
    potencia_kw = round(potencia_w / 1000, 2)

    delta_t = round(temp_proc_k - temp_ar_k, 2)
    
    temp_ar_c = round(temp_ar_k - 273.15, 2)
    temp_proc_c = round(temp_proc_k - 273.15, 2)

    status_matematico = "Operação Normal"
    alertas_detalhados = []

    if delta_t > 10:
        status_matematico = "Crítico: Falha na Dissipação Térmica"
        alertas_detalhados.append("Diferencial de temperatura acima do limite normativo.")
    
    if potencia_kw > 10.0:
        status_matematico = "Alerta: Sobrecarga Elétrica"
        alertas_detalhados.append("Potência calculada acima do limite nominal de operação.")

    url_ia = "http://127.0.0.1:8001/predict"
    
    payload = {
        "temp_ar": temp_ar_k,
        "temp_processo": temp_proc_k,
        "rpm": rpm,
        "torque": torque,
        "desgaste": desgaste
    }

    try:
        response = requests.post(url_ia, json=payload, timeout=5)
        response.raise_for_status()
        resultado_ia = response.json()
    except Exception as e:
        resultado_ia = {
            "falha_prevista": False,
            "risco": 0.0,
            "mensagem": f"Serviço de IA Indisponível: {str(e)}"
        }

    return {
        "potencia_kw": potencia_kw,
        "delta_temp": delta_t,
        "temp_ar_c": temp_ar_c,
        "temp_proc_c": temp_proc_c,
        "status_matematico": status_matematico,
        "alertas_matematicos": alertas_detalhados,
        
        "ia_falha_prevista": resultado_ia.get('falha_prevista'),
        "ia_risco_porcentagem": resultado_ia.get('risco'),
        "ia_mensagem": resultado_ia.get('mensagem'),
        
        "critico": (status_matematico != "Operação Normal") or resultado_ia.get('falha_prevista', False)
    }