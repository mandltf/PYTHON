import streamlit as st
import pandas as pd

st.title('SIOMAY')
st.header('List siomay enak di jogja')
# st.text('- siomay pak kirno')
st.write('**recommended**')

# data frame dgn var df
df = {
    'Nama' : ['kirno', 'dani','kotabaru'],
    'Alamat' : ['jalan kaliurang', 'jalan nologaten', 'kotabaru']
}
st.write('contoh Dataframe')
st.dataframe(df)

# st.write('ini tombol')
if st.button('buy now'):
    st.write('anda telah membeli siomay')

# st.write('rating')
# st.slider('slider', min_value=1, max_value=10, value=5)
st.slider('rating', 0, 100, 25)

jmlh = st.number_input('jumlah pembelian', 0, 100, 25)
st.write(jmlh)

# st.selectbox(...,...,index default)
st.selectbox('Toko pilihan', ['Siomay pak kirno', 'siomay kang dani', 'siomay telkom kotabaru'], 0)

# st.write(text input)
st.text_input('Masukkan alamat pengiriman: ', placeholder='jalan kaliurang')

st.success('berhasil membeli')
st.error('gagal order')

st.text_area('Masukkan pesan tambahan: ', placeholder='siomaynya dibanyakin')

col1, col2 = st.columns(2)
with col1: #utk ngisi kolomnya
    st.write('isi kolom 1')
with col2:
    st.write('isi kolom 2')

# st.write('Expander')
with st.expander('lihat detail'):
    st.write('ini detail siomay')
    st.text_input('Masukkan kata: ', placeholder='apa')

# st.write('ini tabs')
tab1, tab2 = st.tabs(['informasi','ulasan'])
with tab1:
    st.write('someh paling enak di jalan kaliurang km 5')
with tab2:
    st.write('ini tab 2')