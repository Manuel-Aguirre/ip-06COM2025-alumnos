# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0
j = 0
min_idx = 0
fase = "buscar"

def init(vals):
    global items, n, i, j, min_idx, fase
    items = list(vals)
    n = len(items)
    i = 0               # Arrancamos desde la pos. 0.
    j = i + 1           # Comparamos.
    min_idx = i         # El minimo es 1, por ahora.
    fase = "buscar"     # Buscamos el minimo, fase "buscar".

def step():
    global items, n, i, j, min_idx, fase
    # Intentamos hacer que i recorra la lista de terminos
    if i >= n - 1:
        return {"done": True}

    # La consiga pide la fase "buscar". Entonces lo hacemos agregando una condicion.

    if fase == "buscar":
        if j < n:

        # Nos ayudamos comparando los items a y b junto al item actual que usamos "j".

            a = min_idx   # La posicion del numero más chico en la lista mientra lo busca.
            b = j         # Indicamos al visualizador por cual lo estamos comparando. No es un intercambio.
            swap = False  # Falso porqué no hay intercambios, solo marcamos el highlight.

            # Si encontramos un numero más chico, actualizamos el min_idx.
            if items[j] < items[min_idx]:
                min_idx = j                 # Nos ayuda a encontrar el minimo y guardarlo como "j"

            j += 1                  # Podemos avanzar con j, el clasico j = j + 1.
            return {"a": a, "b": b, "swap": swap, "done": False}

        fase = "swap"  # Pasamos a la fase de swap ayudandonos con else. Terminamos el barrido.

    if fase == "swap": # Empezamos la nueva fase, hacer el unico swap y devolverlo.
        # Si el minimo no es "i", hacemos el swap. Tiene que ser igual distinto para que no sea el mismo lugar.
        if min_idx != i: # Si el mínimo está en otra posición distinta de i, lo traemos a su lugar con un swap.
            aux = items[i]
            items[i] = items[min_idx]
            items[min_idx] = aux

            # Al hacer un unico swap, damos un "resultado", pero si no es así lo tenemos que devolver.
            resultado = {"a": i, "b": min_idx, "swap": True, "done": False}
    
        else: # Por sí hay que devolver un paso, no es opcional.
            resultado = {"a": i, "b": min_idx, "swap": False, "done": False}
    
        # La proxima vuelta del algoritmo:
        # Avanzamos con i, ya ordenado.
        # Arranca j despues desde i + 1 porque ya estamos parados en i. Buscamos el minimo en el resto de la lista.
        # Ahora el minimo nuevo empiezo por i.

        i = i + 1
        j = i + 1
        min_idx = i
        fase = "buscar"     # Fase "busqueda" para la proxima vuelta.

        # Retornamos "resultado". Con o sin swap, devolvemos el resultado.

        return resultado