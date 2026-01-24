import streamlit as st

st.set_page_config(page_title="Ordenador de Números", layout="centered")

st.title("🔢 Ordenar de Mayor a Menor")
st.write("Este programa ayuda a entender la condición: **¿Es A > B?**")

# Entrada de datos (A y B)
col1, col2 = st.columns(2)
with col1:
    a = st.number_input("Introduce el número A:", value=0)
with col2:
    b = st.number_input("Introduce el número B:", value=0)

st.divider()

# Lógica del programa (Representando el rombo del diagrama de flujo)
if st.button("ORDENAR Y VER LÓGICA"):
    if a > b:
        # Camino del SÍ
        st.success(f"Resultado: **{a}, {b}**")
        st.info(f"Lógica seguida: Como A ({a}) es mayor que B ({b}), el orden es A, B.")
    elif b > a:
        # Camino del NO
        st.success(f"Resultado: **{b}, {a}**")
        st.info(f"Lógica seguida: Como B ({b}) es mayor que A ({a}), el orden es B, A.")
    else:
        # Caso especial: Igualdad
        st.warning(f"Resultado: **{a} y {b} son iguales**")
        st.info("Lógica: No hay uno mayor que otro.")

# Visualización para los alumnos (Representación del Diagrama de Flujo en texto)
with st.expander("Ver lógica del Diagrama de Flujo"):
    st.code(f"""
    INICIO
      │
      ▼
    Leer A ({a}) y B ({b})
      │
      ▼
    ¿Es A > B? ─── NO ──▶ [ Mostrar B, A ]
      │                   (Caso: {b} > {a})
      ▼
      SÍ
      │
    [ Mostrar A, B ]
    (Caso: {a} > {b})
      │
      ▼
     FIN
    """)
