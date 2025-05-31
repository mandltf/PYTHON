import streamlit as st
import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl
import matplotlib.pyplot as plt

suhu_luar = ctrl.Antecedent(np.arange(0,11,1),'suhu_luar')
suhu_dalam = ctrl.Antecedent(np.arange(0,11,1),'suhu_dalam')
kelembapan = ctrl.Antecedent(np.arange(0,11,1),'kelembapan')
kipas = ctrl.Consequent(np.arange(0,26,1), 'kipas angin')
pendingin_udara = ctrl.Consequent(np.arange(0,26,1), 'pendingin udara')
pemanas = ctrl.Consequent(np.arange(0,26,1), 'pemanas')

# var input
suhu_luar['dingin'] = fuzz.trimf(suhu_luar.universe, [0,0,5])
suhu_luar['sejuk'] = fuzz.trapmf(suhu_luar.universe, [0,4,6,10])
suhu_luar['hangat'] = fuzz.trimf(suhu_luar.universe, [5,10,10])

suhu_dalam['sejuk'] = fuzz.trimf(suhu_dalam.universe, [0,0,5])
suhu_dalam['nyaman'] =fuzz.trapmf(suhu_dalam.universe, [0,3,7,10])
suhu_dalam['hangat'] = fuzz.trimf(suhu_dalam.universe, [5,10,10])

kelembapan['kering'] = fuzz.trimf(kelembapan.universe, [0,0,5])
kelembapan['sedang'] =fuzz.trapmf(kelembapan.universe, [0,4,6,10])
kelembapan['lembab'] = fuzz.trimf(kelembapan.universe, [5,10,10])

# var output
kipas['lambat'] = fuzz.trimf(kipas.universe, [0,0,12])
kipas['sedang'] = fuzz.trimf(kipas.universe, [0,12,25])
kipas['cepat'] =  fuzz.trimf(kipas.universe, [12,25,25])

pendingin_udara['sedikit'] =fuzz.trimf(pendingin_udara.universe, [0,0,12])
pendingin_udara['sedang'] = fuzz.trimf(pendingin_udara.universe, [0,12,25])
pendingin_udara['banyak'] = fuzz.trimf(pendingin_udara.universe, [12,25,25])

pemanas['rendah'] = fuzz.trimf(pemanas.universe, [0,0,12])
pemanas['sedang'] = fuzz.trimf(pemanas.universe, [0,12,25])
pemanas['tinggi'] = fuzz.trimf(pemanas.universe, [12,25,25])

# Rule Base
rules = [
    # Rule 1
    ctrl.Rule(suhu_luar['dingin'] & suhu_dalam['sejuk'] & kelembapan['kering'], kipas['lambat']),
    ctrl.Rule(suhu_luar['dingin'] & suhu_dalam['sejuk'] & kelembapan['kering'], pendingin_udara['sedikit']),
    ctrl.Rule(suhu_luar['dingin'] & suhu_dalam['sejuk'] & kelembapan['kering'], pemanas['tinggi']),

    # Rule 2
    ctrl.Rule(suhu_luar['sejuk'] & suhu_dalam['nyaman'] & kelembapan['sedang'], kipas['sedang']),
    ctrl.Rule(suhu_luar['sejuk'] & suhu_dalam['nyaman'] & kelembapan['sedang'], pendingin_udara['sedang']),
    ctrl.Rule(suhu_luar['sejuk'] & suhu_dalam['nyaman'] & kelembapan['sedang'], pemanas['rendah']),

    # Rule 3
    ctrl.Rule(suhu_luar['hangat'] & suhu_dalam['hangat'] & kelembapan['lembab'], kipas['cepat']),
    ctrl.Rule(suhu_luar['hangat'] & suhu_dalam['hangat'] & kelembapan['lembab'], pendingin_udara['sedikit']),
    ctrl.Rule(suhu_luar['hangat'] & suhu_dalam['hangat'] & kelembapan['lembab'], pemanas['rendah']),

    # Rule 4
    ctrl.Rule(suhu_luar['sejuk'] & suhu_dalam['sejuk'] & kelembapan['sedang'], kipas['lambat']),
    ctrl.Rule(suhu_luar['sejuk'] & suhu_dalam['sejuk'] & kelembapan['sedang'], pendingin_udara['banyak']),
    ctrl.Rule(suhu_luar['sejuk'] & suhu_dalam['sejuk'] & kelembapan['sedang'], pemanas['sedang']),

    # Rule 5
    ctrl.Rule(suhu_luar['hangat'] & suhu_dalam['nyaman'] & kelembapan['sedang'], kipas['cepat']),
    ctrl.Rule(suhu_luar['hangat'] & suhu_dalam['nyaman'] & kelembapan['sedang'], pendingin_udara['sedang']),
    ctrl.Rule(suhu_luar['hangat'] & suhu_dalam['nyaman'] & kelembapan['sedang'], pemanas['rendah']),
]

# Sistem kontrol fuzzy
fan_ctrl = ctrl.ControlSystem(rules)
fan = ctrl.ControlSystemSimulation(fan_ctrl)

ac_ctrl = ctrl.ControlSystem(rules)
ac = ctrl.ControlSystemSimulation(ac_ctrl)

heater_ctrl = ctrl.ControlSystem(rules)
heater = ctrl.ControlSystemSimulation(heater_ctrl)

# tampilan streamlit
st.title("Sistem Kontrol Fuzzy")
st.write("Amanda Latifa - 123230138")

suhu_luar_input = st.slider("Suhu Luar", 0.0, 10.0, 5.0, 0.1)
suhu_dalam_input = st.slider("Suhu Dalam", 0.0, 10.0, 5.0, 0.1)
kelembapan_input = st.slider("Kelembapan", 0.0, 10.0, 5.0, 0.1)

# Komputasi fuzzy
fan.input['suhu_luar'] = suhu_luar_input
fan.input['suhu_dalam'] = suhu_dalam_input
fan.input['kelembapan'] = kelembapan_input
fan.compute()

ac.input['suhu_luar'] = suhu_luar_input
ac.input['suhu_dalam'] = suhu_dalam_input
ac.input['kelembapan'] = kelembapan_input
ac.compute()

heater.input['suhu_luar'] = suhu_luar_input
heater.input['suhu_dalam'] = suhu_dalam_input
heater.input['kelembapan'] = kelembapan_input
heater.compute()

# tampilin hasil
st.write("### Hasil Sistem Kontrol Fuzzy")
st.write(f'Suhu Udara Luar : {suhu_luar_input}')
st.write(f'Suhu Udara Dalam : {suhu_dalam_input}')
st.write(f'Kelembapan Udara : {kelembapan_input}')
st.write(f'Kipas Angin : {fan.output['kipas angin']:.2f}')
st.write(f'Pendingin Udara : {ac.output['pendingin udara']:.2f}')
st.write(f'Pemanas Udara : {heater.output['pemanas']:.2f}')

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
    tab1, tab2, tab3 = st.tabs(['Suhu Udara Luar','Suhu Udara Dalam','Kelembapan'])
    with tab1:
        plot_and_display_output(suhu_luar, "Fungsi Keanggotaan Suhu Udara Luar", suhu_luar_input)

    with tab2:
        plot_and_display_output(suhu_dalam, "Fungsi Keanggotaan Suhu Udara Dalam", suhu_dalam_input)

    with tab3:
        plot_and_display_output(kelembapan, "Fungsi Keanggotaan Kelembapan", kelembapan_input)

