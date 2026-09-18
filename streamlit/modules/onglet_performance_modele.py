import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib

def afficher():
    st.subheader("Performance et interprétation du modèle")

    modele = joblib.load("model/modele_arbre.pkl")
    colonnes_features = joblib.load("model/colonnes_features.pkl")

    importances = modele.feature_importances_

    df_importances = pd.DataFrame({
        'Variable': colonnes_features,
        'Importance': importances
    }).sort_values('Importance', ascending=True)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.barh(df_importances['Variable'], df_importances['Importance'])
    ax.set_xlabel("Importance")
    ax.set_title("Importance des variables dans la décision du modèle")
    st.pyplot(fig)

    st.markdown("""
    **Ce qu'on observe :** l'historique de crédit domine très largement la décision du modèle
    (environ 40% du poids), suivi par les variables financières (revenus, montant du prêt).
    Le genre, le niveau d'études et la zone d'habitation pèsent très peu, voire pas du tout,
    dans la décision.
    """)