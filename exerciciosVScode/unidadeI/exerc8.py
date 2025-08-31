import random
from datetime import datetime, timedelta

def gerar_registros(qtd_registros, inicio, intervalo_segundos):
    """
    Gera uma lista de registros simulados, na qual cada registro é um dicionário
    representando uma transação em um banco NoSQL distribuído. Cada registro contém
    um 'id', 'timestamp','valor' e 'id_dispositivo'.
    """
    registros = []
    tempo_atual = inicio
    for i in range(1, qtd_registros + 1):
        registro = {
            "id": i,
            "timestamp": tempo_atual,
            "valor": round(random.uniform(10.0, 500.0), 2),
            "id_dispositivo": random.choice(["disp_001", "disp_002", "disp_003", "disp_004"])
        }
        registros.append(registro)
        tempo_atual += timedelta(seconds=intervalo_segundos)
    return registros

def filtrar_registros_por_valor(registros, valor_minimo):
    """
    Filtra e retorna os registros cuja transação possui um valor maior ou igual
    a 'valor_minimo'.
    """
    registros_filtrados = [reg for reg in registros if reg["valor"] >= valor_minimo]
    return registros_filtrados

def inserir_registro(registros, novo_registro, posicao=None):
    """
    Insere um novo registro na lista de registros. Se a posição não for
    especificada ou for inválida, o registro é adicionado ao final da lista.
    """
    if posicao is None or posicao >= len(registros):
        registros.append(novo_registro)
    else:
        registros.insert(posicao, novo_registro)
    return registros

def remover_registros_antigos(registros, tempo_limite):
    """
    Remove da lista de registros aqueles cujo timestamp é anterior ao 'tempo_
    limite'.
    """
    registros_atualizados = [reg for reg in registros if reg["timestamp"] >= tempo_limite]
    return registros_atualizados

def principal():
    inicio = datetime.now()
    qtd_registros = 50  # Número de registros simulados
    intervalo_segundos = 30  # Intervalo de 30 segundos entre cada registro
    
    # Gerar registros simulados
    registros = gerar_registros(qtd_registros, inicio, intervalo_segundos)
    
    print("Exibindo os primeiros 5 registros gerados:")
    for reg in registros[:5]:
        print(f"ID: {reg['id']} | Timestamp: {reg['timestamp']} | Valor: {reg['valor']} | Dispositivo: {reg['id_dispositivo']}")
    
    # Filtrar registros com valor maior ou igual a 300
    valor_minimo = 300.0
    registros_filtrados = filtrar_registros_por_valor(registros, valor_minimo)
    print(f"\nQuantidade de registros com valor >= {valor_minimo}: {len(registros_filtrados)}")
    
    # Inserir um novo registro
    novo_registro = {
        "id": len(registros) + 1,
        "timestamp": registros[-1]["timestamp"] + timedelta(seconds=intervalo_segundos),
        "valor": round(random.uniform(10.0, 500.0), 2),
        "id_dispositivo": "disp_005"
    }
    registros = inserir_registro(registros, novo_registro)
    print(f"\nNovo registro inserido: ID: {novo_registro['id']} | Timestamp: {novo_registro['timestamp']} | Valor: {novo_registro['valor']} | Dispositivo: {novo_registro['id_dispositivo']}")
    print(f"Total de registros após inserção: {len(registros)}")
    
    # Remover registros com timestamp anterior a 2 minutos após o início
    tempo_limite = inicio + timedelta(minutes=2)
    registros_atualizados = remover_registros_antigos(registros, tempo_limite)
    print(f"\nQuantidade de registros após remoção dos antigos (antes de {tempo_limite}): {len(registros_atualizados)}")

if __name__ == "__main__":
    principal()