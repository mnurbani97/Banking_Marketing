import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

def run():
    #Membuat title
    st.title('Deposito Simulation')

    #Tambahkan gambar
    image = Image.open('Deposito.jpg')
    st.image(image, caption = 'Deposito')

    #Menambahkan deskripsi
    st.write('Page ini dibuat oleh Mardhya Malik Nurbani')

    #Membuat garis
    st.markdown('----')

    #Masukkan pandas dataframe

    #Show dataframe
    df = pd.read_csv('Banking Marketing.csv')
    st.dataframe(df)

    #Membuat bar plot
    # st.write('#### Plot AttackingWorkRate')
    # fig = plt.figure(figsize=(15,5))
    # sns.countplot(x='AttackingWorkRate', data = df)
    # st.pyplot(fig)

    # #Membuat histogram
    # st.write('#### Histogram of Age')
    # fig = plt.figure(figsize=(15,5))
    # sns.histplot(df['Overall'], bins = 30, kde = True)
    # st.pyplot(fig)

    # #membuat histogram berdasarkan inputan user
    # st.write('#### Histogram berdasarkan input user')
    # #kalo mau pake radio button, ganti selectbox jadi radio
    # option = st.selectbox('Pilih Column : ', ('Age', 'Weight', 'Height', 'ShootingTotal'))
    # fig = plt.figure(figsize= (15,5))
    # sns.histplot(df[option], bins = 30, kde = True)
    # st.pyplot(fig)

    # #Membuat Plotly plot

    # st.write('#### Plotly Plot - ValueEUR vs Overall')
    # fig = px.scatter(df, x = 'ValueEUR', y = 'Overall', hover_data = ['Name', 'Age'])
    # st.plotly_chart(fig)

if __name__ == '__main__':
    run()
