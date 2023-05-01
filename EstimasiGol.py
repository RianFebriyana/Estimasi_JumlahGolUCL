import pickle
import streamlit as sl

model = pickle.load(open('estimasi_gol.sav', 'rb'))

sl.title('Estimasi Jumlah Gol')
sl.subheader('Jumlah Gol Di UCL 2021-2022')
sl.write('---')

RightFoot = sl.number_input('Input Total Gol Kaki Kanan')
LeftFoot = sl.number_input('Input Total Gol Kaki Kiri')
Headers = sl.number_input('Input Total Gol Sundulan')
Inside_area = sl.number_input('Input Total Gol Diarea Kotak')
Outside_areas = sl.number_input('Input Total Gol Diluar Kotak')
Penalties = sl.number_input('Input Total Gol Tendangan Pinalti')

predict = ''

if sl.button('Estimasi Gol'):
    predict = model.predict(
        [[RightFoot,LeftFoot,Headers,Inside_area,Outside_areas,Penalties]]
    )
    sl.write ('Estimasi jumlah gol di pertandingan UCL 2021-2022 : ', predict)