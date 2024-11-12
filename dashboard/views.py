from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def process_request(request):
    if request.method == 'POST':
        try:
            # Parse o JSON recebido no corpo da requisição
            data = json.loads(request.body)

            # Extraia os dados das chaves do JSON
            status = data.get('status', 'failed')  # Status (espera-se 'failed' ou 'success')
            
            # Se o status for 'failed', não faz os cálculos
            if status == 'failed':
                return JsonResponse({
                    "status": "failed",
                    "valor_potassio_hectare": 0.0,
                    "valor_fosforo_hectare": 0.0
                })

            # Caso contrário, processa os valores
            CTC_ph7 = float(data.get('CTC_ph7', 0.0))
            argila = float(data.get('argila', 0.0))
            P = float(data.get('P', 0.0))
            K = float(data.get('K', 0.0))

            # Processamento dos valores para a resposta
            valor_potassio_hectare = CTC_ph7 * 2  # Exemplo de cálculo
            valor_fosforo_hectare = argila * 3    # Exemplo de cálculo

            return JsonResponse({
                "status": status,
                "valor_potassio_hectare": valor_potassio_hectare,
                "valor_fosforo_hectare": valor_fosforo_hectare
            })

        except (json.JSONDecodeError, ValueError) as e:
            return JsonResponse({
                "status": "failed",
                "valor_potassio_hectare": 0.0,
                "valor_fosforo_hectare": 0.0
            }, status=400)

    return JsonResponse({'message': 'Método não permitido'}, status=405)
