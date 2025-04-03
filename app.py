import streamlit as st
import pandas as pd
import numpy as np

# Configuração inicial da página
st.set_page_config(page_title="Oráculo - Simulador Conjoint", layout="wide")

# Estado da sessão para controlar telas
if 'pagina' not in st.session_state:
    st.session_state.pagina = 'home'

# Função para voltar à página inicial
def home():
    st.session_state.pagina = 'home'

# Página inicial (Home)
def pagina_inicial():
    st.title("🔮 ORÁCULO")
    st.subheader("O que é valor para o cliente?")

    st.divider()

    col1, col2, col3 = st.columns(3, gap="large")

    with col1:
        if st.button("✨ NOVO PROJETO", use_container_width=True):
            st.info("📋 [Aqui aparecerá o formulário para o briefing do projeto.]")

    with col2:
        if st.button("📁 PROJETOS ANTIGOS", use_container_width=True):
            st.session_state.pagina = 'simulador'

    with col3:
        if st.button("🗣️ PERGUNTE AO ORÁCULO", use_container_width=True):
            st.info("🤖 [Aqui será possível interagir com o Oráculo via IA futuramente.]")

    st.divider()

    st.markdown("### ⚙️ Gestão e Governança")
    alert_col, users_col, gov_col = st.columns(3, gap="large")

    with alert_col:
        st.markdown("#### 🚨 Alertas")
        st.info("🔔 Nenhum alerta no momento.")

    with users_col:
        st.markdown("#### 👥 Usuários")
        st.info("Gerencie usuários e permissões de acesso.")

    with gov_col:
        st.markdown("#### 🔐 Governança")
        st.info("Controle e registre o acesso e alterações dos projetos.")

    st.divider()
    st.caption("Powered by SuaEmpresa | 2024")

# Simulador Conjoint simples
def simulador_conjoint():
    st.title("📊 Simulador Conjoint")

    st.subheader("🔍 Comparação Rápida")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Opção A:**")
        escolha1 = st.radio("Parede Hidráulica", ["Cerâmica até 150cm", "Apenas cerâmica acima da bancada"], key='a1')
        escolha2 = st.radio("Piso Sala/Quarto", ["Piso laminado", "Sem piso"], key='a2')
        escolha3 = st.radio("Bancadas", ["Granito", "Louça + pia inox"], key='a3')

    with col2:
        st.markdown("**Opção B:**")
        escolha4 = st.radio("Itens Esportivos", ["Piscina", "Mini quadra recreativa"], key='b1')
        escolha5 = st.radio("Itens Sociais Individuais", ["Churrasqueira", "Espaço pizza"], key='b2')
        escolha6 = st.radio("Facilites", ["Lavanderia", "Pet care"], key='b3')

    if st.button("Avaliar Preferências"):
        preferencias = {
            'Atributos': ["Parede Hidráulica", "Piso Sala/Quarto", "Bancadas", "Itens Esportivos", "Itens Sociais Individuais", "Facilites"],
            'Escolhas': [escolha1, escolha2, escolha3, escolha4, escolha5, escolha6],
            'Score': np.random.randint(50, 100, 6)  # Mockup scores
        }

        df_pref = pd.DataFrame(preferencias).sort_values(by="Score", ascending=False)

        st.markdown("### 📈 Ranking das Preferências")
        st.bar_chart(df_pref.set_index('Atributos')['Score'])

    st.button("🏠 Voltar à Home", on_click=home)

# Controle das páginas
if st.session_state.pagina == 'home':
    pagina_inicial()
elif st.session_state.pagina == 'simulador':
    simulador_conjoint()
