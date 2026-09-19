#-----------------Entrada cajero-----------------
def cajero(monto_a_retirar, fondos_disponibles, historial_retiros_dia):
    if monto_a_retirar % 50 != 0:
        return "Monto no válido"

    if monto_a_retirar > fondos_disponibles:
        return "Saldo insuficiente"

    total_retiros_dia = historial_retiros_dia + monto_a_retirar

    if total_retiros_dia > 6000:
        return "Límite excedido"
    
    fondos_disponibles -= monto_a_retirar
    return f"ENTREGADO. Nuevo saldo disponible: {fondos_disponibles}"

monto = float(input("Cantidad a retirar: "))
fondos = float(input("Fondos disponibles: "))
historial = float(input("Historial de retiros del día: "))

resultado = cajero(monto, fondos, historial)
print(resultado)