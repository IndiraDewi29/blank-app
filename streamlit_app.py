import streamlit as st

st.title("🛴Welcome to Indira's webstite!")
st.write("Ayo brunch sushi sambil jalan-jalan di paskal!")
st.image("IMG_0335.jpeg", width=200)
###########
st.title("Aplikasi sederhana")
c1,c2 = st.columns(2)
with c1:
    st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
    angka = st.number_input("Tulis Sebuah Angka:", value=0, step=1)
    if (angka % 2) == 0:
       st.write(f"{angka} adalah bilangan genap")
     else :
       st.write(f"{angka} adalah bilangan ganjil")
