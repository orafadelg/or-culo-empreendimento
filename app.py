import streamlit as st

# Configuração da Página
st.set_page_config(page_title="Oráculo - O que é valor para o cliente?", layout="wide")

# Título principal
st.title("🔮 ORÁCULO")
st.subheader("O que é valor para o cliente?")

st.divider()

# Colunas para botões principais
col1, col2, col3 = st.columns(3, gap="large")

with col1:
    if st.button("✨ NOVO PROJETO", use_container_width=True):
        st.success("Abrindo tela de criação de novo projeto (briefing)...")
        st.info("📋 [Aqui aparecerá o formulário para o briefing do projeto.]")

with col2:
    if st.button("📁 PROJETOS ANTIGOS", use_container_width=True):
        st.success("Abrindo tela com inventário de projetos antigos...")
        st.info("📑 [Aqui aparecerá o inventário dos projetos já realizados.]")

with col3:
    if st.button("🗣️ PERGUNTE AO ORÁCULO", use_container_width=True):
        st.success("Abrindo o módulo de consulta inteligente...")
        st.info("🤖 [Aqui será possível interagir com o Oráculo via IA futuramente.]")

st.divider()

# Seção inferior com alertas, gestão e governança
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

# Rodapé estilizado
st.divider()
st.caption("Powered by SuaEmpresa | 2024")
