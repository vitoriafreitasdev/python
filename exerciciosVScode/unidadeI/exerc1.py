def calcular_despesas(salario, despesas):
    salario_restante = salario - despesas 
    return salario_restante

def sugerir_poupanca(valor_restante):
    valor_adicionado = 0.20 * valor_restante
    return valor_adicionado

try:

    saldo = float(input("Seu saldo: "))
    despesas = float(input("Suas despesas: "))
    tem_poupanca = input("Tem poupança (sim/nao): ").lower().strip()
    poupanca = 0

    if tem_poupanca not in ["sim", "nao"]:
        raise ValueError("Valor inserido incorreto")    
    
    if saldo < 0:
        raise ValueError("Saldo não pode ser negativo")    

    restante = calcular_despesas(saldo, despesas)

    if restante > 0 and tem_poupanca == "sim":
        resposta = input("Deseja reservar 20% do salário  na poupança? (sim/nao): ").strip().lower()
        if resposta == "sim":
            poupanca = sugerir_poupanca(restante)
            restante = restante - poupanca

    if restante and tem_poupanca == "nao":
        resposta = input("Deseja começar a reservar 20% do salário  na poupança? (sim/nao): ").strip().lower()
        if resposta == "sim":
            poupanca = sugerir_poupanca(restante)
            restante = restante - poupanca


    print("-- resultados --")
    print(f"Saldo inserido: {saldo}")
    print(f"Despesas inserida: {despesas}")
    print(f"Poupança: {poupanca}")
    print(f"Dinheiro restante: {restante}")

except ValueError as e:
    print(f"Erro {e}")

