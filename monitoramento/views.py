from django.shortcuts import render
from django.http import HttpResponse
from .models import AtivoEletrico
from .services import processar_manutencao_preditiva

def monitoramento(request):
    todos_ids = AtivoEletrico.objects.values_list('product_id', flat=True).distinct()
    
    id_buscado = request.GET.get('filtro_id', 'M14860').strip()
    
    registro = AtivoEletrico.objects.filter(product_id=id_buscado).first()
    
    if not registro:
        registro = AtivoEletrico.objects.first()
        erro_msg = f"Ativo {id.buscado} não encontrado. Mostrando padrão."
    else:
        erro_msg = None


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
    
    exibir_alerta_amarelo = ("Alerta" in analise['status_matematico'] or "Atenção" in analise['status_matematico']) and analise['ia_risco_porcentagem'] < 20    
    
    contexto = {
        'registro': registro,
        'analise': analise,
        'erro_busca': erro_msg,
        'todos_ids': todos_ids,
        'alerta_amarelo': exibir_alerta_amarelo,
    }
    return render(request, 'monitoramento/index.html', contexto)
    