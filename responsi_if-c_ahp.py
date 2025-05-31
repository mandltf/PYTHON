import numpy as np
import pandas as pd
import streamlit as st

def calc_norm(M):
    if M.ndim==1:
        sM = np.sum(M)
        return M/sM
    else:
        sM = np.sum(M, axis=0)
        return M/sM
    
list_alternatif = ['HP', 'Lenovo', 'Asus', 'Acer', 'Huawei']
list_kriteria = ['CPU', 'GPU', 'RAM', 'Desain', 'Harga']

st.header('RESPONSI AHP IF-C')
st.write('Amanda Latifa - 123230138')

# kriteria
MPB_kriteria = np.array([
    [1/1, 2/1, 3/1, 4/1, 5/1],
    [1/2, 1/1, 1/2, 3/1, 4/1],
    [1/3, 1/2, 1/1, 2/1, 3/1],
    [1/4, 1/3, 1/2, 1/1, 2/1],
    [1/5, 1/4, 1/4, 1/2, 1/1]
])

with st.expander('KRITERIA : '):
    k_norm = calc_norm(MPB_kriteria)
    kriteria_norm = pd.DataFrame(k_norm, index=list_kriteria, columns=list_kriteria)
    st.write(kriteria_norm)
    m, n = k_norm.shape
    v = np.zeros(m)
    for i in range(m):
        v[i] = np.sum(k_norm[i,:])
    k_eigen = v/m
    kriteria_eigen = pd.DataFrame(k_eigen, index=list_kriteria, columns=['eigenvector'])
    st.write(kriteria_eigen)

# CPU
MPB_CPU = np.array([
    [1/1, 2/1, 3/1, 3/1, 4/1],
    [1/2, 1/1, 2/1, 2/1, 3/1],
    [1/3, 1/2, 1/1, 2/1, 2/1],
    [1/3, 1/2, 1/2, 1/1, 2/1],
    [1/4, 1/3, 1/2, 1/2, 1/1]
])

with st.expander('CPU : '):
    CPU_norm = calc_norm(MPB_CPU)
    kriteria_norm = pd.DataFrame(CPU_norm, index=list_alternatif, columns=list_alternatif)
    st.write(kriteria_norm)
    m, n = CPU_norm.shape
    v = np.zeros(m)
    for i in range(m):
        v[i] = np.sum(CPU_norm[i,:])
    CPU_eigen = v/m
    kriteria_eigen = pd.DataFrame(CPU_eigen, index=list_kriteria, columns=['eigenvector'])
    st.write(kriteria_eigen)

# GPU
MPB_GPU = np.array([
    [1/1, 2/1, 3/1, 3/1, 4/1],
    [1/2, 1/1, 2/1, 2/1, 3/1],
    [1/3, 1/2, 1/1, 2/1, 2/1],
    [1/3, 1/2, 1/2, 1/1, 2/1],
    [1/4, 1/3, 1/2, 1/2, 1/1]
])

with st.expander('GPU : '):
    GPU_norm = calc_norm(MPB_CPU)
    kriteria_norm = pd.DataFrame(GPU_norm, index=list_alternatif, columns=list_alternatif)
    st.write(kriteria_norm)
    m, n = GPU_norm.shape
    v = np.zeros(m)
    for i in range(m):
        v[i] = np.sum(GPU_norm[i,:])
    GPU_eigen = v/m
    kriteria_eigen = pd.DataFrame(GPU_eigen, index=list_alternatif, columns=['eigenvector'])
    st.write(kriteria_eigen)

# RAM
MPB_RAM = np.array([16, 8, 8, 4, 8])

with st.expander('RAM : '):
    RAM_norm = calc_norm(MPB_RAM)
    kriteria_norm = pd.DataFrame(RAM_norm, index=list_alternatif, columns=['eigenvector'])
    st.write(kriteria_norm)

# DESIGN
MPB_D = np.array([
    [1/1, 2/1, 2/1, 3/1, 3/1],
    [1/2, 1/1, 1/1, 2/1, 2/1],
    [1/2, 1/1, 1/1, 2/1, 2/1],
    [1/3, 1/2, 1/2, 1/1, 1/1],
    [1/3, 1/2, 1/2, 1/1, 1/1]
])

with st.expander('DESIGN : '):
    D_norm = calc_norm(MPB_D)
    kriteria_norm = pd.DataFrame(D_norm, index=list_alternatif, columns=list_alternatif)
    st.write(kriteria_norm)
    m, n = D_norm.shape
    v = np.zeros(m)
    for i in range(m):
        v[i] = np.sum(D_norm[i,:])
    D_eigen = v/m
    kriteria_eigen = pd.DataFrame(D_eigen, index=list_alternatif, columns=['eigenvector'])
    st.write(kriteria_eigen)

# HARGA
MPB_H = np.array([
    [1/1, 8/10, 9/10, 7/10, 8.5/10],
    [10/8, 1/1, 8/9, 7/8, 8/8.5],
    [10/9, 9/8, 1/1, 7/9, 8.5/9],
    [10/7, 8/7, 9/7, 1/1, 8.5/7],
    [10/8.5, 8.5/8, 9/8.5, 7/8.5, 1/1]
])

with st.expander('HARGA : '):
    H_norm = calc_norm(MPB_H)
    kriteria_norm = pd.DataFrame(H_norm, index=list_alternatif, columns=list_alternatif)
    st.write(kriteria_norm)
    m, n = H_norm.shape
    v = np.zeros(m)
    for i in range(m):
        v[i] = np.sum(H_norm[i,:])
    H_eigen = v/m
    kriteria_eigen = pd.DataFrame(H_eigen, index=list_alternatif, columns=['eigenvector'])
    st.write(kriteria_eigen)

gabung_eigen = np.column_stack([CPU_eigen, GPU_eigen, RAM_norm, D_eigen, H_eigen])
gabung = pd.DataFrame(gabung_eigen, index=list_alternatif, columns=list_kriteria)
st.write(gabung)

nilai = np.dot(gabung_eigen, k_eigen)
nilai_akhir = pd.DataFrame(nilai, index=list_alternatif, columns=['Hasil akhir'])
st.write(nilai_akhir)

id = np.argmax(nilai)
tertinggi = list_alternatif[id]
st.write(f"Alternatif yang paling sesuai adalah {tertinggi}")