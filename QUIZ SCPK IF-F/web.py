import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title='Aplikasi quiz if-f')

st.title('Aplikasi Quiz SCPK IF-F')
st.write('### Selamat datang di aplikasi quiz SCPK IF-F')
data = np.array([["FTI","UPN","YOGYAKARTA"],["FASILKOM","UGM","YOGYAKARTA"],["FEB","UI","DEPOK"]])
df = pd.DataFrame(data, columns=['FAKULTAS','KAMPUS','KOTA'])
st.write(df)

st.write('### Data Diri Saya')
st.write('Nama\t:\tAmanda Latifa')
st.write('NIM\t:\t123230138')
st.write('Kelas\t:\tPrak.SCPK IF-F')

st.write('### Fitur Aplikasi Ini')
with st.expander('Fitur'):
    tab1, tab2, tab3 = st.tabs(['Hitung Luas Segitiga','Hitung Luas Persegi','Hitung Luas Lingkaran'])

with tab1:
    st.write('### Hitung Luas Segitiga')
    a = st.number_input('Masukkan Panjang Alas:',0,100000,0)
    b = st.number_input('Masukkan Tinggi Alas:',0,100000,0)
    if st.button('Hitung luas segitiga', key='segitiga'):
        luas_segitiga = (a * b) / 2
        st.write('Luas segitiga = ',luas_segitiga)

with tab2:
    st.write('### Hitung Luas Persegi')
    c = st.number_input('Masukkan panjang sisi:',0,100000,0)
    if st.button('Hitung luas persegi', key='persegi'):
        luas_persegi = c ** 2
        st.write('Luas persegi = ',luas_persegi)

with tab3:
    st.write('### Hitung Luas Lingkaran')
    d = st.number_input('Masukkan panjang jari-jari:',0,10000,0)
    if st.button('Hitung luas lingkaran',key='lingkaran'):
        luas_lingkaran = np.pi*(d**2)
        st.write('Luas lingkaran = ',luas_lingkaran)
        
