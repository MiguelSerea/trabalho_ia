from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .utils import fuzzy_potassio, fuzzy_fosforo

@csrf_exempt
def process_request(request):
    if request.method == 'POST':
        try:
            # Parse o JSON recebido no corpo da requisição
            data = json.loads(request.body)
            print("Dados recebidos:", data)  # Debug

            # Extrai e converte os valores necessários para os cálculos
            CTC_ph7 = float(data.get('CTC_ph7', 0.0))
            argila = float(data.get('argila', 0.0))
            P = float(data.get('P', 0.0))
            K = float(data.get('K', 0.0))
            
            # Verifica se algum valor foi passado incorretamente
            if any(v is None or v == 0.0 for v in [CTC_ph7, argila, P, K]):
                print("Erro nos valores recebidos.")  # Debug
                return JsonResponse({
                    "status": "failed",
                    "valor_potassio_hectare": 0.0,
                    "valor_fosforo_hectare": 0.0
                }, status=400)

            # Calcula os valores usando as funções utilitárias
            valor_potassio_hectare = fuzzy_potassio(K, CTC_ph7)
            valor_fosforo_hectare = fuzzy_fosforo(P, argila)
            print("Resultado cálculos:", valor_potassio_hectare, valor_fosforo_hectare)  # Debug

            # Retorna a resposta JSON com os valores calculados e o status de sucesso
            return JsonResponse({
                "status": "success",
                "valor_potassio_hectare": valor_potassio_hectare,
                "valor_fosforo_hectare": valor_fosforo_hectare
            })

        except (json.JSONDecodeError, ValueError) as e:
            print("Erro de parsing ou valor:", e)  # Debug
            return JsonResponse({
                "status": "failed",
                "valor_potassio_hectare": 0.0,
                "valor_fosforo_hectare": 0.0
            }, status=400)
        except Exception as e:
            print("Erro inesperado:", e)  # Debug
            return JsonResponse({
                "status": "failed",
                "valor_potassio_hectare": 0.0,
                "valor_fosforo_hectare": 0.0
            }, status=500)

    return JsonResponse({'message': 'Método não permitido'}, status=405)
