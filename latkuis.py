import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('kematian.csv')

st.set_page_config(page_title='Latihan Kuis')
st.header('💀Data Penyebab Kematian')

jml = st.number_input('Jumlah data:',0,len(data),10)
st.dataframe(data.head(jml))

st.subheader('Fitur Aplikasi')
tab1, tab2 = st.tabs(['Fitur Dataset','Line Plot-Rata rata Kematian tiap Tahun'])
with tab1:
    array = ['Bencana Alam','Bencana Non Alam dan Penyakit','Bencana Sosial']
    pilih = st.selectbox('Pilih Tipe',array)
    if pilih == 'Bencana Alam':
        st.write(data[data['Type']=='Bencana Alam'])
    elif pilih == 'Bencana Non Alam dan Penyakit':
        st.write(data[data['Type']=='Bencana Non Alam dan Penyakit'])
    elif pilih == 'Bencana Sosial':
        st.write(data[data['Type']=='Bencana Sosial'])

with tab2:
    X = data['Year'].dropna()
    Z = data.dropna(subset=['Year','Total Deaths'])
    Y = Z.groupby('Year')['Total Deaths'].mean()
    fig, ax = plt.subplots()
    ax.plot(Y.index,Y.values, 'o-b')
    ax.set_title('Rata-rata Kematian tiap Tahun')
    ax.set_xlabel('Tahun')
    ax.set_ylabel('Rata-rata jumlah kematian')
    st.pyplot(fig)
