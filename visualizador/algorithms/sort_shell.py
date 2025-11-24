# Template genérico — SKELETON
# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
gapsalto = 0        # El salto entre posiciones
i = 0          # Posición donde estamos insertando
j = None       # Indice que se mueve hacia atrás
aux = None     # Para guardar el valor que queremos ubicar

fase = "nuevo"  # Para iniciar o recorrer.

# Arrancamos con un salto grande que compara los valores que separa en ese mismo salto.
# Si estan desordenados, los intercambia como haría un Insertion Sort pero con saltos.
# Recorre la lista en ese salto, y cuando termina se reduce a la mitad.
# Repite todo el proceso hasta que se conviertan todo en 1.
# Pero cuando queda 1 no termina ahí, hacemos un Insertion común y finalizamos.

def init(vals):
    global items, n, gapsalto, i, j, aux, fase
    items = list(vals)
    n = len(items)

    # Arrancamos con un salto grande.
    gapsalto = n // 2
    i = gapsalto             # Arranca insertion saltado
    j = None
    aux = None
    fase = "iniciar_i"      # Preparamos la primera vuelta.

def step():
    global items, n, gapsalto, i, j, aux, fase
    # Agregamos la condicion de que si salta entre posiciones (gapsalto) y es 0, esta ordenado.
    if gapsalto == 0:
        return {"done": True}

    # Iniciamos la fase iniciar_i.
    if fase == "iniciar_i":
        if i >= n:                  # Verificamos recorrer la lista con nuestra variable gapsalto
            gapsalto //= 2          # Reducimos el salto
            if gapsalto == 0:
                return {"done": True}
            
            # Reiniciamos variable "i" para el nuevo gapsalto
            i = gapsalto
            fase  = "iniciar_i"
            return {"a": 0, "b": 0, "swap": False, "done": False}

        # Pero como no terminamos, tenemos que trabajar con otros elementos.
        # Se nos une auxiliares e items.
        aux = items[i]      # Guardamos el elemento que ubicamos
        j = i               # J arranca desde "i"
        fase = "recorrer"

        return {"a": i, "b": i - gapsalto, "swap": False, "done": False}


    # La idea es hacer Insertion, como explicamos anteriormente pero con saltos.
    if fase == "recorrer":
        # Va a seguir existiendo elementos que ordenar.
        if j - gapsalto >= 0 and items[j - gapsalto] > aux:
            # Intercambiamos valores nuevamente con auxiliares.
            items[j] = items[j - gapsalto]
            items[j - gapsalto] = aux

            # Unico swap.
            resultado = {"a": j, "b": j - gapsalto, "swap": True, "done": False}

            # Movemos j hacía atras.
            j -= gapsalto
            return resultado
        
        # Si ya no tenemos más movimientos, dejamos el elemento en su lugar.
        i += 1
        fase = "iniciar_i"

        return {"a": j, "b": j - gapsalto if j - gapsalto >= 0 else j, "swap": False, "done": False}