class NODO:
    def __init__(self,clave,dato):
        self.clave = clave
        self.dato = dato
        self.der = None
        self.izq = None

    def __str__(self):
        return str(self.clave)


class ABB:

    def __init__(self, inicio=None, fin=None):

        self.cantidad = 0
        self.raiz = None
        self.inicio = inicio
        self.fin = fin

    def cantidad(self):
        return self.cantidad

    def guardar(self, clave, dato):
        if not self.raiz:
            nodo = NODO(clave,dato)

            self.cantidad +=1
            self.raiz = nodo
            return True

        return self._insertar_nodo(self.raiz,clave,dato)

    def cmp (self, clave, raiz_clave):
        if clave < raiz_clave : return -1

        if clave > raiz_clave : return 1

        return 0

    def _insertar_nodo(self, raiz, clave, dato):
        rama = self.cmp(clave,raiz.clave)

        if rama == 0: raiz.dato = dato

        if rama < 0:

            if raiz.izq: return self._insertar_nodo(raiz.izq,clave,dato)

            nodo = NODO(clave,dato)
            raiz.izq = nodo
            self.cantidad += 1

        if rama > 0:

            if raiz.der : return self._insertar_nodo(raiz.der, clave,dato)

            nodo = NODO(clave,dato)
            raiz.der = nodo
            self.cantidad +=1

        return True


    def __iter__(self):
        return IterABB(self, self.inicio, self.fin)

class IterABB:
    """ Iterador de arboles binarios inOrder @LeonelR."""

    def __init__(self,abb, inicio=None, fin=None):
        """ Constructor """
        self.pila = []
        self.inicio = inicio
        self.fin = fin
        self.apilar(abb.raiz)

    def apilar(self,nodo):
        """ apila nodos izquierdos"""
        if not nodo: return
        #apilo
        self.pila.append(nodo)
        return self.apilar(nodo.izq)

    def next(self):
        """Avanzar(c)"""
        if self.pila == []:
            raise StopIteration

        nodo = self.pila.pop()
        elemento = nodo.clave

        #self.apilar(nodo.der)

        #apilado especial para el tp
        self.apilar_ip(nodo.der)

        return elemento

    def apilar_ip(self,nodo):
        """Apilado contruido especialmente para TP2 algo2 Fiuba @LeonelR. """
        if not nodo: return

        estaEnRango = nodo.dato >= self.inicio and nodo.dato <= self.fin

        if estaEnRango:
            #pila apilar
            self.pila.append(nodo)
            return self.apilar_ip(nodo.izq)

        if nodo.dato >= self.inicio:
            return self.apilar_ip(nodo.izq)
        else:
            return self.apilar_ip(nodo.der)


    def __next__(self):
        return self.next()

def main ():
    abb = ABB(4,20) # rango 4 -- 20

    lista = [10,7,13,5,8,6,50,12,40,47,45,44]
    lista_sort = [5,6,7,8,10,12,13]

    for i in lista:
        print(abb.guardar(i,i))

    print("pruebas \n")

    #muestra ips del 4 al 20
    for item , ok in zip(abb,lista_sort):
        print(item,item == ok)

main()
