import streamlit as st

# Configuração da página (título na aba e layout)
st.set_page_config(
    page_title="Calculadora Simples",
    page_icon="🧮",
    layout="centered"
)

# 1. Título principal com ícone amigável
st.title("🧮 Calculadora Interativa")
st.write("Escolha os números, selecione a operação e clique em **Calcular**.")

st.divider()

# Estrutura em colunas para os números ficarem lado a lado (estética limpa)
col1, col2 = st.columns(2)

# 2. Campos de entrada numérica com valor padrão 0.0
with col1:
    numero_1 = st.number_input("Primeiro número", value=0.0, step=1.0)

with col2:
    numero_2 = st.number_input("Segundo número", value=0.0, step=1.0)

# 3. Componente de seleção da operação
operacao = st.selectbox(
    "Selecione a operação",
    options=["Soma (+)", "Subtração (-)", "Multiplicação (*)", "Divisão (/)"]
)

st.write("")  # Espaço em branco para respirar o layout

# 4. Botão de ação
if st.button("Calcular", type="primary", use_container_width=True):
    
    # 5. Processamento do cálculo e validação
    if operacao == "Soma (+)":
        resultado = numero_1 + numero_2
        st.metric(label="Resultado da Soma", value=f"{resultado:.2f}")

    elif operacao == "Subtração (-)":
        resultado = numero_1 - numero_2
        st.metric(label="Resultado da Subtração", value=f"{resultado:.2f}")

    elif operacao == "Multiplicação (*)":
        resultado = numero_1 * numero_2
        st.metric(label="Resultado da Multiplicação", value=f"{resultado:.2f}")

    elif operacao == "Divisão (/)":
        # Validação de divisão por zero
        if numero_2 == 0.0:
            st.error("⚠️ Ops! Não é possível dividir um número por zero.")
        else:
            resultado = numero_1 / numero_2
            st.metric(label="Resultado da Divisão", value=f"{resultado:.2f}")
