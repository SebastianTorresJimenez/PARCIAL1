import timeit
import time
import random
import statistics

class menu():
    ''' Menu principal y se toma como padre el menu principal del programa'''
    def __init__(self):
        self.lista=[]
        
    @staticmethod
    def imprimir_menu():
        print("Menú: \n 1. Generar lista aleatoria\n 2. Ingresar lista manualmente\n 3. Usar lista previamente cargada\n 4. Crear lista desde rango\n 5. Ayuda\n 6. Salir ")
class numero_aleatorio(menu):
    def __init__(self):
        print("Submenú: \n a.Imprimir lista\n b. Ordenamiento por burbuja\n c. ordenamiento rápido\n d. comparar con sorted()\n e. buscar elemento(busqueda lineal)\n g. sumar elementos\n h. Calcular promedio\n i. Calcular mediana\n j. Calcular varianza\n o. regresar al menú principal")   

    def imprimir_lista(self, mensaje):
        self.mensaje=mensaje
        return self.mensaje
    
class ordenamiento_burbuja(menu):
    def __init__(self,lista_burbuja):
        self.lista_burbuja=lista_burbuja
    
    def ordenar(self):
        n = len(self.lista_burbuja) # Iterar a través de todos los elementos de la lista
        for i in range(n):# Últimos i elementos ya están en su lugar correcto
            for j in range(0, n-i-1):# Intercambiar si el elemento encontrado es mayor que el siguiente elemento
                if self.lista_burbuja[j] > self.lista_burbuja[j+1]:
                    self.lista_burbuja[j], self.lista_burbuja[j+1] = self.lista_burbuja[j+1], self.lista_burbuja[j]

class ordenamiento_rapido:
    def __init__(self, lista_generada):
        self.lista_generada=lista_generada
    
    def __sort__(self, lista_generada=None):
        if lista_generada is None:
            lista_generada = self.lista_generada
        if len(lista_generada) <= 1:
            return lista_generada
        else:
            pivote = lista_generada[0]
            menores = [x for x in lista_generada[1:] if x <= pivote]
            mayores = [x for x in lista_generada[1:] if x > pivote]
            return self.__sort__(menores) + [pivote] + self.__sort__(mayores)

    def ordenar(self):
        self.lista_generada = self.__sort__(self.lista_generada)

class comparar_tiempos:
    def __init__(self,lista1, lista2, lista3):
        self.lista1=lista1
        self.lista2=lista2
        self.lista3=lista3
    def ordenar_sorted(self):
        lista_ordenada=sorted(self.lista3)
        return lista_ordenada
    def comparar(self,tiempo):
        self.tiempo=tiempo
        tiempo_transcurrido = self.lista1
        tiempo_transcurrido1 = self.lista2
        tiempo_transcurrido2 = self.tiempo

        print(f"\nTiempo de ordenar para burbuja: {tiempo_transcurrido} segundos")
        print(f"Tiempo de ordenar para ordenamiento rápido: {tiempo_transcurrido1} segundos")
        print(f"Tiempo de ordenar para sorted(): {tiempo_transcurrido2} segundos\n")

class buscar_elemento:
    def __init__(self,elemento,lista):
        self.elemento=elemento
        self.lista=lista
    def busqueda(self):
        for i, valor in enumerate(self.lista):
            if self.elemento==valor:
                return i
        return -1
    
class estadistica:
    def __init__(self, lista):
        self.lista=lista
    def sumatoria_lista(self):
        return sum(self.lista)
class promedio(estadistica):
    def __init__(self, lista, promedio_total):
        super().__init__(lista)
        self.promedio_total=promedio_total
    
    def promedio_total(self):
        return self.promedio_total

class mediana(estadistica):
    def __init__(self, lista, mediana_total):
        super().__init__(lista)
        self.mediana_total=mediana_total
    def mediana_total(self):
        return self.mediana_total
    
