import time
import keyboard

while True:
    # Obtener el tiempo de entrada del usuario
    tiempo_total = int(input("Ingresa el tiempo en segundos: "))

    # Esperar hasta que el tiempo se agote o el usuario presione Enter
    while tiempo_total:
        # Calcular el tiempo restante
        tiempo_restante = time.strftime("%M:%S", time.gmtime(tiempo_total))
        
        # Imprimir el tiempo restante en la consola
        print(tiempo_restante, end="\r")
        
        # Esperar un segundo
        time.sleep(1)
        
        # Restar un segundo del tiempo total
        tiempo_total -= 1
        
        # Verificar si el usuario ha presionado Enter
        if keyboard.is_pressed('enter'):
            print("Temporizador detenido!")
            break
        if keyboard.is_pressed('m'):
            tiempo_total=tiempo_total+60

    # Cuando el tiempo se agote, mostrar un mensaje y preguntar si desea continuar
    print("Tiempo terminado!")
    respuesta = input("¿Desea continuar? (s/n) ")
    if respuesta.lower() != 's':
        break
