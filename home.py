import streamlit as st

st.set_page_config(
    page_title="Portal de Projetos",
    page_icon="🚀",
    layout="wide"
)

# 1. Definição da Homepage (Página Principal)
def main_page():
    st.title("Bem-vindo ao meu Portal de Projetos 🚀")
    st.markdown("---")
    st.write("Esta é a sua central de controle. Utilize o menu lateral à esquerda para navegar entre os seus 4 projetos desenvolvidos.")
    
    # Exemplo de cartões de acesso rápido na tela inicial
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("**Projeto 1**\n\nDescrição breve do que o primeiro projeto faz.")
        st.info("**Projeto 3**\n\nDescrição breve do terceiro projeto.")
        
    with col2:
        st.warning("**Projeto 2**\n\nDescrição breve do segundo projeto.")
        st.warning("**Projeto 4**\n\nDescrição breve do quarto projeto.")

# 2. Registro das páginas (Home + Os 4 Projetos)
pg = st.navigation({
    "Geral": [
        st.Page(main_page, title="Homepage", icon="🏠", default=True)
    ],
    "Meus Projetos": [
        st.Page("pages/projeto_1.py", title="Projeto 1", icon="📊"),
        st.Page("pages/projeto_2.py", title="Projeto 2", icon="⚙️"),
        st.Page("pages/projeto_3.py", title="Projeto 3", icon="📈"),
        st.Page("pages/projeto_4.py", title="Projeto 4", icon="📁"),
    ]
})

# 3. Executa a navegação selecionada
pg.run()
