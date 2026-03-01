from django.db import models

class AtivoEletrico(models.Model):
    product_id = models.CharField(max_length=50, verbose_name="ID do Produto")
    tipo = models.CharField(max_length=1, choices=[('L', 'Low'), ('M', 'Medium'), ('H', 'High')])
    
    temp_ar_k = models.FloatField(verbose_name="Temp. Ar (K)")
    temp_processo_k = models.FloatField(verbose_name="Temp. Processo (K)")
    rotacao_rpm = models.FloatField(verbose_name="Rotação (RPM)")
    torque_nm = models.FloatField(verbose_name="Torque (Nm)")
    desgaste_ferramenta_min = models.IntegerField(verbose_name="Desgaste (min)")
    
    falha_real = models.BooleanField(default=False, verbose_name="Falha Real (Dataset)")
    tipo_falha_real = models.CharField(max_length=50, blank=True, null=True)

    status_matematico = models.CharField(max_length=100, blank=True, null=True)
    
    predicao_ia_risco = models.FloatField(blank=True, null=True, verbose_name="Risco IA (%)")
    data_leitura = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product_id} - {self.data_leitura}"

    class Meta:
        verbose_name = "Monitoramento de Ativo"
        verbose_name_plural = "Monitoramento de Ativos"