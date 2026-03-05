from django.shortcuts import render
from django.http import HttpResponse
from .models import AtivoEletrico
from .services import processar_manutencao_preditiva
from django.db.models import Avg, F, FloatField

def monitoramento(request):
    
    todos_ids = AtivoEletrico.objects.values_list('product_id', flat=True).distinct()
    id_buscado = request.GET.get('filtro_id', 'M14860').strip()
    registro = AtivoEletrico.objects.filter(product_id=id_buscado).first()
    
    if not registro:
        registro = AtivoEletrico.objects.first()

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
        
    media_categoria_db = AtivoEletrico.objects.filter(tipo=registro.tipo).aggregate(
        media_dt=Avg(F('temp_processo_k') - F('temp_ar_k'), output_field=FloatField())
    )['media_dt'] or 5.0
    
    media_falha_db = AtivoEletrico.objects.filter(
        tipo=registro.tipo, 
        predicao_ia_risco__gt=50 
    ).aggregate(
        media_dt=Avg(F('temp_processo_k') - F('temp_ar_k'), output_field=FloatField())
    )['media_dt']
    
    if not media_falha_db:
        limites_seguranca = {'L': 8.5, 'M': 10.5, 'H': 13.0}
        media_falha_db = limites_seguranca.get(registro.tipo, 10.0)
    
    grafico_dados = {
        'atual': float(analise.get('delta_temp', 0)),
        'media_cat': float(media_categoria_db),
        'media_falha': float(media_falha_db)
        }
    
    ia_risco = analise.get('ia_risco_porcentagem', 0)
    ia_mensagem = analise.get('ia_mensagem', "Sistema Estável")
    status_mat = analise.get('status_matematico', "Operação Normal")

# 2. Lógica de Hierarquia de Alerta (O mais grave vence)
    if ia_risco > 80:
        analise['critico'] = True
    # Forçamos a mensagem da IA a aparecer com destaque
        status_exibicao = f"CRÍTICO: {ia_mensagem}"
        cor_alerta = "danger" 
    elif ia_risco > 40 or "Alerta" in status_mat:
        analise['critico'] = False # Não é crítico total ainda
        status_exibicao = "ATENÇÃO: " + (ia_mensagem if ia_risco > 40 else status_mat)
        cor_alerta = "warning"
    else:
        status_exibicao = "ESTÁVEL: Operação Nominal"
        cor_alerta = "info"
    
    contexto = {
        'registro': registro,
        'analise': analise,
        'todos_ids': todos_ids,
        'alerta_amarelo': ("Alerta" in analise['status_matematico']) and analise['ia_risco_porcentagem'] < 20,
        'grafico_dados': grafico_dados,
        'status_personalizado': status_exibicao,
        'cor_alerta': cor_alerta,
        }
    
    return render(request, 'monitoramento/index.html', contexto)
    