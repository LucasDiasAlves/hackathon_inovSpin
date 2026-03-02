from django.shortcuts import render
from django.http import HttpResponse
from .models import AtivoEletrico
from .services import processar_manutencao_preditiva

def monitoramento(request):
    registro = AtivoEletrico.objects.filter(product_id="M14860").first()
    
    if not registro:
        return render(request, 'dashboard.html', {'erro': 'Registro M14860 não encontrado.'})

    dados_sensor = {
        'temp_ar_k': registro.temp_ar_k,
        'temp_processo_k': registro.temp_processo_k,
        'rotacao_rpm': registro.rotacao_rpm,
        'torque_nm': registro.torque_nm,
        'desgaste_ferramenta_min': registro.desgaste_ferramenta_min,
    }

    analise = processar_manutencao_preditiva(dados_sensor)

    registro.status_matematico = analise['status_matematico']
    registro.predicao_ia_risco = analise['ia_risco_porcentagem']
    registro.save()
    
    contexto = {
        'registro': registro,
        'analise': analise
    }
    return render(request, 'monitoramento/index.html', contexto)
    