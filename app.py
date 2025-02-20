# Importando as bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Criando um DataFrame simples com pandas
data = {
    'Categoria': ['A', 'B', 'C', 'D', 'E'],
    'Valores1': [10, 20, 15, 25, 30],
    'Valores2': [5, 15, 10, 20, 25],
    'Valores3': [8, 18, 12, 22, 28]
}

df = pd.DataFrame(data)

# Gerando os gráficos com matplotlib
fig1, ax1 = plt.subplots()
ax1.bar(df['Categoria'], df['Valores1'], color='blue')
ax1.set_title('Gráfico de Barras')
ax1.set_xlabel('Categorias')
ax1.set_ylabel('Valores')

fig2, ax2 = plt.subplots()
ax2.plot(df['Categoria'], df['Valores2'], marker='o', color='green')
ax2.set_title('Gráfico de Linhas')
ax2.set_xlabel('Categorias')
ax2.set_ylabel('Valores')

fig3, ax3 = plt.subplots()
ax3.scatter(df['Categoria'], df['Valores3'], color='red')
ax3.set_title('Gráfico de Dispersão')
ax3.set_xlabel('Categorias')
ax3.set_ylabel('Valores')

# Criando a aplicação no Streamlit
st.title("Visualização de Gráficos com Streamlit")
st.write("Este aplicativo exibe três gráficos diferentes gerados a partir de um"
         " DataFrame simples.")

# Exibindo os gráficos interativamente
st.pyplot(fig1)
st.pyplot(fig2)
st.pyplot(fig3)
