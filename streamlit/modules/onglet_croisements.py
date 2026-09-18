import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def afficher(df):
    st.subheader("Croisements avancés")

    st.markdown("**Historique de crédit × Niveau d'études**")
    croisement1 = pd.crosstab([df['Historique_credit'], df['Niveau_etude']], df['Statut_pret'], normalize='index') * 100
    st.dataframe(croisement1.round(1))
    st.caption("L'historique de crédit reste-t-il le facteur dominant quel que soit le niveau d'études ?")

    st.divider()

    st.markdown("**Historique de crédit × Zone géographique**")
    croisement2 = pd.crosstab([df['Historique_credit'], df['Zone_habitation']], df['Statut_pret'], normalize='index') * 100
    st.dataframe(croisement2.round(1))
    st.caption("L'effet de l'historique de crédit varie-t-il selon la zone ?")

    st.divider()

    st.markdown("**Montant du prêt × Statut du prêt**")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.boxplot(x='Statut_pret', y='Montant_pret', data=df, ax=ax)
    ax.set_title("Distribution du montant demandé selon le statut")
    st.pyplot(fig)
    st.caption("Les demandes portant sur des montants élevés sont-elles proportionnellement plus souvent refusées ?")