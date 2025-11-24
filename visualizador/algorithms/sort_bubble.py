# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0
j = 0

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 0
    j = 0

# NUESTRA VARIABLE I SI ES MAYOR IGUAL QUE LA N (LISTA DE ITEMS) VA YENDO 1 +1, Y AL FINAL DE LA LISTA SE PARA AL COMPLETAR Y PASAR POR TODA LA LISTA.
# Y CUANDO YA RECORRE TODA LA LISTA, RETURNA TRUE. 

def step():
    global items, n, i, j
    if i >= n - 1:
        return {"done": True}

    a= j
    b= j + 1 

# USAMOS EL IF PARA CREAR UNA CONDICION DE QUE SI ITEM A ES MAYOR QUE ITEM B Y ESTO SE DA SIEMPRE, ASUMIMOS QUE NO HAY INTERCAMBIO.
# SWAP = FALSE LO ASUMIMOS PORQUE NO HAY UN INTERCAMBIO ENTRE ITEM A E ITEM B.

    swap = False
    if items[a] > items[b]:
        aux = items[a]               # GUARDA EL VALOR DE A
        items[a] = items[b]           # PASA EL ITEM DERECHA A LA IZQUIERDA
        items[b] = aux               # PASA EL ITEM GUARDADO A LA DERECHA
        swap = True                 # GRACIAS A AUXILIAR HUBO EL INTERCAMBIO

    # n = la lista de elementos. # i = las pasadas que hacemos. # (n - i - 1) hasta donde puede llegar j en las pasadas.
    # Podemos decir que sirve para ayudar a J para que sepa hasta que lugar puede compararse, y que al mismo tiempo no se ejecute ningún error de pasadas.
    # Nos ayudamos con un If para aclarar la condicion que tiene que cumplir J.

    j +=1                           # LA VARIABLE "i" nos dice en donde estamos parados, mientras que "j" compara las vueltas que estamos dando.
    if j == (n - i - 1):            # J DETECTA SI ESTA TERMINADO EL BUBBLE SORT.
        j = 0
        i += 1
    return {"a": a, "b": b, "swap": swap, "done": False}

    # Se usa True cuando el algoritmo termino todas las vueltas.
    # Si ponemos al final del todo "return {"a": a, "b": b, "swap": swap, "done": True}" con True al final, Bubble Sort va a penasr que ya termino.
    # Entonces usamos False por si todavía hay pasos por seguir, y True si ya se termino de ordenar e intercambiar los algoritmos.