from django.shortcuts import render
from .models import AtivoEletrico
from .services import processar_manutencao_preditiva
from django.db.models import Avg, F, FloatField
from .utils import gerar_leitura_sensor

def monitoramento(request):
    todos_ids = AtivoEletrico.objects.values_list('product_id', flat=True).distinct()
    id_buscado = request.GET.get('filtro_id', 'M14860').strip()
    
    if id_buscado == "GERAR_DADO":
        dados_brutos = gerar_leitura_sensor(tipo=None, condicao=None)
        registro = AtivoEletrico(
            product_id="SIMULADO_01",
            tipo=dados_brutos['tipo'],
            temp_ar_k=dados_brutos['temp_ar_k'],
            temp_processo_k=dados_brutos['temp_processo_k'],
            rotacao_rpm=dados_brutos['rotacao_rpm'],
            torque_nm=dados_brutos['torque_nm'],
            desgaste_ferramenta_min=dados_brutos['desgaste_ferramenta_min']
        )
        is_simulado = True
    else:
        registro = AtivoEletrico.objects.filter(product_id=id_buscado).first()
        if not registro:
            registro = AtivoEletrico.objects.first()
        is_simulado = False

    dados_sensor = {
        'temp_ar_k': registro.temp_ar_k,
        'temp_processo_k': registro.temp_processo_k,
        'rotacao_rpm': registro.rotacao_rpm,
        'torque_nm': registro.torque_nm,
        'desgaste_ferramenta_min': registro.desgaste_ferramenta_min,
    }
    analise = processar_manutencao_preditiva(dados_sensor)

    if not is_simulado and registro:
        registro.status_matematico = analise['status_matematico']
        registro.predicao_ia_risco = analise['ia_risco_porcentagem']
        registro.save()

    if 'historico_simulacao' not in request.session:
        request.session['historico_simulacao'] = []

    if id_buscado == "GERAR_DADO":
        novo_ponto = {
            'delta_t': float(analise.get('delta_temp', 0)),
            'risco': float(analise.get('ia_risco_porcentagem', 0))
        }
        historico = request.session['historico_simulacao']
        historico.append(novo_ponto)
        if len(historico) > 10: historico.pop(0)
        request.session['historico_simulacao'] = historico
        request.session.modified = True

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

    ia_risco = analise.get('ia_risco_porcentagem', 0)
    ia_mensagem = analise.get('ia_mensagem', "Sistema Estável")
    status_mat = analise.get('status_matematico', "Operação Normal")

    if ia_risco > 80:
        cor_alerta = "danger"
        status_exibicao = f"CRÍTICO: {ia_mensagem}"
    elif ia_risco > 40 or "Alerta" in status_mat:
        cor_alerta = "warning"
        status_exibicao = f"ATENÇÃO: {ia_mensagem if ia_risco > 40 else status_mat}"
    else:
        cor_alerta = "info"
        status_exibicao = "ESTÁVEL: Operação Nominal"

    contexto = {
        'registro': registro,
        'analise': analise,
        'todos_ids': todos_ids,
        'grafico_dados': {
            'atual': float(analise.get('delta_temp', 0)),
            'media_cat': float(media_categoria_db),
            'media_falha': float(media_falha_db)
        },
        'status_personalizado': status_exibicao,
        'cor_alerta': cor_alerta,
        'historico': request.session.get('historico_simulacao', [])
    }
    
    return render(request, 'monitoramento/index.html', contexto)