class varianza(estadistica):
    def __init__(self, lista, varianza_total):
        super().__init__(lista)
        self.varianza_total=varianza_total
    def varianza_total(self):
        return self.varianza_total
    
def main():
    menu_principal=menu()
    while(True):
        menu_principal.imprimir_menu()
        try:
            opcion_elegida = int(input(f"Elige una opción: "))
            if opcion_elegida==1:
                tamaño_lista=int(input("ingrese el tamaño de la lista: "))
                lista_generada=[random.randint(0, 100000) for _ in range(tamaño_lista)]
                print(f"lista generada (primeros 10 elementos)= {lista_generada[:10]}\n")
                while(True):
                    sub_menu=numero_aleatorio()
                    opcion_elegida1 = input(f"Elige una opción: ")
                    try:
                        entero=str(opcion_elegida1)            
                        if entero == 'a':
                            imprimir=sub_menu.imprimir_lista(lista_generada)
                            print(f'la lista completa es= {imprimir}\n')
                            time.sleep(2)
                        elif entero == 'b':
                            inicio=time.time()
                            orden=ordenamiento_burbuja(lista_generada)
                            orden.ordenar()
                            final=time.time()
                            tiempo_ejecucion=final-inicio
                            print(f'\nlista ordenada: {orden.lista_burbuja[:10]}')
                            print(f'tiempo de ejecución para burbuja fue {tiempo_ejecucion} segundos\n')
                            time.sleep(2)
                        elif entero=='c':
                            inicio=time.time()
                            sort=ordenamiento_rapido(lista_generada)
                            sort.ordenar()
                            final=time.time()
                            tiempo_ejecucion1=final-inicio
                            print(f'\nlista ordenada: {sort.lista_generada[:10]}')
                            print(f'tiempo de ejecución para burbuja fue {tiempo_ejecucion1} segundos\n')
                            time.sleep(2)
                        elif entero=='d':
                            comparador=comparar_tiempos(tiempo_ejecucion,tiempo_ejecucion1,lista_generada)
                            inicio=time.time()
                            comparador.ordenar_sorted()
                            final=time.time()
                            tiempo_ejecucion2=final-inicio
                            comparador.comparar(tiempo_ejecucion2)
                        elif entero=='e':
                            elemento=int(input("Ingrese el elemento a buscar: "))
                            buscar=buscar_elemento(elemento,lista_generada)
                            buscar.busqueda()
                            # Mostrar el resultado
                            if buscar != -1:
                                print(f"El valor {elemento} se encuentra en la posición {buscar.busqueda()}.")
                            else:
                                print(f"El valor {elemento} no se encuentra en la lista.")
                        elif entero=='g':
                            lista=estadistica(lista_generada)
                            print(f"la sumatoria de toda la lista es: {lista.sumatoria_lista()}\n")
                            time.sleep(2)
                        elif entero=='h':
                            promedio_total1=statistics.mean(lista_generada)
                            total=promedio(lista_generada,promedio_total1)
                            print(f"el promedio de toda la lista: {total.promedio_total}\n")
                            time.sleep(2)
                        elif entero=='i':
                            mediana1=statistics.median(lista_generada)
                            total1=mediana(lista_generada,mediana1)
                            print(f"la mediana de la lista: {total1.mediana_total}\n")
                            time.sleep(2)
                        elif entero=='j':
                            varianza1=statistics.variance(lista_generada)
                            total2=varianza(lista_generada,varianza1)
                            print(f"la varianza de la lista: {float(total2.varianza_total)}\n")
                            time.sleep(2)
                        elif entero=='o':
                            break
                        else:
                            raise ValueError("Opción no válida. Por favor, selecciona una opción válida.")    
                    except ValueError as mensaje: 
                        print(mensaje)
                        time.sleep(2)
            else:
                print("ingrese una opción valida")
                time.sleep(2)
        except ValueError:
            print("\nDebe ingresar un número entero!\n")
            time.sleep(2)


if __name__=='__main__':
    main()