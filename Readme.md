# Fuzzyficação de dados utilizando python com django

  - Este projeto foi desenvolvido como microsserviço de um trabalho da disciplina de **Inteligência Artificial** para extrair dados específicos (``CTC_ph7``,``argila``,``K``,``P``) de laudos de análise de solo emitidos pelo **Labfertil**. Utiliza **Django** para criar uma API e **skfuzzy** para manipular os dados recebidos, permitindo que os dados sejam fuzzyficados e retornados ao fazer a requisição por meio de um ``json``enviados via requisição HTTP ``POST``.<br>

  

## Estrutura do Projeto

1. **Dependências:** `requirements.txt` - Lista de pacotes Python necessários, incluindo:
   - django
   - numpy
   - scipy
   - scikit-fuzzy
   - packaging
   - networkx

     
2. **Servidor Hospedado localmente:** é hospedada em `http://localhost:8000/dashboard/process_request/`, que:
   - Aceita apenas requisições **POST**.
   - Processa jsons enviados para o sufixo `/dashboard/process_request/` dessa URL.
   - confira se o servidor ainda está rodando localmente e esteja atento ao status do erro:
   - ````405 Method Not Allowed````: Tentativa de usar método ``GET`` onde aceita-se apenas método ``POST``, porém, significa que a URL foi encontrada e o servidor está rodando localmente.
   - ````404 Not Found````: Significa que a URL não foi encontrada e o servidor não está rodando.
   - Caso online, você poderá testá-la via Postman, ou pela aplicação principal:

## Configuração e Execução

### Requisitos

1. **Instale as dependências listadas em `requirements.txt`:**

   ```bash
   pip install -r requirements.txt
   ```

2. Verifique se o firewall permite conexões na porta 8000.

## Execução da Aplicação
1. Coloque o server para rodar localmente com o comando:
```bash
   python manage.py runserver
   ```

3. Verifique a versão do python
  Há um problema apartir da versão 3.13.0 do python, usar sempre versão do python inferiores!
  recomendo a versão 3.12.6
   
# Estrutura de Retorno
A resposta será um ``JSON`` com os valores extraídos. Em caso de falha, o campo ``"status"`` será ``"failed"`` e os campos não identificados terão valor ``null``.

Exemplo de JSON de enivio numa operação de sucesso:
```json
{
  "CTC_ph7": 25.0,
  "argila": 35.0,
  "P": 9.3,
  "K": 200.0
}
```
Resposta esperada:
```json
{
"status": "success",
"valor_potassio_hectare": 29.28,
"valor_fosforo_hectare": 136.07
}

```

Exemplo de JSON de envio numa operação onde há falha:
```json
{
  "CTC_ph7": 25.0,
  "argila": 35.0,
  "P": "error",
  "K": 200
}

```
Resposta esperada:
```json
{
"status": "failed",
"valor_potassio_hectare": 0.0,
"valor_fosforo_hectare": 0.0
}

```
---
Obrigado por se interessar pelo projeto!
