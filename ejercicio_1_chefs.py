# =====================================================
#  ESCUELA INTERNACIONAL DE GASTRONOMÍA
#  Registro de chefs recién incorporados
# =====================================================

# ---------- Constantes ----------
LARGO_MINIMO_CODIGO = 8
EXPERIENCIA_MAESTRO = 5          # más de 5 años -> Chef Maestro

MSG_ERROR_CANTIDAD = "¡Ingrediente inválido! Ingresa un entero positivo para continuar el registro."
MSG_ERROR_EXPERIENCIA = "¡Error gastronómico! Ingresa un número entero positivo para la experiencia culinaria."
MSG_ERROR_CODIGO = "¡Código inválido! Debe tener al menos 8 caracteres y no incluir espacios."


# ---------- Funciones de validación ----------
def es_entero_positivo(texto):
    """True si el texto es un número entero mayor que 0."""
    return texto.isdigit() and int(texto) > 0


def pedir_entero_positivo(pregunta, mensaje_error):
    """Pide un dato hasta que sea un entero positivo."""
    dato = input(pregunta).strip().lower()
    while not es_entero_positivo(dato):
        print(mensaje_error)
        dato = input(pregunta).strip().lower()
    return int(dato)


def pedir_codigo():
    """Pide el código culinario: mínimo 8 caracteres y sin espacios."""
    codigo = input("  Código culinario: ").strip().lower()
    while len(codigo) < LARGO_MINIMO_CODIGO or " " in codigo:
        print(MSG_ERROR_CODIGO)
        codigo = input("  Código culinario: ").strip().lower()
    return codigo


# ---------- Programa principal ----------
print("=" * 55)
print("   ESCUELA INTERNACIONAL DE GASTRONOMÍA")
print("   Registro de chefs recién incorporados")
print("=" * 55)

cantidad_chefs = pedir_entero_positivo("¿Cuántos chefs desea registrar? ", MSG_ERROR_CANTIDAD)

total_maestros = 0
total_aprendices = 0

for numero in range(1, cantidad_chefs + 1):
    print(f"\n--- Chef {numero} de {cantidad_chefs} ---")

    codigo = pedir_codigo()
    experiencia = pedir_entero_positivo("  Experiencia culinaria (años): ", MSG_ERROR_EXPERIENCIA)

    if experiencia > EXPERIENCIA_MAESTRO:
        categoria = "Chef Maestro"
        total_maestros += 1
    else:
        categoria = "Chef Aprendiz"
        total_aprendices += 1

    print(f"  ✔ {codigo.upper()} registrado como {categoria}.")

# ---------- Resumen final ----------
print("\n" + "=" * 55)
print("   RESUMEN DE REGISTRO")
print("=" * 55)
print(f"Total de chefs registrados: {cantidad_chefs}")
print(f"Chefs Maestros:  {total_maestros}")
print(f"Chefs Aprendices: {total_aprendices}")
print(f"\n¡La escuela cuenta con {total_maestros} Chefs Maestros y {total_aprendices} Chefs Aprendices! ¡A cocinar!")
