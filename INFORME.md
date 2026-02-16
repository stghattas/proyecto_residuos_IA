# INFORME DEL PROYECTO DE CLASIFICACION DE RESIDUOS
Detección y Clasificación de Residuos Sólidos mediante Inteligencia Artificial y Visión por Computadora <br>
**Autor**: Samer Ghattas <br>
**Fecha**: Febrero, 2026 <br>
**Ubicación**: Maracaibo, Venezuela <br>

## 1. Resumen Ejecutivo <br>
El presente proyecto aborda la problemática de la gestión de residuos mediante el desarrollo de un sistema inteligente de clasificación automática. Utilizando técnicas de Deep Learning, específicamente Redes Neuronales Convolucionales (CNN), se implementó un modelo capaz de identificar seis categorías de residuos: vidrio, papel, cartón, plástico, metal y basura general. El sistema final, desplegado en una interfaz web con Streamlit, alcanzó una precisión de validación del 80%, demostrando la viabilidad del uso de modelos pre-entrenados (MobileNetV2) para tareas de reciclaje, aunque se identificaron limitaciones importantes en entornos con alta saturación visual (aglomeración de objetos).

## 2. Objetivos
### General: <br> 
Desarrollar un prototipo de software basado en visión artificial para la detección y clasificación de residuos reciclables.

### Específicos:

- Entrenar una Red Neuronal Convolucional (CNN) utilizando la técnica de Transfer Learning.

- Implementar estrategias de Data Augmentation y regularización para optimizar el aprendizaje con datasets limitados.

- Desarrollar una interfaz de usuario interactiva para la clasificación en tiempo real.

- Evaluar el desempeño del modelo métricas de precisión y analizar sus fallos en escenarios reales.

## 3. Metodología <br>

### 3.1. Dataset y Preprocesamiento
Se utilizó el dataset estándar TrashNet, compuesto por aproximadamente 2,5+0

### 3.2. Arquitectura del Modelo
Se optó por la arquitectura MobileNetV2 debido a su eficiencia computacional y bajo consumo de recursos, ideal para implementaciones futuras en dispositivos móviles.

- Base: MobileNetV2 pre-entrenada con pesos de ImageNet (Transfer Learning).

- Fine-Tuning: Se descongelaron las últimas capas del modelo base para permitir que la red aprendiera características específicas de los residuos (texturas de arrugas, transparencias, reflejos).

- Cabezal de Clasificación (Top Layers): Se diseñó una estructura personalizada de capas densas:

- Dense (512 neuronas) + ReLU

- Dropout (0.5): Para reducir el sobreajuste (Overfitting).

- Dense (256 neuronas) + ReLU

- Output Layer (Softmax): 6 neuronas correspondientes a las clases.

- Optimizador: Adam con una tasa de aprendizaje dinámica (Learning Rate Decay) y regularización L2.

## 4. Resultados y Análisis
### 4.1. Métricas de Rendimiento
Tras 40 épocas de entrenamiento, el modelo alcanzó los siguientes resultados:

- Precisión en Entrenamiento (Training Accuracy): ~96%

- Precisión en Validación (Validation Accuracy): ~80%

### 4.2. Análisis de la Convergencia
Las gráficas de entrenamiento muestran una curva de aprendizaje estable. Inicialmente, se observó una brecha significativa entre el entrenamiento y la validación (signo de Overfitting), la cual fue mitigada exitosamente mediante la introducción de capas de Dropout y Regularización L2. El modelo logra generalizar correctamente en el 80% de los casos nuevos presentados bajo condiciones similares al dataset de entrenamiento.

### 4.3. Análisis de la Matriz de Confusión
El análisis detallado de los errores revela patrones lógicos en las confusiones del modelo:

Vidrio vs. Plástico: Existe una confusión recurrente entre estas dos clases. Esto se atribuye a que ambos materiales comparten características visuales clave: son transparentes y presentan reflejos especulares ante la luz.

- Papel vs. Cartón: En imágenes donde el cartón está aplanado o el papel muy arrugado, las texturas se vuelven indistinguibles para la red.

- La clase "Trash": Esta categoría presentó la menor precisión debido a su alta variabilidad intra-clase (contiene desde restos de comida hasta objetos mezclados), dificultando la extracción de patrones únicos.

## 5. Limitaciones del Sistema (Análisis de Casos Reales)
Durante las pruebas de campo con la interfaz de usuario, se identificaron dos limitaciones críticas propias de la arquitectura de "Clasificación" (vs. "Detección"):

- Sensibilidad al Contexto (Fondo): El modelo fue entrenado principalmente con objetos sobre fondos neutros (blancos/lisos). Al probar con imágenes en entornos reales (suelo, calle, mesas con texturas), la confianza del modelo disminuye, ya que el fondo introduce "ruido" visual que la red no aprendió a ignorar completamente.

- Problema de Aglomeración (Clutter): El modelo falla al intentar clasificar imágenes que contienen múltiples objetos apilados (ej. una pila de botellas y bolsas).

- Evidencia: En pruebas con una imagen de múltiples botellas de plástico, el modelo arrojó una confianza baja (~35%) y una clasificación errónea.

- Causa: La arquitectura MobileNetV2 (Clasificador) espera un objeto prominente en el centro de la imagen. Al ver múltiples objetos superpuestos, las características se mezclan, impidiendo una identificación correcta.

## 6. Conclusiones
El proyecto ha cumplido satisfactoriamente su objetivo principal, logrando implementar un sistema funcional de clasificación de residuos con una precisión del 80% en entornos controlados.

### Se concluye que:

El uso de Transfer Learning es indispensable para obtener resultados competitivos con datasets pequeños como TrashNet.

La regularización y el aumento de datos (Data Augmentation) fueron factores determinantes para evitar el memorizado (Overfitting) de las imágenes.

Para llevar este prototipo a un producto comercial capaz de operar en vertederos o calles, sería necesario migrar de un modelo de "Clasificación" a uno de "Detección de Objetos" (como YOLO - You Only Look Once), el cual permitiría identificar y contar múltiples residuos simultáneamente en una sola imagen, superando la limitación de aglomeración detectada en este estudio.

## 7. Tecnologías Utilizadas
- Lenguaje: Python 3.10

- Framework de IA: TensorFlow / Keras

- Visión Artificial: OpenCV

- Interfaz Web: Streamlit

- Visualización: Matplotlib, Seaborn

## 8. Evaluaciones

<img width="567" height="438" alt="image" src="https://github.com/user-attachments/assets/34311618-bf43-4650-af2a-4d5d231ee866" /> <br>

<img width="788" height="679" alt="image" src="https://github.com/user-attachments/assets/6d34e3f9-723f-4a1c-8958-8a7d20323860" />

