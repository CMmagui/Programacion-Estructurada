#-----------Nip Cajero-------------------
PIN_correcto = "1234"

intentos = 0
acertado = False

while intentos < 3 and acertado == False:
    intentos = intentos + 1
    PIN_ingresado = input(f"Intento {intentos} de 3 - Ingrese su PIN: ")
    
    if PIN_ingresado == PIN_correcto:
        acertado = True
    else:
        print("PIN incorrecto.")


if acertado:
    mensaje = "ACCEDIDO"
else:
    mensaje = "DENEGADO"

print(mensaje)