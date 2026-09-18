import streamlit as st

def formater_nombre(valeur):
    """Affiche un grand nombre en K ou M pour rester lisible."""
    if valeur >= 1_000_000:
        return f"{valeur / 1_000_000:.1f}M"
    elif valeur >= 1_000:
        return f"{valeur / 1_000:.1f}K"
    else:
        return f"{valeur:,.0f}"

def afficher(df, df_avec_cible):
    st.markdown("### Vue d'ensemble")

    total_lignes = len(df)
    lignes_gardees = len(df_avec_cible)
    prets_acceptes = (df_avec_cible['Statut_pret'] == 'Y').sum()
    taux_acceptation = prets_acceptes / lignes_gardees * 100
    montant_moyen = df_avec_cible['Montant_pret'].mean()
    revenu_moyen = df_avec_cible['Revenu_demandeur'].mean()
    duree_moyenne = df_avec_cible['Duree_pret'].mean()

    col1, col2, col3 = st.columns(3)
    col1.metric("Total de lignes (dataset complet)", total_lignes)
    col2.metric("Lignes gardées (statut connu)", lignes_gardees)
    col3.metric("Prêts acceptés", int(prets_acceptes))

    col4, col5, col6 = st.columns(3)
    col4.metric("Taux d'acceptation", f"{taux_acceptation:.1f}%")
    col5.metric("Montant moyen demandé", formater_nombre(montant_moyen))
    col6.metric("Revenu moyen du demandeur", formater_nombre(revenu_moyen))

    col7, _, _ = st.columns(3)
    col7.metric("Durée moyenne des prêts (mois)", f"{duree_moyenne:.0f}")