def proceso(lista):
    resultado= []
    for i in range (len(lista)):
        if lista[i] % 2 == 0:
            resultado.append(lista[i] // 2)
        else:
            resultado.append(lista[i]* 2)
    return resultado

lista_ejemplo = [1,2,3,4,5]

print(proceso(lista_ejemplo))

"""
Prueba modificación y convertir a documento python
"""