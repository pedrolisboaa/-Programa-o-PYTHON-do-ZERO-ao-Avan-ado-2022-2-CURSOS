import requests
import json

print("#################")
print('#Buscador de CEP#')
print("#################")
print()


cep = 71699005

busca_cep = requests.get(f'https://cep.awesomeapi.com.br/json/{cep}').json()
print(busca_cep)

#dados
distrito = busca_cep['district']
endereco = busca_cep['address']
cidade = busca_cep['city']
estado = busca_cep['state']

lat_lon = [float(busca_cep['lat']), float(busca_cep['lng']) ]


print(f'{estado} {cidade} - {distrito} {endereco}')
print(f'Coordenadas {lat_lon[0]} {lat_lon[1]}')

