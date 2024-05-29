import os
import time
import random
import msvcrt

pausa = False

class Proceso:
    def __init__(self, id, numero1, numero2, operacion, resultado_operacion, tiempo_total, tiempo_maximo, tiempo_restante, tiempofaltante, cadena_operacion, BanderaError, tiempo_bloqueado, tiempo_llegada, tiempo_finalizacion, tiempo_retorno, tiempo_respuesta, tiempo_espera, tiempo_servicio, tiempo_transcurrido):
        self.id = id
        self.numero1 = numero1
        self.numero2 = numero2
        self.operacion = operacion
        self.resultado_operacion = resultado_operacion
        self.tiempo_total = tiempo_total
        self.tiempo_maximo = tiempo_maximo
        self.tiempo_restante = tiempo_restante
        self.tiempofaltante = tiempofaltante
        self.cadena_operacion = cadena_operacion
        self.BanderaError = BanderaError
        self.tiempo_bloqueado = tiempo_bloqueado
        self.tiempo_llegada = tiempo_llegada
        self.tiempo_finalizacion = tiempo_finalizacion
        self.tiempo_retorno = tiempo_retorno
        self.tiempo_respuesta = tiempo_respuesta
        self.tiempo_espera = tiempo_espera
        self.tiempo_servicio = tiempo_servicio
        self.tiempo_transcurrido = tiempo_transcurrido
        
#Estas son nuestras listas
#lista de procesos
lista = []
#lista de procesos nuevos
lista_nuevo = []
#lista de procesos finalizados
lista_finalizados = []
#lista de procesos bloqueados
lista_bloqueados = []
#Este es el que dara los id
lista_id=[]

