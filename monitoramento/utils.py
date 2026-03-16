import numpy as np
import random

def gerar_leitura_sensor(tipo='None', condicao='None'):
    if not tipo or tipo == 'None':
        tipo = random.choice(['L', 'M', 'H'])
    
    if not condicao or condicao == 'None':
        condicao = random.choice(['normal', 'estresse_termico', 'falha_ferramenta'])
        
    temp_ar = round(random.uniform(295.0, 301.0), 2)
    
    if condicao == 'normal':
        delta_t = random.uniform(8.0, 11.0)
        torque = random.uniform(35.0, 45.0)
        desgaste = random.randint(0, 150)
    elif condicao == 'estresse_termico':
        delta_t = random.uniform(13.0, 18.0)
        torque = random.uniform(40.0, 55.0)
        desgaste = random.randint(100, 200)
    else:
        delta_t = random.uniform(9.0, 12.0)
        torque = random.uniform(55.0, 70.0)
        desgaste = random.randint(200, 250)

    temp_processo = round(temp_ar + delta_t, 2)
    rotacao = round(random.uniform(1350, 1550), 0)
    
    return {
        'tipo': tipo,
        'temp_ar_k': temp_ar,
        'temp_processo_k': temp_processo,
        'rotacao_rpm': rotacao,
        'torque_nm': torque,
        'desgaste_ferramenta_min': desgaste
    }