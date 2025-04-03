import streamlit as st
import pandas as pd
import numpy as np

# Configuração inicial da página
st.set_page_config(page_title="Oráculo - Plataforma de Insights", layout="wide")

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
            st.session_state.pagina = 'novo_projeto'

    with col2:
        if st.button("📁 PROJETOS ANTIGOS", use_container_width=True):
            st.session_state.pagina = 'lista_projetos'

    with col3:
        if st.button("🗣️ PERGUNTE AO ORÁCULO", use_container_width=True):
            st.session_state.pagina = 'chat_oraculo'

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
    st.caption("Powered by Okiar | 2025")

# Formulário Novo Projeto
def novo_projeto():
    st.title("✨ Novo Projeto")
    st.markdown("Preencha as informações para solicitar um novo projeto:")

    st.subheader("Perfil do Cliente")
    renda = st.multiselect("Faixa de Renda", ["4k-5k", "5k-6k", "6k-7k", "7k-8k"])
    idade = st.slider("Faixa de Idade", 20, 50, (25, 35))
    regiao = st.multiselect("Região", ["BH e RMBH", "SP e Interior", "RJ", "MG", "ES", "Sul", "NE", "CO/AM"])

    st.subheader("Características do Empreendimento")
    caracteristicas = st.text_area("Descreva aqui:")

    if st.button("📤 Submeter Pedido"):
        st.success("Pedido submetido com sucesso! Entraremos em contato.")

    st.button("🏠 Voltar à Home", on_click=home)

# Lista de Projetos Antigos
def lista_projetos():
    st.title("📁 Projetos Antigos")

    projetos = [
        "CONJOINT #8 ABRIL 2025 MINAS",
        "CONJOINT #9 MAIO 2025 BRASIL GERAL",
        "CONJOINT #10 JUNHO 2025 ALTA RENDA SÃO PAULO",
        "CONJOINT #11 JUNHO 2025 ALTA RENDA RIO DE JANEIRO",
        "CONJOINT #12 JULHO 2025 FAMILIAS GRANDES"
    ]

    for projeto in projetos:
        if st.button(projeto):
            st.session_state.pagina = 'simulador'

    st.button("🏠 Voltar à Home", on_click=home)

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
            'Score': np.random.randint(50, 100, 6)
        }

        df_pref = pd.DataFrame(preferencias).sort_values(by="Score", ascending=False)

        st.markdown("### 📈 Ranking das Preferências")
        st.bar_chart(df_pref.set_index('Atributos')['Score'])

    st.button("🏠 Voltar à Home", on_click=home)

# Chat com o Oráculo
def chat_oraculo():
    st.title("🗣️ Pergunte ao Oráculo")
    st.markdown("Em breve, você poderá conversar diretamente com nossa inteligência artificial.")

    with st.expander("Exemplo de interação"):
        st.markdown("**Usuário:** Quais atributos mais valorizados em SP?  ")
        st.markdown("**Oráculo:** Em São Paulo, os atributos mais valorizados são Bancadas em granito e Piso laminado.")

    st.text_input("Digite sua pergunta:")
    st.button("Enviar (em breve)", disabled=True)

    st.button("🏠 Voltar à Home", on_click=home)

# Controle das páginas
if st.session_state.pagina == 'home':
    pagina_inicial()
elif st.session_state.pagina == 'novo_projeto':
    novo_projeto()
elif st.session_state.pagina == 'lista_projetos':
    lista_projetos()
elif st.session_state.pagina == 'simulador':
    simulador_conjoint()
elif st.session_state.pagina == 'chat_oraculo':
    chat_oraculo()
