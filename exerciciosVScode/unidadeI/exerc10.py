import time
import random

def gerar_tarefas(qtd_tarefas):
    """
    Gera uma lista de tarefas simuladas para o processamento de dados dos sensores.
    Cada tarefa é representada por um dicionário que contém um 'id', uma
    'descricao' e uma 'prioridade' associada.
    """
    tarefas = []
    sensores = ["LIDAR", "câmera", "ultrassônico"]
    prioridades = ["alta", "media", "baixa"]
    
    for i in range(1, qtd_tarefas + 1):
        tarefa = {
            "id": i,
            "descricao": f"Processar dados do sensor {random.choice(sensores)}",
            "prioridade": random.choice(prioridades)
        }
        tarefas.append(tarefa)
    
    return tarefas

def adicionar_tarefa(fila_tarefas, tarefa):
    """
    Adiciona uma nova tarefa ao final da fila de tarefas.
    """
    fila_tarefas.append(tarefa)
    return fila_tarefas

def processar_tarefa(fila_tarefas):
    """
    Processa a tarefa que está no início da fila, simulando o processamento em
    tempo real.
    Remove a tarefa processada da fila e retorna a fila atualizada.
    """
    if len(fila_tarefas) > 0:
        tarefa = fila_tarefas.pop(0)
        print(f"Processando tarefa ID: {tarefa['id']}, Descrição: {tarefa['descricao']}, Prioridade: {tarefa['prioridade']}")
        time.sleep(1)  # Simula o tempo de processamento da tarefa
    else:
        print("Nenhuma tarefa para processar.")
    
    return fila_tarefas

def principal():
    # Gerar uma fila inicial de tarefas simuladas
    qtd_inicial_tarefas = 5
    fila_tarefas = gerar_tarefas(qtd_inicial_tarefas)
    
    print("Fila inicial de tarefas:")
    for tarefa in fila_tarefas:
        print(tarefa)
    
    print("\nProcessamento das tarefas em tempo real:")
    # Processar todas as tarefas na fila
    while fila_tarefas:
        fila_tarefas = processar_tarefa(fila_tarefas)
    
    # Inserir uma nova tarefa simulando a chegada de dados de sensores em tempo real
    nova_tarefa = {
        "id": qtd_inicial_tarefas + 1,
        "descricao": "Processar dados do sensor GPS",
        "prioridade": "alta"
    }
    fila_tarefas = adicionar_tarefa(fila_tarefas, nova_tarefa)
    
    print("\nNova tarefa adicionada. Fila atual:")
    print(fila_tarefas)

if __name__ == "__main__":
    principal()

