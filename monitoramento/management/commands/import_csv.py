import pandas as pd
from django.core.management.base import BaseCommand
from monitoramento.models import AtivoEletrico
import os

class Command(BaseCommand):
    help = 'Importa dados do dataset de manutenção preditiva do Kaggle para o banco de dados'

    def handle(self, *args, **kwargs):
        file_path = os.path.join('data', 'predictive_maintenance.csv')
        
        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f'Arquivo não encontrado em: {file_path}'))
            return

        self.stdout.write(self.style.SUCCESS('Lendo arquivo CSV...'))
        df = pd.read_csv(file_path)
        try:
            ativos_para_criar = []
            
            self.stdout.write(self.style.WARNING('Processando linhas... aguarde.'))

            for index, row in df.iterrows():
                ativo = AtivoEletrico(
                    product_id=row['Product ID'],
                    tipo=row['Type'],
                    temp_ar_k=row['Air temperature [K]'],
                    temp_processo_k=row['Process temperature [K]'],
                    rotacao_rpm=row['Rotational speed [rpm]'],
                    torque_nm=row['Torque [Nm]'],
                    desgaste_ferramenta_min=row['Tool wear [min]'],
                    falha_real=bool(row['Machine failure']),
                    tipo_falha_real=self.get_failure_type(row) 
                )
                ativos_para_criar.append(ativo)

                if len(ativos_para_criar) >= 1000:
                    AtivoEletrico.objects.bulk_create(ativos_para_criar)
                    ativos_para_criar = []
                    self.stdout.write(f'Importadas {index + 1} linhas...')

            if ativos_para_criar:
                AtivoEletrico.objects.bulk_create(ativos_para_criar)

            self.stdout.write(self.style.SUCCESS(f'Sucesso! Todas as {len(df)} linhas foram importadas.'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Erro durante a importação: {e}'))

    def get_failure_type(self, row):
        """Função auxiliar para identificar a string da falha no dataset original"""
        if row['TWF'] == 1: return 'Tool Wear Failure'
        if row['HDF'] == 1: return 'Heat Dissipation Failure'
        if row['PWF'] == 1: return 'Power Failure'
        if row['OSF'] == 1: return 'Overstrain Failure'
        if row['RNF'] == 1: return 'Random Failure'
        return 'Nenhuma'