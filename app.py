import streamlit as st
from textblob import TextBlob
from googletrans import Translator

# Inicializar el traductor
translator = Translator()

# Título de la aplicación
st.title('Análisis de Sentimientos con Emojis, Imágenes y Audios')

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

# Cambiar el color de fondo según el sentimiento
def set_bg_color(color):
    st.markdown(f"""
    <style>
    .stApp {{
        background-color: {color};
    }}
    </style>
    """, unsafe_allow_html=True)

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
        
        # Obtener polaridad y mostrar el emoji, imagen, y audio correspondiente
        x = round(blob.sentiment.polarity, 2)
        
        if x >= 0.5:
            st.write('Es un sentimiento Positivo 😊')
            set_bg_color('yellow')  # Fondo amarillo
            st.image('positivo.png', use_column_width=True)  # Reemplaza 'positivo.png' con la ruta de tu imagen
            audio_file = open('positivo.mp3', 'rb')  # Reemplaza 'positivo.mp3' con la ruta de tu archivo de audio
            st.audio(audio_file.read(), format='audio/mp3', start_time=0)
        elif x <= -0.5:
            st.write('Es un sentimiento Negativo 😔')
            set_bg_color('blue')  # Fondo azul
            st.image('negativo.png', use_column_width=True)  # Reemplaza 'negativo.png' con la ruta de tu imagen
            audio_file = open('negativo.mp3', 'rb')  # Reemplaza 'negativo.mp3' con la ruta de tu archivo de audio
            st.audio(audio_file.read(), format='audio/mp3', start_time=0)
        else:
            st.write('Es un sentimiento Neutral 😐')
            set_bg_color('gray')  # Fondo gris
            st.image('neutral.png', use_column_width=True)  # Reemplaza 'neutral.png' con la ruta de tu imagen
            audio_file = open('neutral.mp3', 'rb')  # Reemplaza 'neutral.mp3' con la ruta de tu archivo de audio
            st.audio(audio_file.read(), format='audio/mp3', start_time=0)

# Corrección de texto en inglés
with st.expander('Corrección en inglés'):
    text2 = st.text_area('Escribe por favor: ', key='4')
    if text2:
        blob2 = TextBlob(text2)
        st.write(blob2.correct())
