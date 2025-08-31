import random
def gerar_dados_sensor(qtd_leituras):
    dados_sensor = [round(random.uniform(15.0, 35.0), 2) for _ in range(qtd_leituras)]
    return dados_sensor
def filtrar_temperaturas_altas(dados_sensor, limite=30.0):
    leituras_altas = [temperatura for temperatura in dados_sensor if temperatura> limite]
    return leituras_altas
def inserir_leitura_sensor(dados_sensor, nova_leitura, posicao=None):

    if posicao is None or posicao >= len(dados_sensor):
        dados_sensor.append(nova_leitura)
    else:
        dados_sensor.insert(posicao, nova_leitura)
    return dados_sensor
def remover_leituras_anormais(dados_sensor, limite_inferior=15.0, limite_superior=35.0):
    dados_limpos = [temperatura for temperatura in dados_sensor if limite_inferior <= temperatura <= limite_superior]
    return dados_limpos
def principal():
    quantidade_leituras = 10000 # Número de leituras simuladas
    dados = gerar_dados_sensor(quantidade_leituras)
    print(f"Quantidade de leituras geradas: {len(dados)}")
    leituras_com_temperatura_alta = filtrar_temperaturas_altas(dados, limite=30.0)
    print(f"Quantidade de leituras acima de 30°C: {len(leituras_com_temperatura_alta)}")
    nova_leitura = 28.5 
    dados = inserir_leitura_sensor(dados, nova_leitura)
    print(f"Quantidade de leituras após inserção: {len(dados)}")
    dados_limpos = remover_leituras_anormais(dados, limite_inferior=15.0,limite_superior=35.0)
    print(f"Quantidade de leituras após remoção de anomalias: {len(dados_limpos)}")
if __name__ == "__main__":
    principal()