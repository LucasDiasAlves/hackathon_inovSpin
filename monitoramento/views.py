from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def monitoramento(request):
    return render(request, 'monitoramento/dashboard.html')
    