import datetime

def generar_horarios_base():
    # Genera turnos de 40 min desde las 17:00 hasta las 22:00
    horarios = []
    inicio = datetime.datetime.strptime("17:00", "%H:%M")
    fin = datetime.datetime.strptime("22:00", "%H:%M")
    
    actual = inicio
    while actual <= fin:
        horarios.append(actual.strftime("%H:%M"))
        actual += datetime.timedelta(minutes=40)
    return horarios

# Iniciamos la lista con los turnos de 40 min
horarios_laborales = generar_horarios_base()
agenda = {}

def mostrar_agenda():
    print("\n--- 💈 ESTADO DE LA AGENDA (Tolerancia 10 min) ---")
    # Ordenamos los horarios para que se vean correlativos
    for hora in sorted(horarios_laborales):
        if hora not in agenda:
            print(f" {hora} [ LIBRE ]")
        else:
            print(f" {hora} [ OCUPADO ] - Cliente: {agenda[hora]}")

def agendar_cliente():
    nombre = input("Nombre del cliente: ")
    print("Horarios sugeridos:", horarios_laborales)
    hora = input("Ingrese la hora (HH:MM): ")
    
    # Si la hora no existe en la lista base, la agregamos manualmente
    if hora not in horarios_laborales:
        confirmar = input(f"La hora {hora} no es un turno estándar. ¿Desea agregarla manualmente? (s/n): ")
        if confirmar.lower() == 's':
            horarios_laborales.append(hora)
        else:
            print("Operación cancelada.")
            return

    if hora not in agenda:
        agenda[hora] = nombre
        # Cálculo de tolerancia para el recordatorio
        h, m = map(int, hora.split(':'))
        limite = f"{h}:{m+10:02d}"
        print(f"✅ Guardado: {nombre} a las {hora}. (Tolerancia hasta {limite})")
    else:
        print(f"❌ Error: El horario {hora} ya está ocupado.")

# --- MENÚ PRINCIPAL ---
while True:
    print("\n1. Ver Agenda y Libres\n2. Agendar Turno\n3. Salir")
    opc = input("Seleccione: ")
    
    if opc == "1":
        mostrar_agenda()
    elif opc == "2":
        agendar_cliente()
    elif opc == "3":
        break