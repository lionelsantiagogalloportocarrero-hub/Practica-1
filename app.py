import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Salud 3º ESO", page_icon="🏥")

# Título y Descripción
st.title("🔽Calculadora de rebajas")
st.markdown("Bienvenido. Introduce tus datos para calcular tus rebajas.")
st.write("---") # Línea separadora

# 2. Entrada de Datos (Barra Lateral)
st.sidebar.header("Tus Datos")
precio = st.sidebar.number_input("Precio del producto (€)", min_value=0, max_value=100000000, value=100)
porcentaje = st.sidebar.slider("Porcentaje de rebaja(%)", 0.00, 50.0, 100.00)

# 3. Botón de Cálculo y Lógica
if st.button("Calcular ahora"):
    
    # Fórmula Matemática: Peso entre altura al cuadrado
    PF = precio - (precio * porcentaje/100)
    
    # 4. Mostrar Resultado con Diseño
    col1, col2 = st.columns(2)
    
    with col1:
        # Usamos metric para que el número se vea grande
        st.metric(label="Tu precio final es:", value=f"{PF:.2f}")
        
    with col2:
        # Usamos condicionales (if/elif/else) para el diagnóstico
        if porcentaje < 25:
            st.warning("🔴 Ahorro mínimo")
        elif 25 <= porcentaje < 50:
            st.success("🟠 Ahorro mediano")
        elif 50 <= porcentaje < 75:
            st.warning("✅ Mega ahorro")
        else:
            st.error("🤩 Ofertón")
            st.balloons() # ¡Premio!
    # Extra: Mostrar la fórmula usada (LaTeX)
    st.write("---")
    st.info("Fórmula matemática utilizada:")
    st.latex(r''' PF = P - P * porcentaje ''')
