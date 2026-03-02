from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import AtivoEletrico
@admin.register(AtivoEletrico)
class GrAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'falha_real')
    search_fields = ('product_id','falha_real')

admin.site.site_header = "Monitoramento Preditiva"
admin.site.site_title = "Admin"
admin.site.index_title = "Gestão de dados"