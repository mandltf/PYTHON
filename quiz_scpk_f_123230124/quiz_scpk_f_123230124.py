import streamlit as st
import pandas as pd
import numpy as np

st.title('Aplikasi Quiz SCPK IF-F')
st.text('Selamat datang di aplikasi Quiz SCPK IF-F')

st.subheader('Data Fakultas pada Kampus')

df = pd.DataFrame({
    'Fakultas': ['FTI','Fasilkom','FEB'],
    'Kampus': ['UPN','UGM','UI'],
    'Kota': ['Yogyakarta', 'Yogyakarta', 'Depok']
})

st.dataframe(df)

st.subheader('Data Diri Saya')
col1,col2,col3 = st.columns(3)
with col1:
    st.write('Nama')
    st.write('NIM')
    st.write('Kelas')
with col2:
    st.write(':')
    st.write(':')
    st.write(':')
with col3:
    st.write('Nadhifa Alya Syafinka')
    st.write('123230124')
    st.write('Prak. SCPK IF-F')

st.subheader('Fitur Aplikasi Ini')

with st.expander("Fitur"):
    segitiga, persegi, lingkaran = st.tabs(['📐Hitung Luas Segitiga', '🟦Hitung Luas Persegi','⚽Hitung Luas Lingkaran'])
    with segitiga:
        st.write('Ini fitur menghitung luas segitiga')
        alas = st.number_input('Masukkan Panjang Alas:')
        tinggi = st.number_input('Masukkan Panjang Tinggi:')
        if st.button('Hitung Luas Segitiga'):
            luas = (alas*tinggi)/2
            st.write(f'Luas Segitiga = {luas}')
    
    with persegi:
        st.write('Ini fitur menghitung luas persegi')
        sisi = st.number_input('Masukkan Panjang Sisi:')
        if st.button('Hitung Luas Persegi'):
            luas = sisi**2
            st.write(f'Luas Persegi = {luas}')

    with lingkaran:
        st.write('Ini fitur menghitung luas lingkaran')
        r = st.number_input('Masukkan Panjang Jari-Jari:')
        if st.button('Hitung Luas Lingkaran'):
            luas = 3.14*(r**2)
            st.write(f'Luas Lingkaran = {luas}')
            
