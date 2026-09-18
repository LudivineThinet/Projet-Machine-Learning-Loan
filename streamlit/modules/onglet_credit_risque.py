import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def afficher(df):
    st.subheader("Taux d'acceptation selon l'historique de crédit")

    taux = pd.crosstab(df['Historique_credit'], df['Statut_pret'], normalize='index') * 100

    col1, col2 = st.columns(2)

    with col1:
        fig, ax = plt.subplots(figsize=(5, 4))
        sns.countplot(x='Historique_credit', hue='Statut_pret', data=df, ax=ax)
        ax.set_xticklabels(['Mauvais (0)', 'Bon (1)'])
        st.pyplot(fig)

    with col2:
        taux_bon = taux.loc[1.0, 'Y'] if 1.0 in taux.index else 0
        taux_mauvais = taux.loc[0.0, 'Y'] if 0.0 in taux.index else 0

        st.metric("Taux d'acceptation (bon historique)", f"{taux_bon:.1f}%")
        st.metric("Taux d'acceptation (mauvais historique)", f"{taux_mauvais:.1f}%")

        st.markdown(f"""
        **Ce qu'on observe :**
        - Seulement **{taux_mauvais:.1f}%** des personnes avec un mauvais historique de crédit obtiennent malgré tout un prêt.
        - À l'inverse, **{taux_bon:.1f}%** des personnes avec un bon historique sont acceptées.
        - L'historique de crédit est de loin le facteur le plus déterminant dans la décision finale (confirmé aussi par l'importance des variables du modèle final : ~40% du poids de la décision).
        """)