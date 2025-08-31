
def adicionar_transacao(pilha_transacoes, transacao):
    """
    Adiciona uma nova transação à pilha principal.
    """
    pilha_transacoes.append(transacao)
    return pilha_transacoes

def desfazer_transacao(pilha_transacoes, pilha_transacoes_desfeitas):
    """
    Remove a transação do topo da pilha principal e a adiciona à pilha de
    transações desfeitas.
    """
    if pilha_transacoes:
        transacao = pilha_transacoes.pop()
        pilha_transacoes_desfeitas.append(transacao)
        print(f"Transação desfeita: {transacao}")
    else:
        print("Nenhuma transação para desfazer.")
    return pilha_transacoes, pilha_transacoes_desfeitas

def refazer_transacao(pilha_transacoes, pilha_transacoes_desfeitas):
    """
    Remove a transação do topo da pilha de transações desfeitas e a retorna para
    a pilha principal.
    """
    if pilha_transacoes_desfeitas:
        transacao = pilha_transacoes_desfeitas.pop()
        pilha_transacoes.append(transacao)
        print(f"Transação refeita: {transacao}")
    else:
        print("Nenhuma transação para refazer.")
    return pilha_transacoes, pilha_transacoes_desfeitas

def exibir_pilhas(pilha_transacoes, pilha_transacoes_desfeitas):
    """
    Exibe o conteúdo das pilhas de transações e de transações desfeitas.
    """
    print("\nPilha de Transações Atuais:")
    for t in pilha_transacoes:
        print(t)
    print("\nPilha de Transações Desfeitas:")
    for t in pilha_transacoes_desfeitas:
        print(t)

def principal():
    # Pilhas para armazenar transações
    pilha_transacoes = []
    pilha_transacoes_desfeitas = []
    
    # Adicionando transações iniciais
    transacoes_iniciais = [
        "Transação 1: Envio de 100 tokens",
        "Transação 2: Recebimento de 50 tokens",
        "Transação 3: Pagamento de 30 tokens",
        "Transação 4: Envio de 20 tokens"
    ]
    
    for transacao in transacoes_iniciais:
        pilha_transacoes = adicionar_transacao(pilha_transacoes, transacao)
    
    print("Estado inicial das pilhas:")
    exibir_pilhas(pilha_transacoes, pilha_transacoes_desfeitas)
    
    # Desfazendo duas transações
    pilha_transacoes, pilha_transacoes_desfeitas = desfazer_transacao(pilha_transacoes, pilha_transacoes_desfeitas)
    print(f"Desfeitas testes: pilha transacoes: {pilha_transacoes}, pilha desfeita: {pilha_transacoes_desfeitas}")
    pilha_transacoes, pilha_transacoes_desfeitas = desfazer_transacao(pilha_transacoes, pilha_transacoes_desfeitas)
    print(f"Desfeitas testes 2: pilha transacoes: {pilha_transacoes}, pilha desfeita: {pilha_transacoes_desfeitas}")

    
    print("\nApós desfazer duas transações:")
    exibir_pilhas(pilha_transacoes, pilha_transacoes_desfeitas)
    
    # Refazendo uma transação
    pilha_transacoes, pilha_transacoes_desfeitas = refazer_transacao(pilha_transacoes, pilha_transacoes_desfeitas)
    print(f"Desfeitas testes 3: pilha transacoes: {pilha_transacoes}, pilha desfeita: {pilha_transacoes_desfeitas}")

    
    print("\nApós refazer uma transação:")
    exibir_pilhas(pilha_transacoes, pilha_transacoes_desfeitas)

if __name__ == "__main__":
    principal()

                                                                  
                        