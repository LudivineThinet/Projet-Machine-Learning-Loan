import streamlit as st
import pandas as pd
from modules import onglet_vue_ensemble

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

onglet_vue_ensemble.afficher(df_avec_cible)