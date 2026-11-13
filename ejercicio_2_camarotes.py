# =====================================================
#  CRUCERO ATLÁNTICO
#  Sistema de gestión de camarotes
# =====================================================

# ---------- Constantes y variables de estado ----------
CAPACIDAD_CANCELACION = 90       # máximo permitido por cancelación (según enunciado)

disponibles = 120                # stock inicial de camarotes
historial = 0                    # contador de reservas de la sesión


# ---------- Funciones auxiliares ----------
def pedir_entero(pregunta):
    """Pide un número entero (positivo, negativo o cero) hasta que sea válido."""
    dato = input(pregunta).strip().lower()
    while not (dato.lstrip("-").isdigit()):
        print("Entrada inválida. Ingresa un número entero.")
        dato = input(pregunta).strip().lower()
    return int(dato)


def mostrar_menu():
    print("\n=== MENÚ PRINCIPAL ===")
    print("1.- Camarotes disponibles.")
    print("2.- Reservar camarote.")
    print("3.- Cancelar camarote.")
    print("4.- Historial de reservas.")
    print("5.- Salir.")


# ---------- Programa principal ----------
print("¡Bienvenido al sistema de gestión de camarotes del Crucero Atlántico!")

opcion = ""
while opcion != "5":
    mostrar_menu()
    opcion = input("Seleccione una opción: ").strip().lower()

    # 1.- Camarotes disponibles
    if opcion == "1":
        print(f"Camarotes disponibles: {disponibles}")

    # 2.- Reservar camarote
    elif opcion == "2":
        cantidad = pedir_entero("¿Cuántos camarotes desea reservar? ")
        if cantidad <= 0:
            print("La cantidad debe ser mayor a 0.")
        elif cantidad > disponibles:
            print(f"No hay suficientes camarotes. Solo quedan {disponibles} disponibles.")
        else:
            disponibles -= cantidad
            historial += cantidad
            print(f"Reserva exitosa: {cantidad} camarote(s). Quedan {disponibles} disponibles.")

    # 3.- Cancelar camarote
    elif opcion == "3":
        cantidad = pedir_entero("¿Cuántos camarotes desea cancelar? ")
        if cantidad <= 0:
            print("La cantidad debe ser mayor a 0.")
        elif cantidad > CAPACIDAD_CANCELACION:
            print(f"No puede superar la capacidad máxima del crucero ({CAPACIDAD_CANCELACION} camarotes).")
        elif cantidad > historial:
            print(f"Solo hay {historial} camarote(s) reservados en esta sesión para cancelar.")
        else:
            disponibles += cantidad
            historial -= cantidad
            print(f"Cancelación exitosa: {cantidad} camarote(s) liberados. Disponibles: {disponibles}.")

    # 4.- Historial de reservas
    elif opcion == "4":
        print(f"Total de reservas realizadas en la sesión: {historial}")

    # 5.- Salir
    elif opcion == "5":
        print("Gracias por utilizar nuestro software, hasta la próxima.")

    else:
        print("Opción inválida. Elige un número del 1 al 5.")
