
import time
import random
from collections import deque  # estrutura FIFO eficiente em memória
from queue import Queue  # alternativa threadsafe, usada se houver múltiplas threads

# ---------- VERSÃO MONOTHREAD COM deque ----------
def gerar_tarefas(qtd_tarefas: int) -> deque:
    """
    Cria uma fila de tarefas simuladas utilizando deque.
    Cada tarefa possui id, descrição e prioridade.
    """
    sensores = ["LIDAR", "câmera", "ultrassônico"]
    prioridades = ["alta", "média", "baixa"]
    fila = deque()
    
    for i in range(1, qtd_tarefas + 1):
        fila.append(
            {
                "id": i,
                "descricao": f"Processar dados do sensor {random.choice(sensores)}",
                "prioridade": random.choice(prioridades),
            }
        )
    return fila

def adicionar_tarefa(fila_tarefas: deque, tarefa: dict) -> deque:
    """
    Adiciona uma nova tarefa ao fim da fila em O(1).
    """
    fila_tarefas.append(tarefa)
    return fila_tarefas

def processar_tarefa(fila_tarefas: deque) -> deque:
    """
    Remove e processa a tarefa que está no início da fila em O(1).
    """
    if fila_tarefas:
        tarefa = fila_tarefas.popleft()
        print(
            f"Processando tarefa ID: {tarefa['id']}, "
            f"Descrição: {tarefa['descricao']}, "
            f"Prioridade: {tarefa['prioridade']}"
        )
        time.sleep(1)  # simula tempo de processamento
    else:
        print("Nenhuma tarefa para processar.")
    
    return fila_tarefas

def principal():
    qtd_inicial = 5
    fila = gerar_tarefas(qtd_inicial)
    
    print("Fila inicial de tarefas:")
    for t in fila:
        print(t)
    
    print("\nProcessamento das tarefas em tempo real:")
    while fila:
        processar_tarefa(fila)
    
    nova_tarefa = {
        "id": qtd_inicial + 1,
        "descricao": "Processar dados do sensor GPS",
        "prioridade": "alta",
    }
    
    adicionar_tarefa(fila, nova_tarefa)
    print("\nNova tarefa adicionada. Fila atual:")
    print(list(fila))  # converte deque para lista apenas para exibir

# ---------- ALTERNATIVA THREADSAFE COM queue.Queue ----------
def gerar_fila_threadsafe(qtd_tarefas: int) -> Queue:
    """
    Cria uma fila FIFO thread-safe que permite múltiplos produtores e
    consumidores.
    """
    sensores = ["LIDAR", "câmera", "ultrassônico"]
    prioridades = ["alta", "média", "baixa"]
    fila_segura = Queue()
    
    for i in range(1, qtd_tarefas + 1):
        fila_segura.put(
            {
                "id": i,
                "descricao": f"Processar dados do sensor {random.choice(sensores)}",
                "prioridade": random.choice(prioridades),
            }
        )
    return fila_segura

if __name__ == "__main__":
    principal()