def main():
    global pausa
    contador = 0
    quantum = 0
    qua = 1
    ban = -1
    # Crearemos nuestras listas

    # Ingresar cantidad de procesos
    while True:
        dato = input("Ingrese procesos a realizar: ")
        if dato.isdigit():
            cantidad = int(dato)
            break
        else:
            print("INGRESA UN DIGITO")
            # Ingresar cantidad de procesos
    while True:
        dato = input("Ingresa el quantum: ")
        if dato.isdigit():
            if int(dato) >0 and int(dato)<18:
                quantum = int(dato)
                break
            else:
                print("Ingresa un valor dentro del rango")
        else:
            print("INGRESA UN DIGITO")
    #Creamos un for para separar la funcion y llenar los campos
    ids =0
    for x in range(cantidad):
        ids+=1
        agregar_procesos(ids)

    # por cada objeto en tu lista que se repreenta como un guion bajo vas a impirmir las caracteristicas de la lista
    for _ in lista:
        proc = len(lista)
        cont = 1
        while proc >= cont:
            _.tiempo_bloqueado = 0
            if _.tiempo_restante==-1:
                _.tiempo_restante=0
            while _.tiempo_restante >= 0 or len(lista_bloqueados) == 0:
                if _.tiempo_respuesta == -1:
                    _.tiempo_respuesta = contador - _.tiempo_llegada
                

                
                # aqui se diviran en 5 constantemente mientras lista sea menor a 5 entrara en un ciclo que agregara los procesos nuevos
                if len(lista) < 5:
                    while True:
                        # usando dos listas y una variable para guardar el primero de la lista funciona
                        if lista_nuevo:
                            if len(lista_bloqueados) + len(lista) == 5:
                                break
                            nuevos = lista_nuevo[0]
                            nuevos.tiempo_llegada = contador  # Captura el tiempo de llegada
                            lista.append(nuevos)
                            lista_nuevo.remove(nuevos)
                            if len(lista) == 5:
                                break
                        else:
                            break
                #limpia de pantalla
                os.system("cls")

                # Seccion de Pausa Error y Interumpcion
                if msvcrt.kbhit():
                    tecla = msvcrt.getch().decode()
                    if tecla == 'p':
                        pausa = True
                    if tecla == 'e':
                        _.BanderaError = True
                        _.resultado_operacion = "ERROR"
                        error = _.tiempo_restante
                        _.tiempo_restante = 1
                        qua=0
                    if tecla == 'i' and lista:
                        # Este if es solo una limitacion para la cantidad de procesos en lista bloqueados
                        if len(lista_bloqueados) >= 5:
                            break
                        else:
                            qua=0
                            obj = lista[0]
                            lista_bloqueados.append(obj)
                            lista.remove(obj)
                            break
                       

                    if tecla == 'n':
                        ids+=1
                        agregar_procesos_nuevos(ids)
                    
                    if tecla =='b':
                        conta=contador
                        tabla_procesos(conta)
                        pausa = True
                        if pausa:
                            print("Presione 'c' para continuar.")
                            while pausa:
                                if msvcrt.kbhit():
                                    tecla = msvcrt.getch().decode()
                                    if tecla == 'c':
                                        pausa = False
                                        print("Programa reanudado.")
                                        break
                        
                        


                # Se impren la cantidad de procesos nuevos
                print("--------------------------------------------------")
                print("CANTIDAD DE PROCESOS NUEVOS")
                print(len(lista_nuevo))
                print("--------------------------------------------------")

                # Se imprimira los procesos pendientes
                print("Cola de Procesos Listos")
                for _ in lista[1:]:
                    print(f"ID: {_.id}, TM: {_.tiempo_maximo}, TR: {_.tiempo_transcurrido}", end=' |\n')
                print("--------------------------------------------------")

                # Impresion de contador
                print(f"Tiempo Transcurrido: {contador} Quantum: {qua} Quantum definido: {quantum}" )
                print("--------------------------------------------------")

                # Se imprimira los procesos en ejecución
                print("Proceso en Ejecución")
                for _ in lista[:1]:
                    print(f"ID: {_.id} Estimado: {_.tiempo_maximo} Restante {_.tiempo_restante} Transcurrido: {_.tiempo_transcurrido}")
                print("--------------------------------------------------")
                # Crearemos un for para nuestra lista de bloqueados con una variable nueva que es el tiempo bloqueado
                print("Procesos Bloqueados")
                for x in lista_bloqueados:
                    print(f"ID: {x.id} Bloqueado: {x.tiempo_bloqueado}")
                print("--------------------------------------------------")
                # Crearemos un for para otra lista donde aparecerán los que ya se han finalizado
                print("Procesos Terminados")
                for x in lista_finalizados:
                    print(f"ID: {x.id} Resultado {x.resultado_operacion}\n Estimado: {x.tiempo_maximo} Llegada: {x.tiempo_llegada} Finalizado: {x.tiempo_finalizacion} Retorno: {x.tiempo_retorno} Respuesta: {x.tiempo_respuesta} Espera: {x.tiempo_espera} Servicio: {x.tiempo_servicio}\n")

                print("--------------------------------------------------")
                # Utilizamos la parte del código anterior que teníamos para agregar la pausa
                if pausa:
                    print("Presione 'c' para continuar.")
                    while pausa:
                        if msvcrt.kbhit():
                            tecla = msvcrt.getch().decode()
                            if tecla == 'c':
                                pausa = False
                                print("Programa reanudado.")
                                break
                #Aqui agregamos la seccion del algoritmo con quantum
                if qua>=quantum and len(lista)>0:
                    qua=0
                    quantu=lista[0]
                    lista.append(quantu)
                    lista.remove(quantu)

                # Eliminamos una unidad del tiempo restante
                if len(lista) > 0:
                    _.tiempo_restante -= 1
                    _.tiempo_transcurrido += 1

                # Contador para lista de bloqueados
                if lista_bloqueados:
                    for x in lista_bloqueados:
                        x.tiempo_bloqueado += 1
                        if x.tiempo_bloqueado > 8:
                            x.tiempo_bloqueado = 0
                            bloqueado = lista_bloqueados[0]
                            lista.append(bloqueado)
                            lista_bloqueados.remove(bloqueado)
                            break
                # Aquí rompemos el ciclo
                if len(lista_bloqueados) == 0 and len(lista) == 0 and _.tiempo_restante == 0:
                    break
                # Cuando tiempo restante llega a cero sucede
                if (_.tiempo_restante <= 0 or _.tiempo_transcurrido ==_.tiempo_maximo) and len(lista)>0:
                    # En esta parte usamos bj para marcar la primera posición de la lista y así usarla tanto para moverla como quitarla
                    bj = lista[0]
                    qua=0
                    bj.tiempo_finalizacion = contador + 1
                    bj.tiempo_retorno = bj.tiempo_finalizacion - bj.tiempo_llegada
                    bj.tiempo_servicio =  bj.tiempo_transcurrido
                    bj.tiempo_espera = bj.tiempo_retorno - bj.tiempo_servicio
                    
                    lista_finalizados.append(bj)
                    lista.remove(bj)
                    cont += 1
                    
                if len(lista)!=0:
                    qua += 1
                    
                contador += 1
                time.sleep(1)
                os.system("cls")

