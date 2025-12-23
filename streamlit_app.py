import streamlit as st
import datetime

# Configuración de estilo
st.set_page_config(page_title="Agenda Peluquería ⚡", layout="centered")

st.title("💈 Gestión de Turnos")

# Función para generar los horarios de 17:00 a 22:00 (cada 40 min)
def generar_horarios():
    lista = []
    actual = datetime.datetime.strptime("17:00", "%H:%M")
    fin = datetime.datetime.strptime("22:00", "%H:%M")
    while actual <= fin:
        lista.append(actual.strftime("%H:%M"))
        actual += datetime.timedelta(minutes=40)
    return lista

# Guardar datos en la sesión (para que no se borren al tocar botones)
if 'agenda' not in st.session_state:
    st.session_state.agenda = {}

horarios = generar_horarios()

# --- FORMULARIO PARA AGENDAR ---
with st.expander("➕ Agendar Cliente Nuevo", expanded=True):
    with st.form("registro"):
        nombre = st.text_input("Nombre del Cliente")
        telefono = st.text_input("WhatsApp (ej: 549381...)")
        hora = st.selectbox("Elegí el horario", horarios)
        boton = st.form_submit_button("Confirmar Turno ✅")
        
        if boton and nombre and telefono:
            st.session_state.agenda[hora] = {"nombre": nombre, "tel": telefono}
            st.success(f"¡Turno guardado para {nombre}!")

# --- VISTA DE LA AGENDA ---
st.subheader("📋 Turnos de Hoy")
for h in horarios:
    col1, col2 = st.columns([1, 3])
    col1.write(f"**{h}**")
    
    if h in st.session_state.agenda:
        cliente = st.session_state.agenda[h]
        # Crear mensaje para WhatsApp
        msg = f"Hola {cliente['nombre']}, confirmo tu turno para las {h}. Recordá los 10 min de tolerancia. ¡Te esperamos!"
        link_wa = f"https://wa.me/{cliente['tel']}?text={msg.replace(' ', '%20')}"
        
        col2.markdown(f"👤 {cliente['nombre']}  -  [📲 Avisar]({link_wa})")
    else:
        col2.write("🟢 *Libre*")

if st.button("Limpiar Agenda 🗑️"):
    st.session_state.agenda = {}
    st.rerun()
   
