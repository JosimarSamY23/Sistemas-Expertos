# Aprendizaje Profundo
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Crear la red neuronal con 3 capas
model = Sequential([
    Dense(64, activation='relu', input_shape=(4,)),  # Capa de entrada (4 neuronas)
    Dense(32, activation='relu'),                    # Capa oculta
    Dense(3, activation='softmax')                   # Capa de salida (3 clases)
])

# Compilar el modelo
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Cargar el dataset Iris
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=42)

# Entrenar el modelo
model.fit(X_train, y_train, epochs=50, batch_size=8, verbose=1)

# Evaluar el modelo
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"Precisión del modelo: {accuracy * 100:.2f}%")

