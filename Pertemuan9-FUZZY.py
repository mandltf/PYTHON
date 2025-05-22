import streamlit as st
import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl
import matplotlib.pyplot as plt

# definisikan variabel fuzzy
rasa = ctrl.Antecedent(np.arange(0,11,1), 'rasa') #input
pelayanan = ctrl.Antecedent(np.arange(0,11,1), 'pelayanan') #output
tip = ctrl.Consequent(np.arange(0,26,1),'tip') #output

#definiskan fungsi keanggotaan
rasa['tidak_enak'] = fuzz.trimf(rasa.universe, [0,0,5]) #segitiga
rasa['biasa'] = fuzz.trapmf(rasa.universe, [0,4,6,10]) #trapesium
rasa['enak'] = fuzz.trimf(rasa.universe, [5,10,10])

pelayanan['buruk'] = fuzz.trimf(pelayanan.universe, [0,0,5])
pelayanan['biasa'] = fuzz.trapmf(pelayanan.universe, [0,3,7,10])
pelayanan['baik'] = fuzz.trimf(pelayanan.universe, [5,10,10])

tip['sedikit'] = fuzz.trimf(tip.universe, [0,0,12])
tip['sedang'] = fuzz.trimf(tip.universe, [0,12,25])
tip['banyak'] = fuzz.trimf(tip.universe, [12,25,25])

#aturan/rules base
rules = [ctrl.Rule(rasa['tidak_enak'] | pelayanan['buruk'], tip['sedikit']),
        ctrl.Rule(pelayanan['biasa'], tip['sedang']),
        ctrl.Rule(rasa['enak'] & pelayanan['baik'],tip['banyak'])
]

#sistem kontrol berbasis aturan
tipping_ctrl = ctrl.ControlSystem(rules)
tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

#Streamlit
st.title("Sistem Kontrol Berbasis Fuzzy untuk Menghitung Tip")
st.write("### Input Nilai")

# input nilai
rasa_input = st.slider("Rasa : ", 0.0, 10.0, 5.0, 0.5)
pelayanan_input = st.slider("Pelayanan : ", 0.0, 10.0, 5.0, 0.5)

# masukkan value ke sistem
tipping.input['rasa'] = rasa_input
tipping.input['pelayanan'] = pelayanan_input
tipping.compute()

# menampilkan hasil
st.write('### Hasil')
st.write(f"Rasa : {rasa_input}")
st.write(f"Pelayanan : {pelayanan_input}")
st.write(f"Tip : {tipping.output['tip']:.2f}%")

def plot_and_display_membership(variable, title):
    st.write(f'### {title}')
    fig, ax = plt.subplots()
    variable.view(ax = ax)
    st.pyplot(plt.gcf())

plot_and_display_membership(rasa, "Fungsi Keanggotaan Rasa")
plot_and_display_membership(pelayanan, "Fungsi Keanggotaan Pelayanan")
plot_and_display_membership(tip, "Fungsi Keanggotaan Tip")
