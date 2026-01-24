import streamlit as st

st.set_page_config(page_title="Cálculo de Entradas", layout="centered")

st.title("🎟️ Taquilla de Espectáculo")

# Definimos el precio fijo
PRECIO_ENTRADA = 100

# Pedimos la cantidad, usando el precio como título del input
cantidad = st.number_input(f"Precio entrada: {PRECIO_ENTRADA} €. ¿Cuántas deseas comprar?", value=1)

if st.button("Calcular Pago"):
    # 1. Validación (Filtro de error)
    if cantidad < 1 or cantidad > 4:
        st.error("❌ Error: Solo se permite la compra de 1 a 4 entradas.")
    else:
        # 2. Lógica de descuentos según cantidad
        descuento = 0
        if cantidad == 2:
            descuento = 0.10
        elif cantidad == 3:
            descuento = 0.15
        elif cantidad == 4:
            descuento = 0.20
        
        # 3. Cálculo final
        total_sin_dto = cantidad * PRECIO_ENTRADA
        pago_final = total_sin_dto * (1 - descuento)
        
        # 4. Resultado directo
        st.subheader(f"Total a pagar: {pago_final:.0f} €")
        if descuento > 0:
            st.write(f"(Aplicado descuento del {int(descuento*100)}%)")

# Diagrama de flujo para los alumnos
with st.expander("Ver Diagrama de Flujo"):
    error_v = " <--- RUTA ACTIVA" if cantidad < 1 or cantidad > 4 else ""
    exito_v = " <--- RUTA ACTIVA" if 1 <= cantidad <= 4 else ""

    st.code(f"""
          [ INICIO ]
              |
      +-------V-------+
      | Leer Cantidad | ({cantidad})
      +-------+-------+
              |
      ________V________
     /                 \\
    /  ¿Es Cantidad     \\
    \\   entre 1 y 4?    /
     \\_________________/
      |               |
    ( NO )          ( SÍ )
      |               |
 [ ERROR ]{error_v}   [ CALCULAR ]{exito_v}
      |               |
      |       +-------V-------+
      |       | ¿2? -> 10%    |
      |       | ¿3? -> 15%    |
      |       | ¿4? -> 20%    |
      |       +-------+-------+
      |               |
      +-------+-------+
              |
      +-------V-------+
      | Mostrar PAGO  |
      +-------+-------+
              |
           [ FIN ]
    """)
