import streamlit as st
import pandas as pd

st.set_page_config(page_title="Analyse", layout="wide")
st.title("Analyse du portefeuille de prêts")

# Chargement et renommage des colonnes, comme dans le notebook
df = pd.read_csv("../data/loan_data.csv")
df = df.rename(columns={
    'Gender': 'Genre',
    'Married': 'Marier',
    'Dependents': 'Personnes_a_charge',
    'Education': 'Niveau_etude',
    'Self_Employed': 'Independant',
    'ApplicantIncome': 'Revenu_demandeur',
    'CoapplicantIncome': 'Revenu_co_demandeur',
    'LoanAmount': 'Montant_pret',
    'Loan_Amount_Term': 'Duree_pret',
    'Credit_History': 'Historique_credit',
    'Property_Area': 'Zone_habitation',
    'Loan_Status': 'Statut_pret'
})

# On garde uniquement les lignes avec un statut connu, comme dans le notebook
df_avec_cible = df[df['Statut_pret'].notna()].copy()

# KPIs
col1, col2, col3, col4 = st.columns(4)

nb_demandes = len(df_avec_cible)
nb_accordes = (df_avec_cible['Statut_pret'] == 'Y').sum()
taux_accord = nb_accordes / nb_demandes * 100
revenu_moyen = df_avec_cible['Revenu_demandeur'].mean()

col1.metric("Demandes traitées", nb_demandes)
col2.metric("Prêts accordés", nb_accordes)
col3.metric("Taux d'accord", f"{taux_accord:.1f}%")
col4.metric("Revenu moyen demandeur", f"{revenu_moyen:,.0f}")