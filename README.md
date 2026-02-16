# ♻️ Detección y Clasificación de Residuos con IA

Este proyecto implementa un sistema de **Inteligencia Artificial y Visión por Computadora** capaz de clasificar residuos sólidos en 6 categorías para facilitar tareas de reciclaje.

El modelo utiliza una red neuronal convolucional (CNN) basada en **MobileNetV2** con técnicas de *Transfer Learning*, alcanzando una precisión del **~80%** en entornos controlados.

## 🚀 Características

* **Clasificación en 6 categorías:** Cartón, Vidrio, Metal, Papel, Plástico y Basura.
* **Interfaz Web Interactiva:** Desarrollada con Streamlit para uso fácil y rápido.
* **Filtro de Confianza:** El sistema alerta si la predicción es incierta (<50%) para evitar falsos positivos.
* **Modelo Optimizado:** Uso de MobileNetV2 para un equilibrio entre velocidad y precisión.

## 🛠️ Requisitos e Instalación

Este proyecto requiere **Python 3.8+**. Para instalar las dependencias necesarias, ejecuta el siguiente comando en tu terminal:

```bash
pip install tensorflow opencv-python-headless matplotlib seaborn scikit-learn pandas streamlit
```

## 📂 Estructura del Proyecto <br>
proyecto_residuos/ <br>
├── dataset/                  # Imágenes organizadas por carpetas (TrashNet) <br>
│   ├── cardboard/ <br>
│   ├── glass/ <br>
│   ├── metal/ <br>
│   ├── paper/ <br>
│   ├── plastic/ <br>
│   └── trash/ <br>
├── entrenamiento.ipynb       # Notebook para entrenar y evaluar el modelo <br>
├── app.py                    # Aplicación web (Interfaz de usuario) <br>
├── modelo_residuos_final.h5  # Archivo del modelo entrenado (se genera tras entrenar) <br>
└── README.md                 # Este archivo <br>

## 💻 Cómo Usar
### 1. Entrenar el Modelo (Opcional)

- Si deseas re-entrenar la inteligencia artificial con nuevos datos: <br>

- Abre el archivo entrenamiento.ipynb en Jupyter Notebook o VS Code. <br>

- Ejecuta todas las celdas. <br>
 
- Al finalizar, se generará el archivo modelo_residuos_final.h5. <br>

### 2. Ejecutar la Aplicación
Para iniciar el clasificador en tu navegador:

```bash
streamlit run app.py
```

Sube una imagen (JPG/PNG) y el sistema te indicará qué tipo de residuo es y en qué contenedor debe depositarse.

## 👤 Autor
Desarrollado por **Samer Ghattas** como parte del proyecto 1 de la materia de **Inteligencia Artificial** en la **Universidad Rafael Urdaneta**. <br>
Maracaibo, Venezuela - 2026.
