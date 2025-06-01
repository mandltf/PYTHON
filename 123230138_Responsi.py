import streamlit as st
import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl
import matplotlib.pyplot as plt

ipk = ctrl.Antecedent(np.arange(0.0,5.0,1.0), 'ipk')
uang = ctrl.Antecedent(np.arange(0.0,11.0,1.0), 'uang')
jml = ctrl.Antecedent(np.arange(0,11,1), 'jml')

nilai = ctrl.Consequent(np.arange(0,101,1), 'nilai')
finansial = ctrl.Consequent(np.arange(0,101,1), 'finansial')
rekomen = ctrl.Consequent(np.arange(0,101,1), 'rekomen')

ipk['rendah'] = fuzz.gaussmf(ipk.universe, 1.5, 0.6)
ipk['sedang'] = fuzz.gaussmf(ipk.universe, 3, 0.4)
ipk['tinggi'] = fuzz.gaussmf(ipk.universe, 4, 0.2)

uang['rendah'] = fuzz.trimf(uang.universe, [-1, 0, 4])
uang['sedang'] = fuzz.trimf(uang.universe, [2, 5, 8])
uang['tinggi'] = fuzz.trimf(uang.universe, [6, 10, 11])

jml['sedikit'] = fuzz.trimf(jml.universe, [-1, 0,4])
jml['sedang'] = fuzz.trimf(jml.universe, [2, 5, 8])
jml['banyak'] = fuzz.trimf(jml.universe, [6, 10, 11])

nilai['rendah'] = fuzz.trimf(nilai.universe, [-1, 0, 40])
nilai['sedang'] = fuzz.trimf (nilai.universe, [30, 50, 70])
nilai['tinggi'] = fuzz.trimf (nilai.universe, [60, 100, 101])

finansial['tidak'] = fuzz.trimf (finansial.universe, [-1, 0, 40])
finansial['perlu'] = fuzz.trimf (finansial.universe, [30, 50, 70])
finansial['sangat'] = fuzz.trimf (finansial.universe, [60, 100, 101])

rekomen['kurang layak'] = fuzz.trimf (rekomen.universe, [-1, 0, 40])
rekomen['dipertimbangkan'] = fuzz.trimf (rekomen.universe, [30, 50, 70])
rekomen['sangat layak'] = fuzz.trimf (rekomen.universe, [60, 100, 101])

rules = [
    ctrl.Rule(ipk['tinggi'] & uang['rendah'] & jml['banyak'], [nilai['tinggi'], finansial['sangat'], rekomen['sangat layak']]),
    ctrl.Rule(ipk['tinggi'] & uang['tinggi'] & jml['sedikit'], [nilai['tinggi'], finansial['tidak'], rekomen['kurang layak']]),
    ctrl.Rule(ipk['tinggi'] & uang['sedang'] & jml['sedang'], [nilai['tinggi'], finansial['perlu'], rekomen['sangat layak']]),
    
    ctrl.Rule(ipk['sedang'] & uang['rendah'] & jml['banyak'], [nilai['sedang'], finansial['sangat'], rekomen['sangat layak']]),
    ctrl.Rule(ipk['sedang'] & uang['tinggi'] & jml['sedikit'], [nilai['sedang'], finansial['tidak'], rekomen['dipertimbangkan']]),
    ctrl.Rule(ipk['sedang'] & uang['sedang'] & jml['sedang'], [nilai['sedang'], finansial['perlu'], rekomen['dipertimbangkan']]),
    
    ctrl.Rule(ipk['rendah'] & uang['rendah'] & jml['banyak'], [nilai['rendah'], finansial['sangat'], rekomen['dipertimbangkan']]),
    ctrl.Rule(ipk['rendah'] & uang['tinggi'] & jml['sedikit'], [nilai['rendah'], finansial['tidak'], rekomen['kurang layak']]),
    ctrl.Rule(ipk['rendah'] & uang['sedang'] & jml['sedang'], [nilai['rendah'], finansial['perlu'], rekomen['kurang layak']]),
]

sistem_ctrl = ctrl.ControlSystem(rules)
sistem = ctrl.ControlSystemSimulation(sistem_ctrl)

st.title('👨‍🍳 Responsi IF-G FUZZY')
st.write('Amanda Latifa - 123230138')

st.sidebar.subheader('Input Data')
ipk_input = st.sidebar.slider('IPK : ', 0.0, 4.0, 2.0, 0.5)
uang_input = st.sidebar.slider('PENGHASILAN : ', 0.0, 10.0, 5.0, 0.5)
jml_input = st.sidebar.slider('TANGGUNGAN : ', 0, 10, 5)

sistem.input['ipk'] = ipk_input
sistem.input['uang'] = uang_input
sistem.input['jml'] = jml_input
sistem.compute()

def display(var, title, result):
    fig, ax = plt.subplots()
    for term_name in var.terms:
        term_mf = var[term_name].mf
        ax.plot(var.universe, term_mf, label=term_name)
    ax.grid(True, alpha=0.35)
    ax.set_title(title, loc='center', fontsize=14)
    ax.set_xlabel(var.label)
    ax.set_ylabel('Derajat keanggotaan')

    # buat garis vertikal
    ax.axvline(x=result, color='black', linestyle='--', label=f'Hasil = {result:.2f}')
    ax.legend()
    st.pyplot(fig)

rekomen_label = max(rekomen.terms, key=lambda term:fuzz.interp_membership(rekomen.universe, rekomen[term].mf, sistem.output['rekomen']))
st.write(f'#### Dengan input : ')
st.write(f'- IPK = {ipk_input}')
st.write(f'- Uang = {uang_input}')
st.write(f'- Tanggungan = {jml_input}')

st.write(f'Menurut ketentuan, skor Rekomendasi Pemberian Beasiswa anda adalah ***{sistem.output['rekomen']:.2f}***')
st.write(f'Maka, anda ***{rekomen_label}*** untuk mendapatkan beasiswa')

with st.expander('Lihat Derajat keanggotaan'):
    kol1, kol2, kol3 = st.tabs(['IPK', 'Penghasilan', 'Tanggungan'])
    with kol1:
        display(ipk, 'Derajat Keanggotaan IPK', ipk_input)
    with kol2:
        display(uang, 'Derajat Keanggotaan Penghasilan', uang_input)
    with kol3:
        display(jml, 'Derajat Keanggotaan Tanggungan', jml_input)
    