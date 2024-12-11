import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(layout="wide")
st.title("Dashboard - Casamento David & Bianca")
df = pd.read_excel("Controle de Fornecedores Casamento (Simulação de orçamento) - David&Bianca.xlsx", header=None)

st.subheader("Dados da Planilha")
st.write(df)

# Nomear as colunas manualmente
df.columns = ['Coluna1', 'Coluna2', 'Coluna3', 'Fornecedores', 'Valores', 'Coluna6', 'Coluna7']

st.subheader("Alterar Valores da Planilha")
coluna = st.selectbox("Escolha a coluna", df.columns)
linha = st.number_input("Escolha a linha para editar", min_value=0, max_value=len(df)-1, step=1)

# Mostrar o valor atual da célula
valor_atual = df.at[linha, coluna]
st.write(f"Valor atual da célula {coluna} na linha {linha}: {valor_atual}")

# Caixa de input para alterar o valor
novo_valor = st.number_input(f"Novo valor para a célula {coluna} na linha {linha}", value=valor_atual)

# Atualizar o DataFrame com o novo valor
if st.button("Atualizar Valor"):
    df.at[linha, coluna] = novo_valor
    st.success(f"Valor da célula {coluna} na linha {linha} foi atualizado para {novo_valor}")

fig_date = px.bar(df, x='Fornecedores', y='Valores', title="Visualização em Gráfico")

col1 = st.columns(1)

col1[0].plotly_chart(fig_date, use_container_width=True)

vatest = ""








