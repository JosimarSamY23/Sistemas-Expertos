# Filtrado de Particulas 
import numpy as np

class FiltradoParticulas:
    def __init__(self, num_particulas, rango_estado, ruido_proceso, ruido_medicion):
        self.num_particulas = num_particulas
        self.particulas = np.random.uniform(low=rango_estado[0], high=rango_estado[1], size=num_particulas)
        self.pesos = np.ones(num_particulas) / num_particulas
        self.ruido_proceso = ruido_proceso
        self.ruido_medicion = ruido_medicion

    def predecir(self):
        self.particulas += np.random.normal(0, self.ruido_proceso, self.num_particulas)

    def actualizar(self, medicion):
        self.pesos *= np.exp(-((self.particulas - medicion) ** 2) / (2 * self.ruido_medicion ** 2))
        self.pesos += 1e-300  # Evitar pesos cero
        self.pesos /= np.sum(self.pesos)  # Normalizar

    def reamostrar(self):
        indices = np.random.choice(range(self.num_particulas), size=self.num_particulas, p=self.pesos)
        self.particulas = self.particulas[indices]
        self.pesos = np.ones(self.num_particulas) / self.num_particulas

    def estimar(self):
        return np.sum(self.particulas * self.pesos)

# Simulación
filtro = FiltradoParticulas(num_particulas=1000, rango_estado=(0, 10), ruido_proceso=1, ruido_medicion=2)
mediciones = [5.2, 6.0, 7.1, 8.5]

for medicion in mediciones:
    filtro.predecir()
    filtro.actualizar(medicion)
    filtro.reamostrar()
    estimacion = filtro.estimar()
    print(f"Medición: {medicion}, Estimación: {estimacion}")
