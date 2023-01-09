from collections import Counter
from heapq import heappush, heappop

simbolos=["A","F","1","3","0","M","T"]
frecuencias=[0.2,0.17,0.13,0.21,0.05,0.09,0.15]

def AH (simbolos, frecuencias):
    frecuencias= list(zip(simbolos,frecuencias))
    lista_nodos= []
    for simbolos, frecuencia in frecuencias:
        heappush(lista_nodos,(frecuencia,len(lista_nodos),simbolos))
        while len(lista_nodos) > 1:
            frecuencia1, _, simbolo1 = heappop(lista_nodos)
            frecuencia2, _, simbolo2 = heappop(lista_nodos)
            heappush(lista_nodos, (frecuencia1 + frecuencia2, len(lista_nodos), (simbolo1, simbolo2)))
    return lista_nodos[0]

def huffman2(arbol):
    codigo = {}
    def codigo1(nodo, codigo2):
        if isinstance(nodo[2], str):
            codigo[nodo[2]] = codigo2
        else:
            codigo1(nodo[2][0], codigo2 + "0")
            codigo1(nodo[2][1], codigo2 + "1")

    codigo1(arbol, "")
    return codigo


def comprimir(text, codes):
    return "".join([codes[char] for char in text])

def descomprimir(compressed, arbol):
    text = ""
    nodo = arbol
    for char in compressed:
        if isinstance(nodo[2], str):
            texto += nodo[2]
            nodo = arbol
        else:
            nodo = nodo[2][int(char)]
    texto += nodo[2]
    return texto