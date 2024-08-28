# Carrega Bibliotecas
import streamlit as st
import pandas as pd
from functions.ia import ia

st.set_page_config(
    layout="wide", page_title="Chef Personalizado", page_icon="👩‍🍳")

# Imagem de Capa
imagem = st.image('input/imagem_2.jpg', use_column_width=True)


# Carrega DataFrame
df = pd.read_excel('output/dados-tratados.xlsx')

col1, col2, = st.columns(2)

# Design do aplicativo
with col1:
    st.title("Chef Personalizado: Seu Gerador de Receitas Sob Medida")
    st.markdown(
        "##### Aplicativo de Receitas com Personalização Avançada de Parâmetros")

# Botão de Limpeza (como fazer que um unico botão limpe tudo???)

with col2:
    if st.button('Limpar Receita'):
        st.session_state.clear()


st.divider()
col3, col4, = st.columns(2)

# Escolher tipo de refeição
with col3:
    tipo_refeicao = genre = st.radio(
        "Qual a refeição?",
        ["Café da manhã", "Almoço", "Café da tarde", "Jantar", "Lanche"], index=None,)


# Criar Listas de Categorias
with col4:
    grupos_selecionados = st.multiselect("Escolha o grupo de alimentos", ["Carnes e derivados", "Verduras, hortaliças e derivados", "Frutas e derivados", "Cereais e derivados", "Pescados e frutos do mar", "Leguminosas e derivados",
                                                                          "Alimentos preparados", "Leite e derivados", "Produtos açucarados", "Gorduras e óleos", "Bebidas (alcoólicas e não alcoólicas)", "Miscelâneas", "Ovos e derivados", "Outros alimentos industrializados"])


# Filtra dataframe
df1 = df[df["Grupo"].isin(grupos_selecionados)].reset_index(drop=True)

lista_ingredientes = df1["Descrição do Alimento"].drop_duplicates().to_list()

with col4:
    # Criar Seleção de Ingrediente
    ingredientes_selecionados = st.multiselect(
        "Selecionar o ingrediente:",
        lista_ingredientes,
    )

st.divider()

# Botão de gerar receita

botao_gerar_receita = st.button("Gerar receita")

# Integrando IA
if botao_gerar_receita:

    prompt = f"""

        Por favor, gerar uma receita para a seguinte refeição:

        {tipo_refeicao}

        dentro do seguinte grupo de alimentos:

        {grupos_selecionados}

        com os seguintes ingredientes:

        {ingredientes_selecionados}

        """
    resposta = ia(prompt)
    # Armazenar a resposta em uso
    st.session_state["retorno"] = resposta


# Consulta resposta armazenada
if "retorno" in st.session_state:
    st.code(st.session_state["retorno"])

# Botão de Download da Receita
if "retorno" in st.session_state:
    texto = st.session_state["retorno"]
    st.download_button(label="Download da Receita", data=texto)
