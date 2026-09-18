import streamlit as st
import pandas as pd
from modules import (
    onglet_vue_ensemble,
    onglet_credit_risque,
    onglet_profil_demandeur,
    onglet_revenus_montants,
    onglet_zone_geographique,
    onglet_croisements,
    onglet_performance_modele,
)

st.set_page_config(page_title="Analyse", layout="wide")
st.title("Analyse du portefeuille de prêts")

df = pd.read_csv("../data/loan_data.csv")
df = df.rename(columns={
    'Gender': 'Genre', 'Married': 'Marier', 'Dependents': 'Personnes_a_charge',
    'Education': 'Niveau_etude', 'Self_Employed': 'Independant',
    'ApplicantIncome': 'Revenu_demandeur', 'CoapplicantIncome': 'Revenu_co_demandeur',
    'LoanAmount': 'Montant_pret', 'Loan_Amount_Term': 'Duree_pret',
    'Credit_History': 'Historique_credit', 'Property_Area': 'Zone_habitation',
    'Loan_Status': 'Statut_pret'
})
df_avec_cible = df[df['Statut_pret'].notna()].copy()

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "Vue d'ensemble", "Crédit et risque", "Profil du demandeur",
    "Revenus et montants", "Zone géographique", "Croisements avancés", "Performance du modèle"
])

with tab1:
    onglet_vue_ensemble.afficher(df, df_avec_cible)

with tab2:
    onglet_credit_risque.afficher(df_avec_cible)

with tab3:
    onglet_profil_demandeur.afficher(df_avec_cible)

with tab4:
    onglet_revenus_montants.afficher(df_avec_cible)

with tab5:
    onglet_zone_geographique.afficher(df_avec_cible)

with tab6:
    onglet_croisements.afficher(df_avec_cible)

with tab7:
    onglet_performance_modele.afficher()