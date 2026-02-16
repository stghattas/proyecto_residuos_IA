import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Configuracion de la pagina
st.set_page_config(page_title="Detector de Residuos", page_icon="♻️")

# --- Cargar el modelo ---
@st.cache_resource # Esto hace que el modelo no se recargue cada vez que se sube una foto
def load_trained_model():
    return tf.keras.models.load_model('./modelo/modelo_residuos.h5')

try:
    model = load_trained_model()
    st.success("Sistema cargado correctamente.")
except:
    st.error("No se encontro el archivo 'modelo_residuos.h5'. Asegurate de entrenar el modelo primero.")

# Clases (Deben coincidir con el orden alfabetico de tus carpetas en 'dataset')
CLASS_NAMES = ['Carton', 'Vidrio', 'Metal', 'Papel', 'Plastico', 'Basura']

# --- Interfaz Grafica ---
st.title("♻️ Clasificacion Inteligente de Residuos")
st.markdown("""
Sube una imagen de un residuo y la Inteligencia Artificial te dira que es 
y en que contenedor deberia ir.
""")

uploaded_file = st.file_uploader("Elige una imagen...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Mostrar imagen
    image = Image.open(uploaded_file)
    st.image(image, caption='Imagen subida', use_column_width=True)
    
    # Boton para clasificar
    if st.button('Analizar Residuo'):
        with st.spinner('Analizando imagen...'):
            # Preprocesamiento (igual que en el entrenamiento)
            img = image.resize((224, 224))
            img_array = np.array(img)
            img_array = img_array / 255.0  # Normalizar
            img_array = np.expand_dims(img_array, axis=0) # Crear batch de 1

            # Prediccion
            predictions = model.predict(img_array)
            score = tf.nn.softmax(predictions[0])
            predicted_class = CLASS_NAMES[np.argmax(predictions)]
            confidence = 100 * np.max(score)

            # Mostrar resultados
            st.write("---")
            st.subheader(f"Resultado: **{predicted_class}**")
            st.write(f"Confianza del modelo: {confidence:.2f}%")
            
            # Barra de progreso para visualizacion
            st.progress(int(confidence))
            
            # --- FILTRO DE CONFIANZA ---
            # Si la confianza es MENOR al 60%, mostramos advertencia y NO damos consejo de reciclaje
            if confidence < 50:
                st.warning(f"⚠️ No estoy seguro. Parece **{predicted_class}**, pero podria equivocarme ({confidence:.2f}%).")
                st.write("Intenta acercarte mas o mejorar la iluminacion.")
            
            else:
                # Si la confianza es ALTA (>= 60%), mostramos el resultado y tu lógica de contenedores
                st.success(f"Es: **{predicted_class}** ({confidence:.2f}%)")
                st.progress(int(confidence)) # Barra visual de carga

                # --- TU LÓGICA DE CONTENEDORES ---
                if predicted_class in ['Papel', 'Carton']:
                    st.info("ℹ️ Depositar en el contenedor AZUL.")
                elif predicted_class in ['Vidrio']:
                    st.info("ℹ️ Depositar en el contenedor VERDE.")
                elif predicted_class in ['Plastico', 'Metal']:
                    st.info("ℹ️ Depositar en el contenedor AMARILLO.")
                elif predicted_class in ['Basura']:
                    st.info("ℹ️ Depositar en el contenedor GRIS (Restos).")