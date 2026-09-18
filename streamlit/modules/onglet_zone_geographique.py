import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def afficher(df):
    st.subheader("Zone géographique")

    col1, col2 = st.columns(2)

    with col1:
        fig, ax = plt.subplots(figsize=(5, 4))
        sns.countplot(x='Zone_habitation', data=df, ax=ax)
        ax.set_title("Nombre de demandes par zone")
        st.pyplot(fig)

    with col2:
        taux_zone = df.groupby('Zone_habitation')['Statut_pret'].apply(
            lambda x: (x == 'Y').mean() * 100
        ).sort_values(ascending=False)

        fig, ax = plt.subplots(figsize=(5, 4))
        taux_zone.plot(kind='bar', ax=ax)
        ax.set_title("Taux d'acceptation par zone (%)")
        ax.set_ylabel("Taux d'acceptation (%)")
        st.pyplot(fig)

    montant_zone = df.groupby('Zone_habitation')['Montant_pret'].mean()
    revenu_zone = df.groupby('Zone_habitation')['Revenu_demandeur'].mean()

    st.markdown("**Montant moyen et revenu moyen par zone :**")
    st.dataframe(
        pd.DataFrame({
            'Montant moyen du prêt': montant_zone,
            'Revenu moyen du demandeur': revenu_zone
        }).round(0)
    )

    st.markdown(f"""
    **Ce qu'on observe :** {taux_zone.index[0]} a le meilleur taux d'acceptation
    ({taux_zone.iloc[0]:.1f}%), tandis que {taux_zone.index[-1]} a le taux le plus bas
    ({taux_zone.iloc[-1]:.1f}%). L'écart reste modéré comparé à l'effet de l'historique de crédit.
    """)