# Documentação http://apiadvisor.climatempo.com.br/doc/index.html
import requests
import json


TOKEN = 'd5dacfbddfd067d8145bfddfe51f2929'
ID_BRASILIA = 8173

"""
# Buscando cidade
# "http://apiadvisor.climatempo.com.br/api/v1/locale/city?name=São Paulo&state=SP&token=your-app-token"

cidade = 'Brasília'
url = f"http://apiadvisor.climatempo.com.br/api/v1/locale/city?name={cidade}&token={TOKEN}"
response = requests.request('GET', url)
retorno_req = json.loads(response.text)
print(retorno_req)
"""

# Registrando o id da cidade em meu token
# iURL = "http://apiadvisor.climatempo.com.br/api-manager/user-token/" + TOKEN + "/locales"
# payload = "localeId[]=" + str(ID_BRASILIA)
# headers = {'Content-Type': 'application/x-www-form-urlencoded'}
# iRESPONSE = requests.request("PUT", iURL, headers=headers, data=payload)
# print(iRESPONSE.text)



busca_previsao = requests.get(f'http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/{ID_BRASILIA}/days/15?token={TOKEN}')
print(json.loads(busca_previsao.text))
