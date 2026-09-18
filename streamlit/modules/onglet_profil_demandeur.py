import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def afficher(df):
    st.subheader("Profil du demandeur")

    variables = {
        'Marier': "Statut matrimonial",
        'Personnes_a_charge': "Personnes à charge",
        'Niveau_etude': "Niveau d'études",
        'Independant': "Travailleur indépendant"
    }

    cols = st.columns(2)

    for i, (col_nom, titre) in enumerate(variables.items()):
        with cols[i % 2]:
            fig, ax = plt.subplots(figsize=(5, 3.5))
            sns.countplot(x=col_nom, hue='Statut_pret', data=df, ax=ax)
            ax.set_title(titre)
            st.pyplot(fig)

    st.markdown("""
    **Ce qu'on observe :** contrairement à l'historique de crédit, ces 4 variables ne montrent
    pas d'écart marqué entre les catégories sur le taux d'acceptation. Elles restent dans le
    dataset et le modèle, mais pèsent peu dans sa décision finale (confirmé par l'importance
    des variables du modèle : proche de 0 pour Genre et Niveau d'études, faible pour les autres).
    """)