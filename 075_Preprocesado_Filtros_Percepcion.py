# Preprocesado: Filtros - Filtro Gaussiano
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen
image = cv2.imread('ruta/a/tu/imagen.jpg')

# Convertir la imagen de BGR a RGB
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Aplicar el filtro Gaussiano
# (imagen, (ancho, alto del kernel), desviación estándar)
filtered_image = cv2.GaussianBlur(image, (5, 5), 0)

# Mostrar la imagen original y la imagen filtrada
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Imagen Original')
plt.imshow(image)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Imagen con Filtro Gaussiano')
plt.imshow(filtered_image)
plt.axis('off')

plt.show()
