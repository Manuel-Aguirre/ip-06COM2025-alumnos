# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool} 

items = []        # Acá guardamos la lista original que el visualizador va a ordenar.
n = 0             # Tamaño de la lista.

pasos = []        # Lista donde vamos a guardar todos los intercambios que hay que hacer.
pos_paso = 0      # En qué paso estamos (un índice dentro de la lista 'pasos').


def init(vals):
    # La idea principal de Merge, ya que se puede hacer de diversas formas es:
    # Copiar la lista original para que haga una idea de intercambios para llegar a la lista ordenada.
    # Esa misma idea de ejecutaría siguiendo una lista de pasos para que Step() solamente la ejecute 1 vez más.
    global items, n, pasos, pos_paso

    # Copiamos la lista original.
    items = list(vals)
    n = len(items)

    # Reiniciamos todo para arrancar desde cero, por eso 0.
    pasos = []
    pos_paso = 0

    # Hacemos otra copia solo para calcular cómo ordenaríamos la lista, por eso se llama la variable "temporal".
    temporal = list(vals)

    # "ordenada" va a ser la lista temporal pero ordenada usando un mini Insertion Sort.
    ordenada = list(temporal)

    # Usamos minis insertion sort para que pueda ordenar temporalmente esta lista.
    # Que hacemos? Ordenar la listra de mayor a menor.
    for x in range(1, len(ordenada)):
        valor = ordenada[x]                 # elemento que vamos a insertar
        j = x - 1

        # Lo movemos hacia atrás mientras el de atrás sea mayor que "valor".
        while j >= 0 and ordenada[j] > valor:
            ordenada[j + 1] = ordenada[j]
            j -= 1

        # Y colocamos el "valor" en el lugar que corresponde.
        ordenada[j + 1] = valor

    # Ahora precisamos idear swaps para poder:
    # Miramos qué valor debería ir ahí en ordenada[i].
    # Buscamos ese valor en la lista temporal.
    # Lo vamos trayendo hacia la posición i con swaps cortos (j-1, j).
    # Cada uno de esos swaps lo guardamos en la lista de "pasos" como explicamos al principio.
    # Después step() va a ejecutar los swaps.

    for i in range(n):

        # El valor que debería estar en la posición i según la lista ordenada.
        valorCorrecto = ordenada[i]

        # Buscamos dónde está ese valor dentro del temporal
        j = i
        while j < n and temporal[j] != valorCorrecto:
            j += 1

        # Una vez encontrado, lo traemos desde j hasta i usando swaps cortos.
        while j > i:
            # Guardamos el swap necesario, y utilizamos .append para ver el final.
            pasos.append((j - 1, j))

            # Aplicamos ese swap sobre el temporal y poder seguir calculando bien el resto.
            temporal[j - 1], temporal[j] = temporal[j], temporal[j - 1]

            # Avanzamos hacia la izquierda.
            j -= 1

    # Toda esta secuencia de pasos la hicimos gracias a la lista temporal, porque:
    # Aún no podíamos modificar la lista original ya que necesitamos darle intrucciones previas para que se realice bien.
    # Ahora sí podemos hacer que steps pueda mover la lista original.


def step():
    # El visualizador aplica en la funcion "items" cada vez que lo llama para avisar que hay posiciones moviendose.
    # Cuando no hayan más pasos que hacer, done = True.
    global items, n, pasos, pos_paso

    # Si ya ejecutamos todos los pasos, entonces el algoritmo terminó.
    if pos_paso >= len(pasos):
        return {"a": 0, "b": 0, "swap": False, "done": True}

    # Tomamos el siguiente par de posiciones a intercambiar.
    a, b = pasos[pos_paso]
    pos_paso += 1

    # Intercambiamos realmente dentro de la lista que se muestra en pantalla.
    # Esta vez no usamos auxiliar porqué la sobrecarga de procesos hace que el visualizador piense que ya termino cuando se queda en mitad del intercambio de elementos.
    items[a], items[b] = items[b], items[a]

    # Avisamos al visualizador que hubo un swap y que seguimos.
    return {"a": a, "b": b, "swap": True, "done": False}
