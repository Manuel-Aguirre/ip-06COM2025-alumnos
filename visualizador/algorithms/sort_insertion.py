# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0
j = None

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 1
    j = None

def step():
    global items, n, i, j
    if i >= n:
        return {"done": True} # Una vez procesamos la lista, termina.

    if j is None: # j es None sería decir que empezamos a desplazar los items[i]
        j = i # Esto nos dice donde estamos parados.
        return {"a": j-1, "b": j, "swap": False, "done": False}
    if j > 0 and items[j] < items[j-1]: # Para verificar si todavía se desplaza para la izq.
        aux = items[j]
        items[j] = items[j-1]
        items[j-1] = aux

        j-= 1 #Avanzamos otro lugar hacia la izquierda.

        # Devolvemos un paso con swap = True.
        return {"a": j, "b": j+1, "swap": True, "done": False}

    # Una vez el elemento quedo ubicado, podemos resetear el mismo.
    i += 1
    j = None

    # Nos pide solo highlight de avance pero sin swap.
    return {"a": i-1, "b": i-1, "swap": False, "done": False}

    # items es la lista de visualizador.
    # n nos dice hasta donde llega la lista.
    # i recorre la lista de la primera posicion hasta la ultima.
    # j la usamos para mover los elementos de a un paso.

    # Inits se ejecuta cada vez que le damos a "Mezclar" o al principio de todo en estado inicial.
    # Como items0 ya esta ordenado, usamos i = 1.
    # j none es es porqué no movimos nada aún.

    # Como step lo esta llamando el visualizador muchas veces, step hace micro paso.
    # i >= n porqué "i" llego al final de la lista. Nos devuelve true porqué el algoritmo termino.

    # Como J is None, no empieza a desplazar, j = i para indicarle que queremos insertar.
    # Como es "sin swap" usamos j-1 y j, para mostrar donde estamos.
    # Esto es como decir "Me ocupo de los elementos de la posicion 1"

    # j > 0 indica que hay algo a la izquierda, un elemento.
    # Y con los items j = items j -1, para indicar el más chico, osea que sigue desordenado.
    # Usamosa uxiliar para un intercambio más comodo.
    # J se mueve una vez a la izquierda y devolvemos swap True mostrando el intercambio.

    # Sabemos que If es la condicion que se tiene que cumplir. 
    # Entoncs podemos saber que quedo en su lugar definitivo.