import streamlit as st

st.set_page_config(page_title="Cálculo de Entradas", layout="centered")

st.title("🎟️ Taquilla de Espectáculo")
st.write("Máximo 4 entradas por persona.")

# Configuración de precios
PRECIO_BASE = 100.0  # Puedes cambiar el precio base aquí

# Entrada de datos
cantidad = st.number_input("¿Cuántas entradas deseas comprar?", min_value=1, max_value=4, value=1)
precio_total_sin_desc = cantidad * PRECIO_BASE

# Lógica de descuentos
descuento = 0
if cantidad == 2:
    descuento = 0.10
elif cantidad == 3:
    descuento = 0.15
elif cantidad == 4:
    descuento = 0.20

pago_final = precio_total_sin_desc * (1 - descuento)

if st.button("Calcular Total"):
    if descuento > 0:
        st.subheader(f"Pago Final: {pago_final} €")
        st.write(f"(Se ha aplicado un {int(descuento*100)}% de descuento)")
    else:
        st.subheader(f"Pago Final: {pago_final} €")
        st.write("(Sin descuento para 1 entrada)")

# Diagrama de flujo dinámico
with st.expander("Ver Diagrama de Flujo del proceso"):
    # Marcas dinámicas según la elección
    c1 = " <--- SELECCIONADO" if cantidad == 1 else ""
    c2 = " <--- SELECCIONADO" if cantidad == 2 else ""
    c3 = " <--- SELECCIONADO" if cantidad == 3 else ""
    c4 = " <--- SELECCIONADO" if cantidad == 4 else ""
    
    st.code(f"""
          [ INICIO ]
              |
      +-------V-------+
      | Leer Cantidad | ({cantidad})
      +-------+-------+
              |
      ________V________
     |                 |
¿Cant == 2? --(SÍ)--> [ Dto 10% ] {c2}
     | (NO)            |
¿Cant == 3? --(SÍ)--> [ Dto 15% ] {c3}
     | (NO)            |
¿Cant == 4? --(SÍ)--> [ Dto 20% ] {c4}
     | (NO)            |
[ Sin Dto ] {c1}       |
     |                 |
     +--------+--------+
              |
      +-------V-------+
      | Mostrar PAGO  |
      +-------+-------+
              |
           [ FIN ]
    """)
