
def funcaoExemplo(n):
    print(n)
    if n == 10:
        return
    funcaoExemplo(n + 1)


funcaoExemplo(1)

def fatorial(n):
    
    if n <= 1:
        return 1
    
    return n * fatorial(n-1)


print(fatorial(5))