import streamlit as st
import pandas as pd
from sklearn import datasets
import matplotlib.pyplot as plt

#pengaturan web
st.set_page_config(page_title='eksplorasi iris')
st.title('✨aplikasi eksplorasi dataset iris')
st.write('## menyajikan dataset iris secara interaktif')

iris = datasets.load_iris()
# Create a new dataframe from the iris dataset
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target
df['species'] = df['target'].map({
    0:'setosa',
    1:'versicolor',
    2:'virginica'
})

st.write('dataset iris')
jml = st.sidebar.slider('Jumlah data yang ingin ditampilkan', 5, len(df), 10)
st.dataframe(df.head(jml))
# st.dataframe(df.head()) #head biar ga smuanya ketampil

with st.expander('informasi dataset'):
    # informasi dataset
    st.write('\n')
    st.write('#### informasi dataset')
    st.write('jumlah data: ', len(df))
    st.text(df.info())

    #cek missing values/ data kosong
    st.write('\n')
    st.write('#### cek missing values')
    st.write(df.isnull().sum()) #cek missing values

    st.write('#### statistik deskriptif')
    st.write(df.describe())

st.header('visualisasi data')
tab1, tab2 = st.tabs(['hai','hello']) #blom selese

#visualisasi data
st.write('\n')
st.write('#### visualisasi data')
fig, ax = plt.subplots(figsize=(10,5))
for species in df['target'].unique(): #mengambil data berdasarkan target dgn nilai yg sama sbyk 1 kali
    subset = df[df['target'] == species]
    ax.plot(subset.index, subset['sepal length (cm)'], marker='o', linestyle='-', label=f'Species {species}')

ax.set_title('Visualisasi Data Iris')
ax.set_xlabel('index')
ax.set_ylabel('Sepal Length')
ax.legend(title='species')
st.pyplot(fig) #untuk menampilkan plotnya

#st.write(df['sepal length (cm)'].value_counts()) #menghitung