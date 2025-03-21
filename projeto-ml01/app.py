# Importa a biblioteca Streamlit para criar a interface web
import streamlit as st

# Importa a biblioteca Pandas para manipulação de dados
import pandas as pd

# Importa o modelo de regressão linear do Scikit-Learn
from sklearn.linear_model import LinearRegression

# Lê os dados do arquivo CSV contendo informações sobre pizzas
df = pd.read_csv("pizzas.csv")

# Cria um modelo de regressão linear
modelo = LinearRegression()

# Define as variáveis independentes (diâmetro da pizza) e dependentes (preço da pizza)
x = df[["diametro"]]
y = df[["preco"]]

# Treina o modelo com os dados fornecidos
modelo.fit(x, y)

# Define o título da aplicação no Streamlit
st.title("Prevendo o valor de uma pizza")

# Adiciona um divisor visual na interface
st.divider()

# Cria um campo de entrada numérico para o usuário inserir o diâmetro da pizza
diametro = st.number_input("digite o tamanho do diametro da pizza: ")

# Verifica se o usuário inseriu um valor no campo de entrada
if diametro:
  # Faz a previsão do preço da pizza com base no diâmetro informado
  preco_previsto = modelo.predict([[diametro]])[0][0]
  
  # Exibe o valor previsto da pizza na interface
  st.write(f"o valor da pizza com diametro de {diametro:.2f} cm é de R$ {preco_previsto:.2f}.")
