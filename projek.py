import numpy as np
import pandas as pd
import skfuzzy as fuzz
import skfuzzy.control as ctrl
import matplotlib.pyplot as plt
import streamlit as st


st.set_page_config(page_title='Projek Akhir')
import streamlit as st

# col1, col2 = st.columns([1, 3.5])  # Adjust the ratio as needed

# with col1:
#     st.image('tanaman.png', width=160, )

# with col2:
#     st.title('Sistem Prediksi Kebutuhan Penyiraman Legum')

st.write("#### Dataset tanaman dengan 5 kriteria:")
st.write("- unsur hara (kurang, cukup, berlebih)")
st.write("- temperature (rendah, sedang, tinggi)")
st.write("- humidity (kering, normal, lembab)")
st.write("- rainfall (rendah, sedang, tinggi)")
st.write("- ph (asam, netral, basa)")

data = pd.read_csv('dataset_tanaman.csv')
with st.expander("Dataset Tanaman Legum"):
    # Tentukan kolom yang ingin ditampilkan
    required_columns = ['unsur hara', 'temperature', 'humidity', 'rainfall', 'ph']
    st.dataframe(data[required_columns])

st.sidebar.title("Input Nilai")
unsur_hara_input = st.sidebar.number_input('Input jumlah unsur hara : ', 18, 53)
temperature_input = st.sidebar.number_input('Input jumlah temperature : ', 24, 35)
humidity_input = st.sidebar.number_input('Input jumlah humidity : ', 40, 90)
rainfall_input = st.sidebar.number_input('Input jumlah rainfall : ', 30, 75)
ph_input = st.sidebar.number_input('Input jumlah ph : ', 3, 10)
# st.dataframe(data[required_columns].head(sidebar))

unsur_hara = ctrl.Antecedent(np.arange(18,54,1), 'unsur') #input
temperature = ctrl.Antecedent(np.arange(24, 36, 1), 'temperature')
humidity = ctrl.Antecedent(np.arange(40, 91, 1), 'humidity') 
rainfall = ctrl.Antecedent(np.arange(30, 76, 1), 'rainfall') 
ph = ctrl.Antecedent(np.arange(3, 11, 1), 'ph')
kebutuhan_air = ctrl.Consequent(np.arange(0, 31, 1), 'kebutuhan_air')


unsur_hara['kurang'] = fuzz.trapmf(unsur_hara.universe, [18, 18, 25, 32])
unsur_hara['cukup'] = fuzz.trimf(unsur_hara.universe, [28, 35, 42])
unsur_hara['berlebih'] = fuzz.trapmf(unsur_hara.universe, [40, 45, 53, 53])

temperature['rendah'] = fuzz.trapmf(temperature.universe, [24, 24, 26, 28])
temperature['sedang'] = fuzz.trimf(temperature.universe, [26, 29.5, 33])
temperature['tinggi'] = fuzz.trapmf(temperature.universe, [31, 33, 35, 35])

humidity['kering'] = fuzz.trapmf(humidity.universe, [40, 40, 50, 60])
humidity['normal'] = fuzz.trimf  (humidity.universe, [55, 65, 75])
humidity['lembab'] = fuzz.trapmf (humidity.universe, [70, 80, 90, 90])

rainfall['rendah'] = fuzz.trapmf(rainfall.universe, [30, 30, 40, 50])
rainfall['sedang'] = fuzz.trimf  (rainfall.universe, [45, 58, 70])
rainfall['tinggi'] = fuzz.trapmf (rainfall.universe, [65, 70, 75, 75])

ph['asam'] = fuzz.trapmf  (ph.universe, [3, 3, 4, 5])
ph['netral'] = fuzz.trimf    (ph.universe, [5, 6, 8])
ph['basa'] = fuzz.trapmf   (ph.universe, [7, 8, 10, 10])

kebutuhan_air['sedikit'] = fuzz.trimf(kebutuhan_air.universe, [0, 0, 10])
kebutuhan_air['sedang']  = fuzz.trimf(kebutuhan_air.universe, [5, 15, 25])
kebutuhan_air['banyak']  = fuzz.trimf(kebutuhan_air.universe, [20, 30, 30])

rules = [
    # Rule 1: Panas, kering, asam, curah hujan rendah, unsur hara kurang -> kebutuhan air banyak
    ctrl.Rule(
        temperature['tinggi'] & humidity['kering'] & ph['asam'] & rainfall['rendah'] & unsur_hara['kurang'],
        kebutuhan_air['banyak']
    ),

    # Rule 2: Sedang, normal, netral, curah hujan sedang, unsur hara cukup -> kebutuhan air sedang
    ctrl.Rule(
        temperature['sedang'] & humidity['normal'] & ph['netral'] & rainfall['sedang'] & unsur_hara['cukup'],
        kebutuhan_air['sedang']
    ),

    # Rule 3: Rendah, lembab, basa, curah hujan tinggi, unsur hara berlebih -> kebutuhan air sedikit
    ctrl.Rule(
        temperature['rendah'] & humidity['lembab'] & ph['basa'] & rainfall['tinggi'] & unsur_hara['berlebih'],
        kebutuhan_air['sedikit']
    ),

    # Rule 4: Panas, lembab, netral, curah hujan rendah, unsur hara cukup -> kebutuhan air sedang
    ctrl.Rule(
        temperature['tinggi'] & humidity['lembab'] & ph['netral'] & rainfall['rendah'] & unsur_hara['cukup'],
        kebutuhan_air['sedang']
    ),

    # Rule 5: Sedang, kering, asam, curah hujan sedang, unsur hara berlebih -> kebutuhan air sedang
    ctrl.Rule(
        temperature['sedang'] & humidity['kering'] & ph['asam'] & rainfall['sedang'] & unsur_hara['berlebih'],
        kebutuhan_air['sedang']
    ),
]

# Sistem kontrol fuzzy
watering_legum = ctrl.ControlSystem(rules)
watering = ctrl.ControlSystemSimulation(watering_legum)

# Komputasi fuzzy
watering.input['unsur'] = unsur_hara_input
watering.input['temperature'] = temperature_input
watering.input['humidity'] = humidity_input
watering.input['rainfall'] = rainfall_input
watering.input['ph'] = ph_input
watering.compute()

if st.sidebar.button("Hasil"):
   st.sidebar.markdown(f"Berdasarkan suhu **{temperature_input}°C**, kelembapan **{humidity_input}%**, curah hujan **{rainfall_input} mm**, pH tanah **{ph_input}**, dan unsur hara rata-rata **{unsur_hara_input}** ")
   st.sidebar.markdown(f"kebutuhan air tanaman ditentukan sebesar {watering.output['kebutuhan_air']:.2f} mm/m³.")    

