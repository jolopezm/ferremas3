import requests
from datetime import datetime, timedelta
from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    # Obtener la fecha actual en el formato YYYY-MM-DD
    today = datetime.today()
    yesterday = today - timedelta(days=1)
    yesterday = yesterday.strftime('%Y-%m-%d')
    today = today.strftime('%Y-%m-%d')

    # Tu nombre de usuario y contraseña
    user = 'nico.munozt@duocuc.cl'
    password = 'Host_Duoc65'
    timeseries = 'F073.TCO.PRE.Z.D'  # Supongamos que este es el código de serie del dólar

    # URL de la API
    url = f'https://si3.bcentral.cl/SieteRestWS/SieteRestWS.ashx?user={user}&pass={password}&firstdate={today}&lastdate={today}&timeseries={timeseries}&function=GetSeries'

    # Realizar la solicitud a la API
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        series_data = data.get('Series', {}).get('Obs', [])

        # Renderizar los datos en la plantilla
        return render(request, 'index.html', {'series_data': series_data})
    else:
        return JsonResponse({'error': 'No se pudo obtener los datos del Banco Central'}, status=500)
