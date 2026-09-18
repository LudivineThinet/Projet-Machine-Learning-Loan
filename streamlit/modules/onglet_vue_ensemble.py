import streamlit as st
import pandas as pd

def afficher(df):
    col1, col2, col3, col4 = st.columns(4)

    nb_demandes = len(df)
    nb_accordes = (df['Statut_pret'] == 'Y').sum()
    nb_refuses = (df['Statut_pret'] == 'N').sum()
    taux_accord = nb_accordes / nb_demandes * 100

    col1.metric("Demandes traitées", nb_demandes)
    col2.metric("Prêts accordés", nb_accordes)
    col3.metric("Prêts refusés", nb_refuses)
    col4.metric("Taux d'acceptation", f"{taux_accord:.1f}%")

    col5, col6, col7, col8 = st.columns(4)
    col5.metric("Montant moyen demandé", f"{df['Montant_pret'].mean():,.0f}")
    col6.metric("Montant total demandé", f"{df['Montant_pret'].sum():,.0f}")
    col7.metric("Revenu moyen", f"{df['Revenu_demandeur'].mean():,.0f}")
    col8.metric("Durée moyenne (mois)", f"{df['Duree_pret'].mean():.0f}")