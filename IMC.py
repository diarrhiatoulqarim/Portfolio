import streamlit as st

st.title("Application sur l'IMC")

poids = st.number_input("Saisir le poids (kg)")
taille = st.number_input("Saisir la taille (m)")

if taille > 0:
    IMC = poids / (taille ** 2)

    if IMC < 18.5:
        st.warning("dell thiop gaynn")

    elif 18.5 <= IMC < 25:
        st.success("yakofa am")

    elif 25 <= IMC < 30:
        st.warning("sport boy")

    else:
        st.error("Obésité")

else:
    st.info("Veuillez entrer une taille différente de 0")
