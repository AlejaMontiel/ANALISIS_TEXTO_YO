import streamlit as st
from textblob import TextBlob
from googletrans import Translator

# Inicializar el traductor
translator = Translator()

# Título de la aplicación
st.title('Análisis de Sentimientos con Emojis')

# Subtítulo y explicación
st.subheader("Por favor escribe en el campo de texto la frase que deseas analizar")
with st.sidebar:
    st.subheader("Polaridad y Subjetividad")
    st.markdown("""
    **Polaridad**: Indica si el sentimiento expresado en el texto es positivo, negativo o neutral. 
    Su valor oscila entre -1 (muy negativo) y 1 (muy positivo), con 0 representando un sentimiento neutral.
    
    **Subjetividad**: Mide cuánto del contenido es subjetivo (opiniones, emociones, creencias) frente a objetivo
    (hechos). Va de 0 a 1, donde 0 es completamente objetivo y 1 es completamente subjetivo.
    """)

# Análisis de polaridad y subjetividad
with st.expander('Analizar Polaridad y Subjetividad en un texto'):
    text1 = st.text_area('Escribe por favor: ')
    if text1:
        # Traducir texto al inglés
        translation = translator.translate(text1, src="es", dest="en")
        trans_text = translation.text
        
        # Crear el objeto TextBlob a partir del texto traducido
        blob = TextBlob(trans_text)
        
        # Mostrar polaridad y subjetividad
        st.write('Polaridad: ', round(blob.sentiment.polarity, 2))
        st.write('Subjetividad: ', round(blob.sentiment.subjectivity, 2))
        
        # Obtener polaridad y mostrar el emoji correspondiente
        x = round(blob.sentiment.polarity, 2)
        if x >= 0.5:
            st.write('Es un sentimiento Positivo 😊')
            st.image('positivo.png', use_column_width=True)
            #st.audio('positivo.mp3')
        elif x <= -0.5:
            st.write('Es un sentimiento Negativo 😔')
            st.image('negativo.jpg', use_column_width=True)
            #st.audio('negativo.mp3')
        else:
            st.write('Es un sentimiento Neutral 😐')
            st.image('neutro.png', use_column_width=True)
            #st.audio('neutro.mp3')

