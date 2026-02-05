import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('Aplikasi Analisis Sample Superstore')

tab1, tab2 = st.tabs(['Unggah File','Analisis Data'])

with tab1:
    file = st.file_uploader('Unggah File CSV',type='csv')

    if file is not None:
        data = pd.read_csv(file)
        st.write('Isi Dari DataFrame Adalah : ')
        st.dataframe(data)

with tab2:
    #Ubah Tipe Data dari Order Date
    data = pd.read_csv('Sample-Superstore.csv')
    data['Order Date'] = pd.to_datetime(data['Order Date'])
    
    #Menambahkan Atribut Tahun dan Bulan
    data['Year'] = data['Order Date'].dt.year
    data['Month'] = data['Order Date'].dt.month
    
    data_2015 = data[data['Year'] == 2015]
    
    #Statistik Jumlah Transaksi per Bulan Tahun 2015
    transaksi_per_bulan = data_2015.groupby('Month')['Sales'].count().sort_index()
    
    #Buat List Untuk Grafik
    bulan_list = transaksi_per_bulan.index.tolist()
    jml_transaksi = transaksi_per_bulan.values.tolist()
    warna = ['red','blue','blue','blue','blue','blue','blue','blue','blue','blue','red','blue']
    
    st.bar_chart(data=transaksi_per_bulan)
    
    fig, ax = plt.subplots()
    #Buat Grafik
    ax.bar(
        bulan_list,
        jml_transaksi,
        color = warna
    )
    ax.set_title('Jumlah Transaksi Per Bulan Pada Tahun 2015')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Jumlah Transaksi')
    
    st.pyplot(fig)