def agregar_procesos(ids):
        id = ids
        # Ingreso de numero1
        numero1 = random.randint(-100, 100)
        # Ingreso de numero2
        numero2 = random.randint(1, 100)
        # Creamos un if con una opcion que tenga numeros aletorios del 1 a 6 para escoger que operacion se hara
        opcion = random.randint(1, 6)
        # Si nuestra opcion da 1 le dara a operacion el signo + y resultado la suma de numero1 y numero2
        if opcion == 1:
            operacion = '+'
            resultado_operacion = numero1 + numero2
        # Si nuestra opcion da 2 le dara a operacion el signo - y resultado la resta de numero1 y numero2
        elif opcion == 2:
            operacion = '-'
            resultado_operacion = numero1 - numero2
        # Si nuestra opcion da 3 le dara a operacion el signo * y resultado la multiplicacion de numero1 y numero2
        elif opcion == 3:
            operacion = '*'
            resultado_operacion = numero1 * numero2
        # Si nuestra opcion da 4 le dara a operacion el signo / y resultado la division de numero1 y numero2
        elif opcion == 4:
            operacion = '/'
            resultado_operacion = numero1 / numero2
        # Si nuestra opcion da 5 le dara a operacion el signo % y resultado del porcentaje de numero1 y numero2
        elif opcion == 5:
            operacion = '%'
            resultado_operacion = numero1 % numero2
        # aqui necesito tu ayuda roberto
        elif opcion == 6:
            operacion = '+'
            resultado_operacion = numero1 + numero2
        # Aqui desginamos el tiempo maximo
        tiempo_maximo = random.randint(8, 16)

        # Ingresamos los demas datos de nuestra clase
        tiempo_total = 0
        tiempo_restante = tiempo_maximo
        tiempofaltante = 0
        cadena_operacion = ""
        BanderaError = False
        tiempo_bloqueado = 0
        tiempo_llegada = 0
        tiempo_finalizacion = 0
        tiempo_retorno = 0
        tiempo_respuesta = -1
        tiempo_espera = -1
        tiempo_servicio = 0
        tiempo_transcurrido = 0
        quieromorir = Proceso(id, numero1, numero2, operacion, resultado_operacion, tiempo_total, tiempo_maximo, tiempo_restante, tiempofaltante, cadena_operacion, BanderaError, tiempo_bloqueado, tiempo_llegada, tiempo_finalizacion, tiempo_retorno, tiempo_respuesta, tiempo_espera, tiempo_servicio, tiempo_transcurrido)
        lista.append(quieromorir)

