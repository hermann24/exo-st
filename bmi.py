import streamlit as st
st.title("Bienvenue au calcul du BMI")
weight = st.number_input("Veuillez entrer votre poids (en kg)")
status = st.radio('Selectionner le format de taille:', ('cm', 'mètre', 'pied'))

if status == 'cm':
    height = st.number_input("Veuillez entrer votre taille en cm")
    try:
        bmi = weight/(height / 100)**2
    except:
        st.text('Entrer une valeur differente de 0 pour la taille')
elif status == 'mètre':
    height = st.number_input("Veuillez entrer votre taille en mètre")
    try:
        bmi = weight/height**2
    except:
        st.text('Entrer une valeur differente de 0 pour la taille')
else :
    height = st.number_input("Veuillez entrer votre taille en pied")
    try:
        bmi = weight/(height * 0.3048)**2
    except:
        st.text('Entrer une valeur differente de 0 pour la taille')

if st.button('Calculer'):
    st.subheader('Votre BMI est :')
    st.subheader(bmi)



