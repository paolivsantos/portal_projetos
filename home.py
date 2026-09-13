import streamlit as st

st.set_page_config(
    page_title="Portal de Ferramentas - R7",
    page_icon="🛠️",
    layout="wide"
)

st.title("🛠️ Portal de Ferramentas e Geradores")
st.markdown("Central de acesso rápido para os utilitários de desenvolvimento e automação.")
st.markdown("---")

# Linha 1 de Projetos
col1, col2 = st.columns(2)

with col1:
    st.subheader("Gerador de Embeds")
    st.write("Ferramenta para criação e configuração de embeds.")
    st.link_button("Acessar Aplicação", "https://gerador-embeds-r7-obk9xcjfxwbfwrhotean2h.streamlit.app/", use_container_width=True)
    st.markdown("")

with col2:
    st.subheader("Gerador de HTML Dinâmico")
    st.write("Gerador voltado para estruturas RecordPlus.")
    st.link_button("Acessar Aplicação", "https://gerador-recordplus-dcpkndkmykkyxayh9y4skk.streamlit.app/", use_container_width=True)
    st.markdown("")

# Linha 2 de Projetos
col3, col4 = st.columns(2)

with col3:
    st.subheader("Gerador e Organizador de Iframes")
    st.write("Gerenciamento e estruturação de iframes para portais.")
    st.link_button("Acessar Aplicação", "https://piwlihrpmkw4pqmq8nbuwg.streamlit.app/", use_container_width=True)
    st.markdown("")

with col4:
    st.subheader("Dashboard Lei do Bem")
    st.write("Painel para acompanhamento de horas e dados da Lei do Bem.")
    st.link_button("Acessar Aplicação", "https://dashboardhorasleidobem.streamlit.app/", use_container_width=True)
    st.markdown("")