def agregar_procesos_nuevos(ids):
        id = ids
        # Ingreso de numero1
        numero1 = random.randint(-100, 100)
        # Ingreso de numero2
        numero2 = random.randint(1, 100)
        # Creamos un if con una opcion que tenga numeros aletorios del 1 a 6 para escoger que operacion se hara
        opcion = random.randint(1, 6)
        # Si nuestra opcion da 1 le dara a operacion el signo + y resultado la suma de numero1 y numero2
        if opcion == 1:
            operacion = '+'
            resultado_operacion = numero1 + numero2
        # Si nuestra opcion da 2 le dara a operacion el signo - y resultado la resta de numero1 y numero2
        elif opcion == 2:
            operacion = '-'
            resultado_operacion = numero1 - numero2
        # Si nuestra opcion da 3 le dara a operacion el signo * y resultado la multiplicacion de numero1 y numero2
        elif opcion == 3:
            operacion = '*'
            resultado_operacion = numero1 * numero2
        # Si nuestra opcion da 4 le dara a operacion el signo / y resultado la division de numero1 y numero2
        elif opcion == 4:
            operacion = '/'
            resultado_operacion = numero1 / numero2
        # Si nuestra opcion da 5 le dara a operacion el signo % y resultado del porcentaje de numero1 y numero2
        elif opcion == 5:
            operacion = '%'
            resultado_operacion = numero1 % numero2
        # aqui necesito tu ayuda roberto
        elif opcion == 6:
            operacion = '+'
            resultado_operacion = numero1 + numero2
        # Aqui desginamos el tiempo maximo
        tiempo_maximo = random.randint(8, 16)

        # Ingresamos los demas datos de nuestra clase
        tiempo_total = 0
        tiempo_restante = tiempo_maximo
        tiempofaltante = 0
        cadena_operacion = ""
        BanderaError = False
        tiempo_bloqueado = 0
        tiempo_llegada = 0
        tiempo_finalizacion = 0
        tiempo_retorno = 0
        tiempo_respuesta = -1
        tiempo_espera = -1
        tiempo_servicio = 0
        tiempo_transcurrido = 0
        quieromorir = Proceso(id, numero1, numero2, operacion, resultado_operacion, tiempo_total, tiempo_maximo, tiempo_restante, tiempofaltante, cadena_operacion, BanderaError, tiempo_bloqueado, tiempo_llegada, tiempo_finalizacion, tiempo_retorno, tiempo_respuesta, tiempo_espera, tiempo_servicio, tiempo_transcurrido)
        lista_nuevo.append(quieromorir)


#Aqui podremos poner pausa y marcar el sistema de pausa        
def tabla_procesos(conta):
    os.system("cls")

    print("PROCESOS NUEVOS")
    for x in lista_nuevo:
        print(f"ID: {x.id} Operacion: {x.numero1} {x.operacion} {x.numero2}")
    print("--------------------------------------------------")
    print(f"----TIEMPO: {conta}----")
    print("-------------PROCESOS LISTOS---------------------")
    for x in lista[1:]:
        if x.tiempo_espera==-1:
            x.tiempo_espera =  conta - x.tiempo_llegada-x.tiempo_transcurrido
        print(f"ID:{x.id} Operacion: {x.numero1} {x.operacion} {x.numero2} Llegada: {x.tiempo_llegada} Espera: {x.tiempo_espera} Servicio: {x.tiempo_transcurrido}")
        if x.tiempo_respuesta>=0:
            print(f"Respuesta: {x.tiempo_respuesta}")
    print("-----------Proceso en ejecucion-----------")
    for x in lista[0:1]:
        if x.tiempo_espera==-1:
            x.tiempo_espera =  conta - x.tiempo_llegada-x.tiempo_transcurrido
        print(f"ID:{x.id} Operacion: {x.numero1} {x.operacion} {x.numero2} Llegada: {x.tiempo_llegada} Espera: {x.tiempo_espera} Servicio: {x.tiempo_transcurrido} Respuesta:{x.tiempo_respuesta}")
    print("-----------PROCESOS FINALIZADOS----------------------")            
    for x in lista_finalizados:
            print(f"ID:{x.id} Operacion: {x.numero1} {x.operacion} {x.numero2}={x.resultado_operacion} \n Estimado: {x.tiempo_maximo} Llegada: {x.tiempo_llegada} Finalizado: {x.tiempo_finalizacion} Retorno: {x.tiempo_retorno} Respuesta: {x.tiempo_respuesta} Espera: {x.tiempo_espera} Servicio: {x.tiempo_servicio}")
    print("------------Procesos Bloqueados-------------------")
    for x in lista_bloqueados:
        x.tiempo_espera =  conta - x.tiempo_llegada-x.tiempo_transcurrido
        print(f"ID: {x.id} Bloqueado: {x.tiempo_bloqueado} Restante: {8-x.tiempo_bloqueado} Llegada: {x.tiempo_llegada} Espera: {x.tiempo_espera} Servicio: {x.tiempo_transcurrido} Respuesta:{x.tiempo_respuesta}")
    print("--------------------------------------------------")



if __name__ == "__main__":
    os.system("cls")
    main()