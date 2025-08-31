import random
from datetime import datetime, timedelta
def gerar_logs_temporais(qtd_logs, inicio, intervalo_segundos):
    logs = []
    tempo_atual = inicio
    for _ in range(qtd_logs):
        valor = round(random.uniform(20.0, 80.0), 2)
        log = {"tempo": tempo_atual, "valor": valor}
        logs.append(log)
        tempo_atual += timedelta(seconds=intervalo_segundos)
    return logs
def calcular_media_movel(logs, janela):
    medias_moveis = []
    for i in range(len(logs) - janela + 1):
        soma = sum(log["valor"] for log in logs[i:i+janela])
        media = soma / janela
        registro_media = {"tempo": logs[i+janela - 1]["tempo"], "media":round(media, 2)}
        medias_moveis.append(registro_media)
    return medias_moveis

def inserir_log(logs, novo_log, posicao=None):
    if posicao is None or posicao >= len(logs):
        logs.append(novo_log)
    else:
        logs.insert(posicao, novo_log)
    return logs
def detectar_anomalias(medias_moveis, limite):

    anomalias = [registro for registro in medias_moveis if registro["media"] > limite]
    return anomalias
def principal():
    inicio = datetime.now()
    qtd_logs = 100 # Número de logs simulados
    intervalo_segundos = 60 # Intervalo de 60 segundos entre cada log
    logs = gerar_logs_temporais(qtd_logs, inicio, intervalo_segundos)
    print("Exibindo os primeiros 5 logs gerados:")
    for log in logs[:5]:
        print(f"{log['tempo']} – Valor: {log['valor']}")
    janela = 5 # Tamanho da janela para o cálculo da média móvel
    medias_moveis = calcular_media_movel(logs, janela)
    print("\nExibindo as primeiras 5 médias móveis calculadas:")
    for media in medias_moveis[:5]:
        print(f"{media['tempo']} – Média: {media['media']}")
    limite_anomalia = 70.0 
    anomalias = detectar_anomalias(medias_moveis, limite_anomalia)
    print(f"\nQuantidade de anomalias detectadas (média móvel > {limite_anomalia}): {len(anomalias)}")

    nova_data = logs[-1]["tempo"] + timedelta(seconds=intervalo_segundos)
    novo_valor = round(random.uniform(20.0, 80.0), 2)
    novo_log = {"tempo": nova_data, "valor": novo_valor}
    logs = inserir_log(logs, novo_log)
    print(f"\nNovo log inserido: {novo_log['tempo']} – Valor: {novo_log['valor']}")
    print(f"Total de logs após inserção: {len(logs)}")
if __name__ == "__main__":
    principal()