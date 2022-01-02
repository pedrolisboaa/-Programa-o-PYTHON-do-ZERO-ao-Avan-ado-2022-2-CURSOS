def agencia(**kargs):
    return kargs


carro = agencia(modelo='uno', motor=1.0, cor='vermelho')
carro2 = agencia(modelo='gol', motor=1.4, cor='branco', teto_solar=True)
print(carro)
print(carro2)