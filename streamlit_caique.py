# Carrega Bibliotecas
import streamlit as st
import pandas as pd

# Carrega DataFrame
df = pd.read_excel('output/dados-tratados.xlsx')

# Design do aplicativo
st.title("Gerador de Receitas")
st.header(
    "Meta: criar um app gerador de receitas com diferencial da quantidade de parâmetros")


# Criar Lista de Categorias
col1, col2 = st.columns(2)
st.header("Selecionar Categoria de Alimentos")


lista_selecionados = []


botao_carne = st.button("🥩 Carne e derivados")

if botao_carne:
    lista_selecionados.append("Carnes e derivados")

else:
    pass

st.text(" Os valores selecioados até o momento sao: " + str(lista_selecionados))


# Filtra dataframe
df1 = df[df["Grupo"].isin(lista_selecionados)].reset_index(drop=True)

if len(df1) > 0:
    st.dataframe(df1)

else:
    st.text("Nenhum valor")

# with col1:
#     if st.button("🥩 Carnes e derivados"):
#         update_selection("Carnes e derivados")
#     if st.button("🥦 Verduras, hortaliças e derivados"):
#         update_selection("Verduras, hortaliças e derivados")
#     if st.button("🍎 Frutas e derivados"):
#         update_selection("Frutas e derivados")
#     if st.button("🌾 Cereais e derivados"):
#         update_selection("Cereais e derivados")
#     if st.button("🐟 Pescados e frutos do mar"):
#         update_selection("Pescados e frutos do mar")
#     if st.button("🌱 Leguminosas e derivados"):
#         update_selection("Leguminosas e derivados")
#     if st.button("🍲 Alimentos preparados "):
#         update_selection("Alimentos preparados")

# with col2:
#     if st.button("🥛 Leite e derivados")
#     update_selection("Leite e derivados")
#     if st.button("🍬 Produtos açucarados")
#     update_selection("Produtos açucarados")
#     if st.button("🧈 Gorduras e óleos")
#     update_selection("Gorduras e óleos")
#     if st.button("🍷 Bebidas (alcoólicas e não alcoólicas)")
#     update_selection("Bebidas (alcoólicas e não alcoólicas)")
#     if st.button("🍴 Miscelâneas")
#     update_selection("Miscelâneas")
#     if st.button("🥚 Ovos e derivados")
#     update_selection("Ovos e derivados")
#     if st.button("🍱 Outros alimentos industrializados")
#     update_selection("Outros alimentos industrializados")


# # Sessão para armazenamento das seleções
# if 'selected_items' not in st.session_state:
#     st.session_state.selected_items = []


# # Botão de Limpar Seleção
# st.session_state.selected_items.clear()


# option = st.selectbox("Qual ingrediente você quer utilizar ?",
#                       ("Email", "Home phone", "Mobile phone"),
#                       index=None,
#                       placeholder="Select contact method...",
#                       )

# st.write("You selected:", option)

# # Importando o DataFrame Interativo

# st.dataframe(df)
