
import numpy as np
from datetime import datetime, timedelta

def gerar_logs_acesso_array(qtd_logs, inicio, intervalo_segundos):
    dtipo = np.dtype([
        ('timestamp', 'datetime64[ns]'),
        ('ip', 'U15'),
        ('usuario', 'U20'),
        ('status', 'U7')
    ])
    registros = np.empty(qtd_logs, dtype=dtipo)
    lista_ips = np.array(["192.168.1.1", "192.168.1.2",
                         "192.168.1.3", "10.0.0.1", "10.0.0.2"])
    lista_usuarios = np.array(["usuario_a", "usuario_b",
                              "usuario_c", "usuario_d"])
    lista_status = np.array(["sucesso", "falha"])
    pesos_status = np.array([0.8, 0.2])
    tempo_atual = inicio
    
    for idx in range(qtd_logs):
        registros[idx] = (
            np.datetime64(tempo_atual, 'ns'),
            np.random.choice(lista_ips),
            np.random.choice(lista_usuarios),
            np.random.choice(lista_status, p=pesos_status)
        )
        tempo_atual += timedelta(seconds=intervalo_segundos)
    
    return registros

def detectar_ips_suspeitos_array(registros, limiar_falhas):
    falhas_mask = registros['status'] == 'falha'
    ips_com_falha = registros['ip'][falhas_mask]
    ips_unicos, contagens = np.unique(ips_com_falha, return_counts=True)
    return ips_unicos[contagens >= limiar_falhas]

def inserir_log_array(registros, novo_log):
    dtipo = registros.dtype
    registro_np = np.array(
        (np.datetime64(novo_log['timestamp'], 'ns'),
         novo_log['ip'],
         novo_log['usuario'],
         novo_log['status']),
        dtype=dtipo
    )
    return np.append(registros, registro_np)

def principal():
    inicio = datetime.now()
    qtd_logs = 100
    intervalo_segundos = 30
    registros = gerar_logs_acesso_array(qtd_logs, inicio, intervalo_segundos)
    
    print("Primeiros cinco logs:\n")
    for log in registros[:5]:
        ts = log['timestamp'].astype('datetime64[ms]').astype(datetime)
        print(f"Timestamp: {ts} | IP: {log['ip']} | Usuário: {log['usuario']} | Status: {log['status']}")
    
    limiar_falhas = 3
    ips_suspeitos = detectar_ips_suspeitos_array(registros, limiar_falhas)
    print(f"\nIPs suspeitos (com {limiar_falhas} ou mais falhas): {ips_suspeitos}")
    
    # criação do novo registro utilizando numpy.timedelta64
    novo_ts = registros[-1]['timestamp'] + np.timedelta64(intervalo_segundos, 's')
    novo_log = {
        "timestamp": novo_ts,
        "ip": "192.168.1.99",
        "usuario": "usuario_novo",
        "status": "falha"
    }
    registros = inserir_log_array(registros, novo_log)
    
    print("\nNovo log inserido:")
    ts_novo = novo_log['timestamp'].astype('datetime64[ms]').astype(datetime)
    print(f"Timestamp: {ts_novo} | IP: {novo_log['ip']} | Usuário: {novo_log['usuario']} | Status: {novo_log['status']}")
    print(f"Total de logs após inserção: {len(registros)}")

if __name__ == "__main__":
    principal()