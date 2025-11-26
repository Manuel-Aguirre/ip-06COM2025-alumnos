# Template genérico — SKELETON
# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
# Agregá acá tus punteros/estado, p.ej.:
# i = 0; j = 0; fase = "x"; stacks = []


stacks = []        # Stacks, por donde se guardan las "cosas/elemento" que faltan ordenar.
izqlimite = 0      # El limite izquierdo del elemento.
derlimite = 0      # El limite derecho del elemento. 
i = 0              # Marca donde quedan los numeros menores al corte de referencia.
j = 0              # Recorre el elemento actual.
corte_ref = 0      # Posiciona el numero del corte de referencia.
fase = "nuevo"     # Sacar o particionar el elemento.

def init(vals):
    global items, n, stacks, izqlimite, derlimite, i, j, corte_ref, fase
    items = list(vals)
    n = len(items)
    # Comenzamos marcando un elemento de la lista. Usando .append para marcar el final de la misma.
    stacks = []
    if n > 0:
        stacks.append((0, n - 1))
    
    # Volvemos a poner nuestras variables para ajustarlas y comenzarlas a usar en Quick Sort.

    izqlimite = 0
    derlimite = 0
    i = 0
    j = 0
    corte_ref = 0
    fase = "nuevo"

def step():
    global items, n, stacks, izqlimite, derlimite, i, j, corte_ref, fase
    # Damos una condicion por si no quedan/hay elementos por ordenar.
    if fase == "nuevo" and not stacks:
        return {"a": 0, "b": 0, "swap": False, "done": True}

    # La fase "nuevo" toma un elemento pendiente. Porque recordamos que Quick Sort no ordena todo de una.
    # Se divide en pedazos chicos, como listas y sus sublistas, ordenandolas uno x uno.
    if fase == "nuevo":
        # Obetenemos el ultimo elemento.
        ultimo = len(stacks) - 1
        izqlimite, derlimite = stacks[ultimo]

        # Volvemos a escribir la lista "pendiente" pero sin el ultimo elemento porque ya lo tenemos.
        pendiente = []
        for k in range(0, ultimo):          # Osea, todos menos el ultimo.
            pendiente.append(stacks[k])     # .append final de la lista.
        stacks = pendiente

        # Hacemos uso del corte de referencia.
        corte_ref = derlimite

        # Hacemos uso de nuestras variables "i" y "j". Que ya arranquen desde toda la izq.
        i = izqlimite
        j = izqlimite

        fase = "empezar"
        return {"a": j, "b": corte_ref, "swap": False, "done": False}

        # La nueva fase empezar va a separar los elementos en grupos:
        # Los más chicos del numero de referencia.
        # Los que son más grandes.

    if fase == "empezar":
        if j < derlimite:   # J no va a llegar al final para seguir comparando elementos.
            a = j
            b = corte_ref
            swap = False

            # Si el elemento es menor al de la referencia va hacía la izquierda.
            # Utilizamos el mismo metodo que siempre, auxiliares.
            if items[j] < items[corte_ref]:
                aux = items[i]
                items[i] = items[j]
                items[j] = aux

                # Necesitamos una variable que recopile las mismas, usamos "resultado".
                resultado = {"a": i, "b": j, "swap": True, "done": False}

                # Que se sigan comparando elementos y que vaya mirando el siguiente, de la forma:
                i += 1      # Marcamos el limite de los más chicos.
                j += 1      # Comparamos este elemento, vamos al siguiente.
                return resultado
            else:
                # Como no hay un swap, no hay intercambio de elementos, mostramos en visualizador:
                # Elementos que se comparan, sin moverse. Es avisarle al mismo lo que pasa en ese paso.
                resultado = {"a": a, "b": b, "swap": False, "done": False}
                j += 1
                return resultado
        else:
            # Ultimo intercambio usando corte de referencia.
            aux = items[i]
            items[i] = items[corte_ref]
            items[corte_ref] = aux

            corteNuevo = i

            # Generamos los elementos izquierdos y derechos para agregarlos en pendiente.
            # Empezamos con el izquierdo, si tiene un elemento mayor a 1.
            if corteNuevo - 1 > izqlimite:
                stacks.append((izqlimite, corteNuevo - 1))
            
            # Ahora nos toca lo mismo pero con el derecho.
            if corteNuevo + 1 < derlimite:
                stacks.append((corteNuevo + 1, derlimite))

            # Quick cuando termina de separar los elementos, independientemente de que sea izq. o der.
            # Usando el corte de referencia ya queda listo, pero va a necesitar buscar otro elemento pendiente.
            # Si quedan elementos de la lista sin usarse u ordenarse, hay que:
            # Agarrar el ultimo, ordenarlo, volverlo a fase "nuevo", agarrar otro, lo ordena y repetidamente el mismo proceso.

            fase = "nuevo"
            return {"a": i, "b": corte_ref, "swap": True, "done": False}
