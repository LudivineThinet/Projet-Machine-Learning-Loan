import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def afficher(df):
    st.subheader("Revenus et montants des prêts")

    col1, col2 = st.columns(2)

    with col1:
        fig, ax = plt.subplots(figsize=(5, 4))
        sns.scatterplot(x='Revenu_demandeur', y='Montant_pret', hue='Statut_pret', data=df, ax=ax)
        ax.set_title("Revenu du demandeur vs Montant du prêt")
        st.pyplot(fig)

    with col2:
        avec_co = df[df['Revenu_co_demandeur'] > 0]['Montant_pret'].mean()
        sans_co = df[df['Revenu_co_demandeur'] == 0]['Montant_pret'].mean()

        st.metric("Montant moyen avec co-demandeur", f"{avec_co:,.0f}")
        st.metric("Montant moyen sans co-demandeur", f"{sans_co:,.0f}")

        corr = df['Revenu_demandeur'].corr(df['Montant_pret'])
        st.markdown(f"""
        **Ce qu'on observe :**
        - Corrélation entre revenu du demandeur et montant du prêt : **{corr:.2f}**, un lien modéré mais réel, plus le revenu est élevé, plus le montant emprunté tend à l'être aussi.
        - Les demandeurs avec un co-demandeur empruntent en moyenne des montants {'plus élevés' if avec_co > sans_co else 'similaires ou plus bas'} que ceux sans co-demandeur.
        """)