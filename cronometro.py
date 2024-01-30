import time
menu=int(input("1-Timer\n2-Cronometro\nQue Opcion deseas: "))
# Preguntar al usuario cuánto tiempo desea cronometrar
bandera=0
while True:

    if menu==1:
        # Obtener el tiempo de entrada del usuario
        tiempo_total = int(input("Ingresa el tiempo en segundos: "))

        # Esperar hasta que el tiempo se agote
        while tiempo_total:
        # Calcular el tiempo restante
            tiempo_restante = time.strftime("%H:%M:%S", time.gmtime(tiempo_total))
        
        # Imprimir el tiempo restante en la consola
            print(tiempo_restante, end="\r")
        
        # Esperar un segundo
            time.sleep(1)
        
        # Restar un segundo del tiempo total
            tiempo_total -= 1
            
            if tiempo_restante==0:
                bandera=0
                break
            

    # Cuando el tiempo se agote, mostrar un mensaje
        print("Tiempo terminado!")

    if menu==2:
        print("Cronometro seleccionado")
        tiempo_total = int(input("¿Cuántos segundos  quieres cronometrar? "))
        tiempo_total=tiempo_total
        print(tiempo_total, "segundos")

        # Iniciar el cronómetro
        inicio = time.time()

        # Ciclo mientras el tiempo no ha terminado
        while (time.time() - inicio) < tiempo_total:
            # Calcular el tiempo transcurrido
            tiempo_transcurrido = time.time() - inicio
            
            # Convertir tiempo transcurrido a formato hh:mm:ss
            tiempo_formateado = time.strftime("%H:%M:%S", time.gmtime(tiempo_transcurrido))
            
            # Imprimir el tiempo transcurrido en la consola
            print(tiempo_formateado, end="\r")
            time.sleep(1)
            
            if inicio==0:
                bandera=0
                break
                

