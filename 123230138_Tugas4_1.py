import numpy as np
import pandas as pd
import streamlit as st

st.title("Analytical Hierarchy Process")

def calc_norm(M):
    print ('Normalisasi Matriks')
    if M.ndim == 1 :
        sM = np.sum(M)
        return M/sM
    else:
        sM = np.sum(M, axis = 0)
        return M/sM

list_kriteria = ['gaya', 'keandalan', 'keekonomisan', 'biaya']
list_alternatif = ['Yamaha', 'Honda', 'Suzuki', 'Kawasaki']

# kriteria
st.write("#### kriteria")
MPB_kriteria = np.array([
    [1/1, 1/2, 3/1, 1/2],
    [2/1, 1/1, 4/1, 3/1],
    [1/3, 1/4, 1/1, 2/1],
    [2/1, 1/3, 1/2, 1/1]
])

with st.expander("Detail : "):
    st.write("Matrik Perbandingan Berpasangan Kriteria")
    kriteria = pd.DataFrame(MPB_kriteria, index=list_kriteria, columns=list_kriteria)
    st.write(kriteria)

    k_norm = calc_norm(MPB_kriteria)
    st.write("Normalisasi Matriks")
    kriteria_norm = pd.DataFrame(k_norm, index=list_kriteria, columns=list_kriteria)
    st.write(kriteria_norm)

    m, n = k_norm.shape
    V = np.zeros(m)
    for i in range(m):
        V[i] = np.sum(k_norm[i, :])

    k_eigen = V / m
    st.write("Eigenvector")
    kriteria_eigen = pd.DataFrame(k_eigen, index=list_kriteria, columns=["Eigenvector"])
    st.write(kriteria_eigen)

# Kriteria Gaya
st.write("#### Alternatif - Gaya")
MPB_gaya = np.array([
    [1/1, 1/2, 2/1, 1/3],
    [2/1, 1/1, 3/1, 1/2],
    [1/2, 1/3, 1/1, 1/4],
    [3/1, 2/1, 4/1, 1/1]
])

with st.expander("Detail : "):
    st.write("Matrik Perbandingan Berpasangan Kriteria Gaya")
    kriteria = pd.DataFrame(MPB_gaya, index=list_alternatif, columns=list_alternatif)
    st.write(kriteria)

    g_norm = calc_norm(MPB_gaya)
    st.write("Normalisasi Matriks")
    kriteria_norm = pd.DataFrame(g_norm, index=list_alternatif, columns=list_alternatif)
    st.write(kriteria_norm)

    m, n = g_norm.shape
    V = np.zeros(m)
    for i in range(m):
        V[i] = np.sum(g_norm[i, :])

    g_eigen = V / m
    st.write("Eigenvector")
    kriteria_eigen = pd.DataFrame(g_eigen, index=list_alternatif, columns=["Eigenvector"])
    st.write(kriteria_eigen)

# Kriteria Keandalan
st.write("#### Alternatif - Keandalan")
MPB_andal = np.array([
    [1/1, 1/2, 3/1, 2/1],
    [2/1, 1/1, 4/1, 3/1],
    [1/3, 1/4, 1/1, 1/2],
    [1/2, 1/3, 2/1, 1/1]
])

with st.expander("Detail : "):
    st.write("Matrik Perbandingan Berpasangan Kriteria Keandalan")
    kriteria = pd.DataFrame(MPB_andal, index=list_alternatif, columns=list_alternatif)
    st.write(kriteria)

    a_norm = calc_norm(MPB_andal)
    st.write("Normalisasi Matriks")
    kriteria_norm = pd.DataFrame(a_norm, index=list_alternatif, columns=list_alternatif)
    st.write(kriteria_norm)

    m, n = a_norm.shape
    V = np.zeros(m)
    for i in range(m):
        V[i] = np.sum(a_norm[i, :])

    a_eigen = V / m
    st.write("Eigenvector")
    kriteria_eigen = pd.DataFrame(a_eigen, index=list_alternatif,columns=["Eigenvector"])
    st.write(kriteria_eigen)

# Kriteria Keekonomisan
st.write("#### Alternatif - Keekonomisan")
ym = 60
hn = 80
sz = 60
kw = 80

ekonomis = np.array([ym, hn, sz, kw])

with st.expander("Detail : "):
    st.write("Perbandingan Kriteria Keekonmisan")
    kriteria = pd.DataFrame(ekonomis, index=list_alternatif, columns=["Nilai"])
    st.write(kriteria)

    e_norm = calc_norm(ekonomis)

    st.write("Eigenvector")
    ekonomi_eigen = pd.DataFrame(e_norm, index=list_alternatif, columns=["Eigenvector"])
    st.write(ekonomi_eigen)

# Kriteria Biaya
st.write("#### Alternatif - Biaya")
ym = 16
hn = 30
sz = 15
kw = 40

biaya = np.array([ym, hn, sz, kw])

with st.expander("Detail : "):
    st.write("Perbandingan Kriteria Biaya")
    kriteria = pd.DataFrame(biaya, index=list_alternatif, columns=["Nilai"])
    st.write(kriteria)

    b_norm = calc_norm(biaya)

    st.write("Eigenvector")
    biaya_eigen = pd.DataFrame(b_norm, index=list_alternatif, columns=["Eigenvector"])
    st.write(biaya_eigen)

st.write("#### Jawaban Akhir dan Vector Keputusan")
st.write("Eigenvector")
gabung_eigen = np.column_stack([g_eigen, a_eigen, e_norm, b_norm])
gabung = pd.DataFrame(gabung_eigen, index=list_alternatif, columns=list_kriteria)
st.write(gabung)

st.write("Nilai Akhir")
Score = np.dot(gabung_eigen, k_eigen)
Score_full = pd.DataFrame(Score, index=list_alternatif, columns=["Hasil Akhir"])
st.write(Score_full)

# Mendapatkan nama motor dan nilai tertinggi
Motor_id = np.argmax(Score)
Motor_Win = list_alternatif[Motor_id]
Max_Motor_Score = np.max(Score)

st.write(f'Nilai motor terbaik terpilih berdasarkan kriteria adalah {Motor_Win} dengan nilai akhir {Max_Motor_Score}')