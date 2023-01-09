precio = [103, 60, 70, 5, 15] 
pesos = [12, 23, 11, 15, 7]
peso_maximo = 100

def mochila(peso_máximo, pesos, precio, n):
    if n == 0 or peso_maximo == 0:
        return 0
    elif pesos [n-1] > peso_maximo:
        return mochila(peso_maximo, pesos, precio, n-1)
    else:
        return max(precio[n-1] + mochila(peso_maximo-pesos[n-1], pesos, precio, n-1), mochila(peso_maximo, pesos, precio, n-1))
    
    print(mochila(peso_mxima, pesos, precio, len(precio)))