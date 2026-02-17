import streamlit as st

st.title("Application sur l'IMC")

poids = st.number_input("Saisir le poids (kg)")
taille = st.number_input("Saisir la taille (m)")

if taille > 0:
    IMC = poids / (taille ** 2)

    if IMC < 18.5:
        st.warning("Ton IMC est un peu en dessous de la normale, ça peut être bien d’en parler avec un professionnel de santé.")

    elif 18.5 <= IMC < 25:
        st.success("Ton IMC est normal 👍 Continue à garder de bonnes habitudes !")

    elif 25 <= IMC < 30:
        st.warning("Ton IMC est légèrement au-dessus de la normale ⚠️ Pense à adopter de bonnes habitudes (sport, alimentation).")

    else:
        st.error("Ton IMC est élevé ❌ Il est conseillé de consulter un professionnel de santé.")

else:
    st.info("Veuillez entrer une taille différente de 0")

