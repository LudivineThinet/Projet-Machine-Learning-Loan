import streamlit as st
import pandas as pd
import numpy as np
import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

st.set_page_config(page_title="Simulateur", layout="wide")
st.title("Simulateur de demande de prêt")

modele = joblib.load(BASE_DIR / "model" / "modele_arbre.pkl")
imputer_mode = joblib.load(BASE_DIR / "model" / "imputer_mode.pkl")
imputer_mediane = joblib.load(BASE_DIR / "model" / "imputer_mediane.pkl")
scaler = joblib.load(BASE_DIR / "model" / "scaler_duree.pkl")
mappings = joblib.load(BASE_DIR / "model" / "mappings_encodage.pkl")
colonnes_features = joblib.load(BASE_DIR / "model" / "colonnes_features.pkl")

st.markdown("Remplis les informations du client pour tester l'éligibilité au prêt.")

with st.form("formulaire_simulateur"):
    col1, col2 = st.columns(2)

    with col1:
        genre = st.selectbox("Genre", ["Male", "Female"])
        marier = st.selectbox("Marié(e)", ["Yes", "No"])
        personnes_a_charge = st.selectbox("Personnes à charge", ["0", "1", "2", "3+"])
        niveau_etude = st.selectbox("Niveau d'études", ["Graduate", "Not Graduate"])
        independant = st.selectbox("Travailleur indépendant", ["Yes", "No"])
        zone = st.selectbox("Zone d'habitation", ["Urban", "Rural", "Semiurban"])

    with col2:
        revenu_demandeur = st.number_input("Revenu du demandeur", min_value=0, value=5000)
        revenu_co_demandeur = st.number_input("Revenu du co-demandeur", min_value=0, value=0)
        montant_pret = st.number_input("Montant du prêt demandé", min_value=0, value=150)
        duree_pret = st.selectbox("Durée du prêt (mois)", [12, 36, 60, 84, 120, 180, 240, 300, 360, 480])
        historique_credit = st.selectbox("Historique de crédit", ["Bon (1)", "Mauvais (0)"])

    valider = st.form_submit_button("Simuler la demande")

if valider:
    ligne = {
        'Genre_encoded': mappings['Genre'][genre],
        'Marier_encoded': mappings['Marier'][marier],
        'Personnes_a_charge_encoded': 3.0 if personnes_a_charge == '3+' else float(personnes_a_charge),
        'Niveau_etude_encoded': mappings['Niveau_etude'][niveau_etude],
        'Independant_encoded': mappings['Independant'][independant],
        'Historique_credit': 1.0 if historique_credit == "Bon (1)" else 0.0,
        'Zone_Rural': zone == 'Rural',
        'Zone_Semiurban': zone == 'Semiurban',
        'Zone_Urban': zone == 'Urban',
        'Revenu_demandeur_log': np.log1p(revenu_demandeur),
        'Revenu_co_demandeur_log': np.log1p(revenu_co_demandeur),
        'Montant_pret_log': np.log1p(montant_pret),
        'Duree_pret_std': scaler.transform([[duree_pret]])[0][0]
    }

    X_nouveau = pd.DataFrame([ligne])[colonnes_features]

    prediction = modele.predict(X_nouveau)[0]
    probabilite = modele.predict_proba(X_nouveau)[0]

    st.divider()
    if prediction == 1:
        st.success(f"Prêt accordé (probabilité : {probabilite[1]*100:.1f}%)")
    else:
        st.error(f"Prêt refusé (probabilité de refus : {probabilite[0]*100:.1f}%)")