import streamlit as st
import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl
import matplotlib.pyplot as plt

# input dan output
ipk = ctrl.Antecedent(np.arange(0,5,1), 'ipk')
uang = ctrl.Antecedent(np.arange(0,11,1), 'uang')
jmlh = ctrl.Antecedent(np.arange(0,11,1), 'jmlh')

nilai = ctrl.Consequent(np.arange(0,101,1), 'nilai')
finansial = ctrl.Consequent(np.arange(0,101,1), 'finansial')
rekomen = ctrl.Consequent(np.arange(0,101,1), 'rekomen')

# fungsi keanggotaan
ipk['rendah'] = fuzz.gaussmf(ipk.universe, 1.5, 0.6)
ipk['sedang'] = fuzz.gaussmf(ipk.universe, 3, 0.4)
ipk['tinggi'] = fuzz.gaussmf(ipk.universe, 4, 0.2)

uang['rendah'] = fuzz.trimf(uang.universe, [-1, 0, 4])
uang['sedang'] = fuzz.trimf(uang.universe, [2,5,8])
uang['tinggi'] = fuzz.trimf(uang.universe, [6,10,11])

jmlh['sedikit'] = fuzz.trimf(jmlh.universe, [-1, 0, 4])
jmlh['sedang'] = fuzz.trimf(jmlh.universe, [2,5,8])
jmlh['banyak'] = fuzz.trimf(jmlh.universe, [6,10,11])

nilai['rendah'] = fuzz.trimf(nilai.universe, [-1, 0, 40])
nilai['sedang'] = fuzz.trimf(nilai.universe, [30,50,70])
nilai['tinggi'] = fuzz.trimf(nilai.universe, [60,100,101])

finansial['tidak'] = fuzz.trimf(finansial.universe, [-1, 0, 40])
finansial['perlu'] = fuzz.trimf(finansial.universe, [30,50,70])
finansial['sangat'] = fuzz.trimf(finansial.universe, [60,100,101])

rekomen['kurang layak'] = fuzz.trimf(rekomen.universe, [-1, 0, 40])
rekomen['dipertimbangkan'] = fuzz.trimf(rekomen.universe, [30,50,70])
rekomen['sangat layak'] = fuzz.trimf(rekomen.universe, [60,100,101])

rules = [
    ctrl.Rule(ipk['tinggi'] & uang['rendah'] & jmlh['banyak' ], [nilai['tinggi'], finansial['sangat'], rekomen['sangat layak']]),
    ctrl.Rule(ipk['tinggi'] & uang['tinggi'] & jmlh['sedikit'], [nilai['tinggi'], finansial['tidak'], rekomen['kurang layak']]),
    ctrl.Rule(ipk['tinggi'] & uang['sedang'] & jmlh['sedang' ], [nilai['tinggi'], finansial['perlu'], rekomen['sangat layak']]),

    ctrl.Rule(ipk['sedang'] & uang['rendah'] & jmlh['banyak' ], [nilai['sedang'], finansial['sangat'], rekomen['sangat layak']]),
    ctrl.Rule(ipk['sedang'] & uang['tinggi'] & jmlh['sedikit'], [nilai['sedang'], finansial['tidak'], rekomen['dipertimbangkan']]),
    ctrl.Rule(ipk['sedang'] & uang['sedang'] & jmlh['sedang' ], [nilai['sedang'], finansial['perlu'], rekomen['dipertimbangkan']]),

    ctrl.Rule(ipk['rendah'] & uang['rendah'] & jmlh['banyak' ], [nilai['rendah'], finansial['sangat'], rekomen['dipertimbangkan']]),
    ctrl.Rule(ipk['rendah'] & uang['tinggi'] & jmlh['sedikit'], [nilai['rendah'], finansial['tidak'], rekomen['kurang layak']]),
    ctrl.Rule(ipk['rendah'] & uang['sedang'] & jmlh['sedang' ], [nilai['rendah'], finansial['perlu'], rekomen['kurang layak']]),
]

# sistem kontrol
sistem_ctrl = ctrl.ControlSystem(rules)
sistem = ctrl.ControlSystemSimulation(sistem_ctrl)


st.header('Responsi IF-E Fuzzy')
st.write('Amanda Latifa - 123230138')

ipk_input = st.slider('IPK : ',0,4,2)
uang_input = st.slider('Penghasilan Orang tua : ',0,10,5)
jmlh_input = st.slider('Jumlah tanggungan orang tua : ',0,10,5)

# komputasi fuzzy
sistem.input['ipk'] = ipk_input
sistem.input['uang'] = uang_input
sistem.input['jmlh'] = jmlh_input
sistem.compute()

st.write('### hasil')
st.write(f'Nilai : {sistem.output["nilai"]:.2f}')

# masukin visualisasi fungsi keanggotaan ke tab
def plot_and_display_output(variable, title, result):
    fig, ax = plt.subplots()
    for term_name in variable.terms:
        term_mf = variable[term_name].mf
        ax.plot(variable.universe, term_mf, label=term_name)
    ax.grid(True, alpha=0.35)
    ax.set_title(title, loc='center', fontsize=14)
    ax.set_xlabel(variable.label)
    ax.set_ylabel('Derajat Keanggotaan')
    # Menambahkan garis tengah hasil
    ax.axvline(x = result, color='black', linestyle='--', label=f'Hasil : {result:.2f}')
    ax.legend()
    st.pyplot(fig)

with st.expander("Grafik Fungsi Keanggotaan") :
    tab1, tab2, tab3 = st.tabs(['IPK','Penghasilan orang tua','Jumlah tanggungan keluarga'])
    with tab1:
        plot_and_display_output(ipk, "IPK", ipk_input)

    with tab2:
        plot_and_display_output(uang, "Penghasilan orang tua", uang_input)

    with tab3:
        plot_and_display_output(jmlh, "Jumlah tanggungan keluarga", jmlh_input)

    rekomen_label = max(rekomen.terms, key=lambda term: fuzz.interp_membership(rekomen.universe, rekomen[term].mf, sistem.output['rekomen']))
    st.write('### Hasil')
    st.write(f"Nilai akhir mahasiswa : {sistem.output['nilai']:.2f}")
    st.write(f"Tingkat kebutuhan finansial : {sistem.output['finansial']:.2f}")
    st.write(f"Rekomendasi kelayakan beasiswa : {sistem.output['rekomen']:.2f} → **{rekomen_label}**")

