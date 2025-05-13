import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title='WP')
st.header('Dataframe')
st.write('123230138 - Amanda Latifa')
tab1, tab2, tab3 = st.tabs(['Kriteria','Alternatif','Matriks'])

list_kriteria = []
list_bobot = []
list_norm_bobot = []
list_keterangan = []
list_alternatif = []

with tab1:
    jml = st.number_input('Matriks Jumlah kriteria',1)
    for a in range(int(jml)):
        col1, col2,col3 = st.columns(3)
        with col1:
            kriteria = st.text_input(f'Kriteria {a+1}')
            list_kriteria.append(kriteria)
        with col2:
            bobot = st.number_input(f'Bobot {list_kriteria[a]}',0, key=f'bobot{a}')
            list_bobot.append(bobot)
        with col3:
            ket = ['Benefit','Cost']
            keterangan = st.selectbox(f'Keterangan {list_kriteria[a]}', ket, key=f'ket{a}')
            if keterangan=='Benefit':
                list_keterangan.append(1)
            else:
                list_keterangan.append(-1)
    # normalisasi bobot
    total_bobot = sum(list_bobot) if sum(list_bobot)>0 else 1 #biar ga dividen by zero
    norm_bobot = [nilai/total_bobot for nilai in list_bobot]
    list_norm_bobot = norm_bobot

with tab2:
    jml2 = st.number_input('Masukkan jumlah alternatif',1)
    for b in range(int(jml2)):
        alternatif = st.text_input(f'Alternatif {b+1}', key=f'alt{b}')
        list_alternatif.append(alternatif)

with tab3:
    st.subheader('Matriks Alternatif')
    # header tabel
    kol = st.columns(len(list_kriteria)+1)
    kol[0].markdown('*#*')
    for i, j in enumerate(list_kriteria):
        kol[i+1].write(f'{j} ({list_bobot[i]})')

    # isi tabel
    matriks = []
    for a, alt in enumerate(list_alternatif):
        cols = st.columns(len(list_kriteria)+1)
        cols[0].write(alt)
        baris = []
        for b in range(len(list_kriteria)):
            isi = cols[b+1].number_input(f'{a, b}',0, key=f'{b},{a}')
            baris.append(isi)
        matriks.append(baris)
    
    # DataFrame data
    if st.button('Buat DataFrame',key='buat'):
        df = pd.DataFrame(matriks, index=list_alternatif, columns=list_kriteria)
        st.write(df)
        st.success('Matriks Berhasil Dibuat')
    
    if st.button('Find Best Alternatif', key='best'):
        # DataFrame normalisasi bobot
        df1 = pd.DataFrame(list_norm_bobot, index=list_alternatif, columns=['Normalized Weights'])
        st.write(df1)
        s = []
        for a in range(len(list_alternatif)):
            vektor_s = 1
            for b in range(len(list_kriteria)):
                vektor_s *= matriks[a][b]**(list_norm_bobot[b]*list_keterangan[b])
            s.append(vektor_s)

        # DataFrame vektor s
        df2 = pd.DataFrame(s, index=list_alternatif, columns=['Vektor S'])   
        st.write(df2)   
        v = [nilai/sum(s) for nilai in s]

        # DataFrame vektor v
        df3 = pd.DataFrame(v, index=list_alternatif, columns=["Vektor V"])
        st.write(df3)

        best = list_alternatif[v.index(max(v))]
        st.markdown(f'**Alternatif Terbaik adalah {best}**')

        