from django.shortcuts import render
from django.http import JsonResponse
import requests

def index(request):
    return render(request, 'index.html')

import json

def obtener_datos_banco_central(request):
    url = 'https://si3.bcentral.cl/SieteRestWS/SieteRestWS.ashx'
    params = {
        'user': 'nico.munozt@duocuc.cl',  # Asegúrate de que tu nombre de usuario esté correctamente codificado
        'pass': 'Host_Duoc65',    # Reemplaza 'tu_contraseña' con tu contraseña real
        'firstdate': '2023-01-01',
        'lastdate': '2023-12-31',
        'timeseries': 'F073.TCO.PRE.Z.D',  # Serie de tiempo de ejemplo
        'function': 'GetSeries'
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        print(json.dumps(data, indent=4))  # Añade esta línea para imprimir los datos en la consola
        series_data = data.get('Series', {}).get('Obs', [])
        return render(request, 'datos_banco_central.html', {'series_data': series_data})
    else:
        return JsonResponse({'error': 'No se pudo obtener los datos del Banco Central'}, status=500)